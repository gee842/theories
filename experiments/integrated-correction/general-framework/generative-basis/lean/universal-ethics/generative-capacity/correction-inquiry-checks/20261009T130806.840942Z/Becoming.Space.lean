import Becoming.Evolution
import Becoming.Reserve

/-!
# Space: the whole and its parts

Ren proposed that counting all the space, generative and degenerative, gives the theory of
becoming. This module states the structure of that proposal. The space is every world.
The laws stated with no premise hold of each world. The premises of the other theorems are
met by some worlds and not by others, so they carve out parts. The generative, degenerative
and living parts are non-empty, and they overlap.

* **The space.** A world is its relata, read with one kind of relatum (`Becoming.Roles`),
  with the flow among them and their web (`World`). The two-kind reading of any flow and
  web is a world, and arising and ceasing read the same there (`World.ofRoles`,
  `World.generative_ofRoles`, `World.degenerative_ofRoles`).
* **Laws of the whole.** The laws of `Becoming.Change`, and Price's equation in
  `Becoming.Evolution`, are stated of every web and every amount with no premise, so they
  hold throughout the space. Read of parts: in a finite world, generation recurs exactly
  when degeneration does, some relatum ceasing at arbitrarily late steps
  (`World.generative_iff`). The core is constructive, so this reads a world whose activity
  is decided at each step; classically every world is.
* **Finiteness separates them.** Where the relata are infinitely many, either can recur
  without the other (`World.separate`, from `Dawn` and `Dusk`); that these worlds are
  infinite follows from the law.
* **Premises carve parts.** Activity needing support, balance, only active formations
  giving, only active formations taking and only what they draw on, dissipation,
  embodiment and a reserve carrying activity are each met by some worlds and not by others
  (`World.contingent`). They are premises, not laws.
* **Living crosses generation.** Among finite worlds, generation recurring or not occurs
  both with every event living and with some event not living (`World.living_crosses`):
  two sides handing one standing back and forth, the same while each draws on its own
  standing, mutualists active throughout, and a parent drawing a pool down. Neither
  generation nor degeneration decides whether events are living.
* **Dissipation brings a finite world to rest.** In a finite, balanced, dissipative world
  in which whatever arises is embodied, neither generation nor degeneration recurs
  (`World.rests`). Each premise is needed (`World.rests_needs`): a world burning fresh fuel
  keeps generating with infinitely many relata, two sides handing a standing back and
  forth keep generating without dissipation, the same sides without any flow keep
  generating without balance, and a relatum whose activity is not its standing keeps
  arising without embodiment.

Generative, degenerative and living name parts of the space, and none of them is
evaluated here. `Living` is the structural condition that every event is living in the
stepwise reading (`Web.valuation` in `Becoming.Metaethics`). The module does not show that
the theory needs no axiom: it shows which statements need no premise and which premises
carve which parts. No ethical predicate, ranking or axiom occurs.
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

/-- Generation recurs: some relatum arises at arbitrarily late steps. -/
def Generative : Prop :=
  w.web.Unceasing

/-- Degeneration recurs: some relatum ceases at arbitrarily late steps. -/
def Degenerative : Prop :=
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

theorem generative_ofRoles {F C : Type} (L : Flow F C) (W : Web F C) :
    (ofRoles L W).Generative ↔ W.Unceasing :=
  W.roles_unceasing

theorem degenerative_ofRoles {F C : Type} (L : Flow F C) (W : Web F C) :
    (ofRoles L W).Degenerative ↔ ∀ N, ∃ t f, N ≤ t ∧ W.Ceases t f :=
  ⟨fun ceasing N => match ceasing N with
    | ⟨t, .inl f, later, ceases⟩ => ⟨t, f, later, ceases⟩
    | ⟨_, .inr _, _, ceases⟩ => False.elim ceases.1,
   fun ceasing N => match ceasing N with
    | ⟨t, f, later, ceases⟩ => ⟨t, .inl f, later, ceases⟩⟩

/-! ## Laws of the whole -/

/-- In a finite world, generation recurs exactly when degeneration does. The core is
constructive, so whether each relatum is active at each step is decided; classically it
always is. -/
theorem generative_iff [∀ t x, Decidable (w.web.active t x)] (finite : w.Finite) :
    w.Generative ↔ w.Degenerative :=
  match finite with
  | ⟨_, _, every⟩ => w.web.unceasing_iff every

/-- Dissipation brings a finite world to rest: where the flow balances and dissipates and
whatever arises is embodied, neither generation nor degeneration recurs. -/
theorem rests [∀ t x, Decidable (w.web.active t x)] (finite : w.Finite)
    (balanced : w.Balanced) (dissipative : w.Dissipative) (embodied : w.ArisingEmbodied) :
    ¬ w.Generative ∧ ¬ w.Degenerative :=
  match finite with
  | ⟨_, distinct, every⟩ =>
    have quiet : ¬ w.Generative := fun generative =>
      Web.generation_ceases balanced dissipative distinct every fun N =>
        match generative N with
        | ⟨t, x, later, arises⟩ => ⟨t, x, later, embodied t x arises, arises⟩
    ⟨quiet, fun degenerative => quiet ((generative_iff finite).mpr degenerative)⟩

/-! ## Worlds -/

/-- Two sides hand one standing back and forth (`Handing`). -/
def handing : World :=
  ⟨Bool, Handing.flow, Handing.web⟩

instance handing_decided : ∀ t x, Decidable (handing.web.active t x) :=
  fun t x => Nat.decLt 0 (Handing.stands x t)

theorem handing_finite : handing.Finite :=
  ⟨[true, false], Handing.distinct, Handing.every⟩

theorem handing_generative : handing.Generative :=
  fun N => match Handing.recurs true N with
  | ⟨t, later, arises⟩ => ⟨t, true, later, arises⟩

/-- Two sides hand one standing back and forth: a finite world in which generation and
degeneration recur and every event is living. Activity needs support, the flow balances,
only active sides give, and every side is embodied, so the zero reserve carries it; the
sides take without drawing, and the flow does not dissipate. -/
theorem handing_world :
    handing.Finite ∧ handing.Generative ∧ handing.Degenerative ∧ handing.Living ∧
    handing.Dependent ∧ handing.Balanced ∧ handing.Acting ∧ ¬ handing.Taking ∧
    ¬ handing.Dissipative ∧ handing.Embodied ∧ handing.Carried :=
  ⟨handing_finite, handing_generative, (generative_iff handing_finite).mp handing_generative,
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

/-- The same activity as `handing`, so generation and degeneration recur, while not every
event is living: the holder draws on its own standing as it hands it on, the undermining
of `Embodied.ending_breaks`. The flow balances, only active sides give and take, and they
take only from what they draw on. -/
theorem spending_world :
    spending.Finite ∧ spending.Generative ∧ spending.Degenerative ∧ ¬ spending.Living ∧
    spending.Dependent ∧ spending.Balanced ∧ spending.Acting ∧ spending.Taking ∧
    spending.Embodied :=
  have generative : spending.Generative := fun N => match Handing.recurs true N with
    | ⟨t, later, arises⟩ => ⟨t, true, later, arises⟩
  ⟨spending_finite, generative, (generative_iff spending_finite).mp generative,
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
    mutualism.Finite ∧ ¬ mutualism.Generative ∧ ¬ mutualism.Degenerative ∧
    mutualism.Living ∧ mutualism.Dependent ∧ mutualism.Embodied :=
  ⟨mutualism_finite, fun generative => match generative 0 with
    | ⟨_, _, _, arises⟩ => arises.1 trivial,
   fun degenerative => match degenerative 0 with
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

/-- A finite world in which generation does not recur and not every event is living: the
parent's taking leaves the pool below its own need. The pool stands without being active,
so not every relatum is embodied. -/
theorem drawdown_world :
    drawdown.Finite ∧ ¬ drawdown.Generative ∧ ¬ drawdown.Degenerative ∧
    ¬ drawdown.Living ∧ drawdown.Dependent ∧ drawdown.Taking ∧ ¬ drawdown.Embodied :=
  have quiet : ¬ drawdown.Generative := fun generative => match generative 1 with
    | ⟨t, x, later, arises⟩ => drawdown_quiet t x later arises.2
  ⟨drawdown_finite, quiet, fun degenerative => quiet ((generative_iff drawdown_finite).mpr
     degenerative),
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
    unbalanced.Finite ∧ unbalanced.Generative ∧ unbalanced.Dissipative ∧
    unbalanced.Embodied ∧ ¬ unbalanced.Balanced :=
  ⟨⟨[true, false], Handing.distinct, Handing.every⟩, handing_generative,
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

/-- Balanced and dissipative, whatever arises embodied, and generating: so not finite. -/
theorem kindling_world :
    kindling.Balanced ∧ kindling.Dissipative ∧ kindling.ArisingEmbodied ∧
    kindling.Generative ∧ ¬ kindling.Finite :=
  have generative : kindling.Generative := fun N =>
    match Kindling.kindling.2.2.2.2.2 true N with
    | ⟨t, later, arises⟩ => ⟨t, .side true, later, arises⟩
  ⟨Kindling.kindling.1, Kindling.kindling.2.2.2.2.1, kindling_arising, generative,
   fun finite => (rests finite Kindling.kindling.1 Kindling.kindling.2.2.2.2.1
     kindling_arising).1 generative⟩

/-- One relatum whose activity is not its standing (`Flicker`). -/
def flicker : World :=
  ⟨Unit, Flicker.flow, Flicker.web⟩

theorem flicker_world :
    flicker.Finite ∧ flicker.Balanced ∧ flicker.Dissipative ∧ flicker.Generative ∧
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

/-- Where the relata are infinitely many, generation and degeneration separate: either
recurs without the other. -/
theorem separate :
    (dawn.Generative ∧ ¬ dawn.Degenerative ∧ ¬ dawn.Finite) ∧
    (dusk.Degenerative ∧ ¬ dusk.Generative ∧ ¬ dusk.Finite) :=
  have dawnGen : dawn.Generative := (generative_ofRoles _ _).mpr Dawn.unceasing
  have dawnQuiet : ¬ dawn.Degenerative := fun degenerative =>
    match (degenerative_ofRoles _ _).mp degenerative 0 with
    | ⟨t, f, _, ceases⟩ => Dawn.never_ceases t f ceases
  have duskDeg : dusk.Degenerative := (degenerative_ofRoles _ _).mpr Dusk.ceasing
  have duskQuiet : ¬ dusk.Generative := fun generative =>
    match (generative_ofRoles _ _).mp generative 0 with
    | ⟨t, f, _, arises⟩ => Dusk.nothing_arises t f arises
  ⟨⟨dawnGen, dawnQuiet, fun finite => dawnQuiet ((generative_iff finite).mp dawnGen)⟩,
   ⟨duskDeg, duskQuiet, fun finite => duskQuiet ((generative_iff finite).mpr duskDeg)⟩⟩

/-- Living crosses generation: among finite worlds, generation recurring or not occurs
both with every event living and with some event not living. In a finite world
degeneration recurs exactly when generation does, so the same holds of it. -/
theorem living_crosses :
    (handing.Finite ∧ handing.Generative ∧ handing.Living) ∧
    (spending.Finite ∧ spending.Generative ∧ ¬ spending.Living) ∧
    (mutualism.Finite ∧ ¬ mutualism.Generative ∧ mutualism.Living) ∧
    (drawdown.Finite ∧ ¬ drawdown.Generative ∧ ¬ drawdown.Living) :=
  ⟨⟨handing_finite, handing_generative, handing_world.2.2.2.1⟩,
   ⟨spending_finite, spending_world.2.1, spending_world.2.2.2.1⟩,
   ⟨mutualism_finite, mutualism_world.2.1, mutualism_world.2.2.2.1⟩,
   ⟨drawdown_finite, drawdown_world.2.1, drawdown_world.2.2.2.1⟩⟩

/-- Each premise of `rests` is needed: without finiteness, dissipation, balance or
embodiment, generation can recur. -/
theorem rests_needs :
    (kindling.Balanced ∧ kindling.Dissipative ∧ kindling.ArisingEmbodied ∧
      kindling.Generative ∧ ¬ kindling.Finite) ∧
    (handing.Finite ∧ handing.Balanced ∧ handing.ArisingEmbodied ∧ handing.Generative ∧
      ¬ handing.Dissipative) ∧
    (unbalanced.Finite ∧ unbalanced.Dissipative ∧ unbalanced.ArisingEmbodied ∧
      unbalanced.Generative ∧ ¬ unbalanced.Balanced) ∧
    (flicker.Finite ∧ flicker.Balanced ∧ flicker.Dissipative ∧ flicker.Generative ∧
      ¬ flicker.ArisingEmbodied) :=
  ⟨kindling_world,
   ⟨handing_finite, Handing.balances, Embodied.arising handing_world.2.2.2.2.2.2.2.2.2.1,
    handing_generative, handing_world.2.2.2.2.2.2.2.2.1⟩,
   ⟨unbalanced_world.1, unbalanced_world.2.2.1, Embodied.arising unbalanced_world.2.2.2.1,
    unbalanced_world.2.1, unbalanced_world.2.2.2.2⟩,
   flicker_world⟩

end World

end Becoming
