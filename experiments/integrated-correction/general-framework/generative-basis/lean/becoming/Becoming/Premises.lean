import Becoming.Space

/-!
# Premises: how the premises carve the space

`Becoming.Space` shows that each premise of the spine is met by some worlds and not by
others. This module maps the premises against one another: which follow from which, and
that the rest are independent, none following from all the others together.

* **Two more premises as parts.** A census lists the relata active at each step, each
  once, so finitely many are active at each step (`World.Counted`, after
  `Becoming.Population`). Descent transmits every dependence within one bound
  (`World.Transmitting`, after `Becoming.Evolution`).
* **What follows from what.** Activity needing support is the zero reserve, so it is
  carried (`World.Dependent.carried`); where every relatum is embodied, whatever arises is
  (`World.Embodied.arising`). In a finite world whose activity is decided, a census exists
  (`World.Finite.counted`). Where only active relata take and the flow dissipates, only
  active relata give across every enclosed step, since giving needs uptake there; every
  step of a finite world is enclosed (`World.acting_of_enclosed`, `World.Finite.acting`).
* **The rest are independent.** Eight premises remain: activity needing support,
  balance, only active relata giving, only active relata taking and only from what they
  draw on, dissipation, embodiment, a census and bounded transmission (`World.premises`).
  For each, a world meets the other seven and not it (`World.independent`), so none
  follows from the others (`World.none_follows`). The worlds failing a census or only
  active relata giving are infinite, as the implications require.
* **All together.** Mutualists active throughout meet all eight
  (`World.mutualism_premised`). In a finite world the eight together bring the world to
  rest: neither generation nor degeneration recurs (`World.premised_rests`).

Premises stated relative to a further reading, such as a continuation relation
(`Becoming.Identity`), a renewal relation (`Becoming.Generation`), a reserve that decays
(`Becoming.Reserve`) or a family of conditions (`Becoming.Flow`, `Becoming.Dissipation`),
are not mapped here. That each formation taking part in a flow is listed once is a
condition of the representation, not of the world. No ethical predicate, ranking or axiom
occurs.
-/

namespace Becoming

/-! ## Lists and totals -/

/-- A number beyond every member of a list. -/
def beyond : List Nat → Nat
  | [] => 0
  | n :: l => n + 1 + beyond l

theorem lt_beyond {m : Nat} : ∀ {l : List Nat}, m ∈ l → m < beyond l
  | _ :: _, .head _ => Nat.lt_of_lt_of_le (Nat.lt_succ_self m) (Nat.le_add_right _ _)
  | n :: _, .tail _ mem => Nat.lt_of_lt_of_le (lt_beyond mem) (Nat.le_add_left _ (n + 1))

/-- No finite list holds every number. -/
theorem beyond_not_mem (l : List Nat) : ¬ beyond l ∈ l :=
  fun mem => Nat.lt_irrefl _ (lt_beyond mem)

/-- The members of a list at which a decided property holds. -/
def keep {α : Type} (p : α → Prop) [∀ a, Decidable (p a)] : List α → List α
  | [] => []
  | a :: as => if p a then a :: keep p as else keep p as

theorem mem_keep {α : Type} {p : α → Prop} [∀ a, Decidable (p a)] {x : α} :
    ∀ {as : List α}, x ∈ keep p as ↔ x ∈ as ∧ p x
  | [] => ⟨fun no => (nomatch no), fun ⟨no, _⟩ => (nomatch no)⟩
  | a :: as => by
    have ih : x ∈ keep p as ↔ x ∈ as ∧ p x := mem_keep
    show x ∈ (if p a then a :: keep p as else keep p as) ↔ _
    by_cases h : p a
    · rw [if_pos h]
      exact ⟨fun mem => match mem with
          | .head _ => ⟨.head _, h⟩
          | .tail _ mem => ⟨.tail _ (ih.mp mem).1, (ih.mp mem).2⟩,
        fun ⟨mem, px⟩ => match mem with
          | .head _ => .head _
          | .tail _ mem => .tail _ (ih.mpr ⟨mem, px⟩)⟩
    · rw [if_neg h]
      exact ⟨fun mem => ⟨.tail _ (ih.mp mem).1, (ih.mp mem).2⟩,
        fun ⟨mem, px⟩ => match mem with
          | .head _ => absurd px h
          | .tail _ mem => ih.mpr ⟨mem, px⟩⟩

theorem keep_distinct {α : Type} {p : α → Prop} [∀ a, Decidable (p a)] :
    ∀ {as : List α}, Distinct as → Distinct (keep p as)
  | [], _ => trivial
  | a :: as, ⟨fresh, distinct⟩ => by
    show Distinct (if p a then a :: keep p as else keep p as)
    by_cases h : p a
    · rw [if_pos h]
      exact ⟨fun mem => fresh (mem_keep.mp mem).1, keep_distinct distinct⟩
    · rw [if_neg h]
      exact keep_distinct distinct

/-- Giving a family nothing, a formation dissipates on it, whatever it takes. -/
theorem gives_nothing {G T : Nat} (nothing : G = 0) : G + sign T ≤ T :=
  Nat.le_trans (Nat.le_of_eq ((congrArg (· + sign T) nothing).trans (Nat.zero_add _))) (sign_le T)

namespace World

variable (w : World)

/-! ## Two more premises -/

/-- A census lists the relata active at each step, each once: finitely many are active at
each step (`Web.Census`). -/
def Counted : Prop :=
  ∃ alive, w.web.Census alive

/-- Descent transmits every dependence within one bound (`Flow.TransmitsWithin`). -/
def Transmitting : Prop :=
  ∃ δ, ∀ c, w.flow.TransmitsWithin w.web c δ

/-! ## What follows from what -/

variable {w}

/-- Activity needing support is the zero reserve, so it is carried. -/
theorem Dependent.carried (dependent : w.Dependent) : w.Carried :=
  ⟨fun _ _ => 0, Web.carries_zero.mpr dependent⟩

/-- In a finite world whose activity is decided, the active relata at each step can be
listed: a census exists. -/
theorem Finite.counted [∀ t x, Decidable (w.web.active t x)] (finite : w.Finite) :
    w.Counted :=
  match finite with
  | ⟨all, distinct, every⟩ =>
    ⟨fun t => keep (w.web.active t) all, fun _ =>
      ⟨keep_distinct distinct, fun x =>
        ⟨fun active => mem_keep.mpr ⟨every x, active⟩, fun mem => (mem_keep.mp mem).2⟩⟩⟩

/-- In a finite world the exchange of every step lies within the finitely many relata. -/
theorem Finite.enclosed (finite : w.Finite) (t : Nat) : w.flow.Enclosed t :=
  match finite with
  | ⟨all, distinct, every⟩ => ⟨all, distinct, fun _ _ c outside => absurd (every c) outside⟩

/-- Where only active relata take and the flow dissipates, only active relata give across
every enclosed step: giving needs uptake there (`Flow.Dissipative.giving_needs_uptake`). -/
theorem acting_of_enclosed (taking : w.Taking) (dissipative : w.Dissipative)
    (enclosed : ∀ t, w.flow.Enclosed t) : w.Acting :=
  fun t _ _ present gives =>
    match Flow.Dissipative.giving_needs_uptake dissipative (enclosed t) present gives with
    | ⟨_, takes⟩ => (taking t _ _ present takes).1

/-- So in a finite world, where only active relata take and the flow dissipates, only
active relata give. -/
theorem Finite.acting (finite : w.Finite) (taking : w.Taking) (dissipative : w.Dissipative) :
    w.Acting :=
  acting_of_enclosed taking dissipative finite.enclosed

/-- What follows from what. -/
theorem follows :
    (∀ w : World, w.Dependent → w.Carried) ∧
    (∀ w : World, w.Embodied → w.ArisingEmbodied) ∧
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Finite → w.Counted) ∧
    (∀ w : World, (∀ t, w.flow.Enclosed t) → w.Taking → w.Dissipative → w.Acting) ∧
    (∀ w : World, w.Finite → ∀ t, w.flow.Enclosed t) :=
  ⟨fun _ => Dependent.carried, fun _ => Embodied.arising, fun _ _ => Finite.counted,
   fun _ enclosed taking dissipative => acting_of_enclosed taking dissipative enclosed,
   fun _ => Finite.enclosed⟩

/-! ## The premises -/

/-- The eight premises: activity needing support, balance, only active relata giving,
only active relata taking and only from what they draw on, dissipation, embodiment, a
census and bounded transmission. -/
abbrev premises : List (World → Prop) :=
  [Dependent, Balanced, Acting, Taking, Dissipative, Embodied, Counted, Transmitting]

/-- A world meets every premise. -/
def Premised (w : World) : Prop :=
  ∀ P, P ∈ premises → P w

/-- A world meets every premise but `P`, and does not meet `P`. -/
def MeetsAllBut (w : World) (P : World → Prop) : Prop :=
  (∀ Q, Q ∈ premises → Q ≠ P → Q w) ∧ ¬ P w

theorem Premised.of (dependent : w.Dependent) (balanced : w.Balanced) (acting : w.Acting)
    (taking : w.Taking) (dissipative : w.Dissipative) (embodied : w.Embodied)
    (counted : w.Counted) (transmitting : w.Transmitting) : w.Premised
  | _, .head _ => dependent
  | _, .tail _ (.head _) => balanced
  | _, .tail _ (.tail _ (.head _)) => acting
  | _, .tail _ (.tail _ (.tail _ (.head _))) => taking
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.head _)))) => dissipative
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))) => embodied
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))) => counted
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))))) =>
    transmitting
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ no))))))) =>
    nomatch no

theorem MeetsAllBut.of {P : World → Prop}
    (dependent : P ≠ Dependent → w.Dependent) (balanced : P ≠ Balanced → w.Balanced)
    (acting : P ≠ Acting → w.Acting) (taking : P ≠ Taking → w.Taking)
    (dissipative : P ≠ Dissipative → w.Dissipative) (embodied : P ≠ Embodied → w.Embodied)
    (counted : P ≠ Counted → w.Counted) (transmitting : P ≠ Transmitting → w.Transmitting)
    (fails : ¬ P w) : w.MeetsAllBut P :=
  ⟨fun Q mem ne => match Q, mem, ne with
    | _, .head _, ne => dependent fun same => ne same.symm
    | _, .tail _ (.head _), ne => balanced fun same => ne same.symm
    | _, .tail _ (.tail _ (.head _)), ne => acting fun same => ne same.symm
    | _, .tail _ (.tail _ (.tail _ (.head _))), ne => taking fun same => ne same.symm
    | _, .tail _ (.tail _ (.tail _ (.tail _ (.head _)))), ne =>
      dissipative fun same => ne same.symm
    | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))), ne =>
      embodied fun same => ne same.symm
    | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))), ne =>
      counted fun same => ne same.symm
    | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))))), ne =>
      transmitting fun same => ne same.symm
    | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ no))))))), _ =>
      (nomatch no),
   fails⟩

/-- Where nothing takes part, nothing gives, takes or descends, and dissipation holds
vacuously. -/
theorem still_vacuous {R : Type} (W : Web R R) :
    (⟨R, Flow.still, W⟩ : World).Acting ∧ (⟨R, Flow.still, W⟩ : World).Taking ∧
    (⟨R, Flow.still, W⟩ : World).Dissipative ∧ (⟨R, Flow.still, W⟩ : World).Transmitting :=
  ⟨fun _ _ _ present _ => (nomatch present), fun _ _ _ present _ => (nomatch present),
   Flow.still_dissipative, ⟨0, fun _ _ _ _ descends _ => (nomatch descends.1)⟩⟩

/-- Where no level changes, nothing comes to stand, so nothing descends. -/
theorem steady_transmitting {w : World} (steady : ∀ t x, w.web.level (t + 1) x = w.web.level t x) :
    w.Transmitting :=
  ⟨0, fun _ t x _ descends _ => absurd (Nat.lt_of_lt_of_le descends.2.2.2
    (Nat.le_of_eq (steady t x))) descends.2.2.1⟩

/-! ## Independence -/

namespace Strained

/-- One relatum standing at one, active throughout, depending on itself at need two. -/
def web : Web Unit Unit where
  level _ _ := 1
  active _ _ := True
  requires _ _ _ := True
  need _ _ _ := 2
  draws _ _ _ := False

end Strained

/-- A relatum active beyond its own standing, with no flow. -/
def strained : World :=
  ⟨Unit, Flow.still, Strained.web⟩

instance strained_decided : ∀ t x, Decidable (strained.web.active t x) :=
  fun _ _ => isTrue trivial

theorem strained_finite : strained.Finite :=
  ⟨[()], ⟨fun no => (nomatch no), trivial⟩, fun () => .head _⟩

/-- Every premise but activity needing support. -/
theorem strained_but : strained.MeetsAllBut Dependent :=
  .of (fun ne => absurd rfl ne) (fun _ _ _ => rfl) (fun _ => (still_vacuous _).1)
    (fun _ => (still_vacuous _).2.1) (fun _ => (still_vacuous _).2.2.1)
    (fun _ _ _ => ⟨fun _ => Nat.zero_lt_one, fun _ => trivial⟩)
    (fun _ => strained_finite.counted) (fun _ => (still_vacuous _).2.2.2)
    fun dependent => Nat.not_succ_le_self 1 (dependent 0 () trivial () trivial)

instance unbalanced_decided : ∀ t x, Decidable (unbalanced.web.active t x) :=
  fun t x => Nat.decLt 0 (Handing.stands x t)

/-- Every premise but balance: the sides of `Handing` with no flow. -/
theorem unbalanced_but : unbalanced.MeetsAllBut Balanced :=
  .of (fun _ => Handing.dependent) (fun ne => absurd rfl ne) (fun _ => (still_vacuous _).1)
    (fun _ => (still_vacuous _).2.1) (fun _ => (still_vacuous _).2.2.1)
    (fun _ => unbalanced_world.2.2.2.1) (fun _ => unbalanced_world.1.counted)
    (fun _ => (still_vacuous _).2.2.2) unbalanced_world.2.2.2.2

namespace Scatter

inductive Relatum where
  | taker
  | giver
  | ground (n : Nat)

/-- One unit at each ground relatum and nothing elsewhere. -/
def unit : Relatum → Nat
  | .taker => 0
  | .giver => 0
  | .ground _ => 1

/-- The taker stands at one; the giver and the ground stand at nothing. -/
def level : Relatum → Nat
  | .taker => 1
  | .giver => 0
  | .ground _ => 0

/-- Across every step the giver gives a unit to every ground relatum and the taker takes
it back. -/
def flow : Flow Relatum Relatum where
  present _ := [.taker, .giver]
  take _ x y := match x with
    | .taker => unit y
    | .giver => 0
    | .ground _ => 0
  give _ x y := match x with
    | .taker => 0
    | .giver => unit y
    | .ground _ => 0

/-- A relatum is active while it stands; the taker draws on everything. -/
def web : Web Relatum Relatum where
  level _ x := level x
  active _ x := 0 < level x
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ x _ := x = .taker

/-- The index of a ground relatum. -/
def index : Relatum → Nat
  | .taker => 0
  | .giver => 0
  | .ground n => n

/-- No finite family holds every ground relatum. -/
theorem outside (cs : List Relatum) : ¬ Relatum.ground (beyond (cs.map index)) ∈ cs :=
  fun mem => beyond_not_mem _ (mem_map_of (g := index) mem)

end Scatter

/-- A relatum never active gives to infinitely many while an active one takes as much
back. -/
def scatter : World :=
  ⟨Scatter.Relatum, Scatter.flow, Scatter.web⟩

/-- Every premise but only active relata giving. No step is enclosed: the exchange of
every step reaches infinitely many relata, so dissipation holds vacuously. -/
theorem scatter_but : scatter.MeetsAllBut Acting :=
  .of (fun _ _ _ _ _ no => no.elim)
    (fun _ _ c => match c with
      | .taker => rfl
      | .giver => rfl
      | .ground _ => rfl)
    (fun ne => absurd rfl ne)
    (fun _ _ f _ present takes => match f, present, takes with
      | .taker, _, _ => ⟨Nat.zero_lt_one, rfl⟩
      | .giver, _, takes => absurd takes (Nat.lt_irrefl 0)
      | .ground _, .tail _ (.tail _ no), _ => nomatch no)
    (fun _ cs _ _ closed => absurd
      (closed .taker (.head _) (.ground (beyond (cs.map Scatter.index)))
        (Scatter.outside cs)).1.symm Nat.zero_ne_one)
    (fun _ _ _ => Iff.rfl)
    (fun _ => ⟨fun _ => [.taker], fun _ => ⟨⟨fun no => (nomatch no), trivial⟩, fun x =>
      match x with
      | .taker => ⟨fun _ => .head _, fun _ => Nat.zero_lt_one⟩
      | .giver => ⟨fun no => absurd no (Nat.lt_irrefl 0),
          fun mem => match mem with | .tail _ no => (nomatch no)⟩
      | .ground _ => ⟨fun no => absurd no (Nat.lt_irrefl 0),
          fun mem => match mem with | .tail _ no => (nomatch no)⟩⟩⟩)
    (fun _ => steady_transmitting fun _ _ => rfl)
    fun acting => Nat.lt_irrefl 0 (acting 0 .giver (.ground 0) (.tail _ (.head _))
      Nat.zero_lt_one)

namespace Morsel

inductive Relatum where
  | eater
  | morsel

/-- One at the first step, nothing after. -/
def first : Nat → Nat
  | 0 => 1
  | _ + 1 => 0

/-- The eater stands at one throughout; the morsel at one at the first step. -/
def level (t : Nat) : Relatum → Nat
  | .eater => 1
  | .morsel => first t

/-- Across the first step the eater takes the morsel. -/
def flow : Flow Relatum Relatum where
  present _ := [.eater]
  take t x y := match x, y with
    | .eater, .morsel => first t
    | .eater, .eater => 0
    | .morsel, .eater => 0
    | .morsel, .morsel => 0
  give _ _ _ := 0

/-- A relatum is active while it stands; nothing depends on or draws on anything. -/
def web : Web Relatum Relatum where
  level := level
  active t x := 0 < level t x
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

end Morsel

/-- An eater takes a morsel it does not draw on. -/
def morsel : World :=
  ⟨Morsel.Relatum, Morsel.flow, Morsel.web⟩

instance morsel_decided : ∀ t x, Decidable (morsel.web.active t x) :=
  fun t x => Nat.decLt 0 (Morsel.level t x)

theorem morsel_finite : morsel.Finite :=
  ⟨[.eater, .morsel],
   ⟨fun mem => match mem with | .tail _ no => (nomatch no), fun no => (nomatch no), trivial⟩,
   fun
    | .eater => .head _
    | .morsel => .tail _ (.head _)⟩

/-- Every premise but only active relata taking and only from what they draw on. -/
theorem morsel_but : morsel.MeetsAllBut Taking :=
  .of (fun _ _ _ _ _ no => no.elim)
    (fun _ t c => match t, c with
      | _, .eater => rfl
      | 0, .morsel => rfl
      | _ + 1, .morsel => rfl)
    (fun _ _ _ _ _ gives => absurd gives (Nat.lt_irrefl 0))
    (fun ne => absurd rfl ne)
    (fun _ cs _ _ _ _ _ => gives_nothing (total_zero cs))
    (fun _ _ _ => Iff.rfl) (fun _ => morsel_finite.counted)
    (fun _ => ⟨0, fun _ _ x _ descends _ => match x, descends.2.2 with
      | .eater, comes => absurd Nat.zero_lt_one comes.1
      | .morsel, comes => absurd comes.2 (Nat.lt_irrefl 0)⟩)
    fun taking => (taking 0 .eater .morsel (.head _) Nat.zero_lt_one).2

namespace Keeping

inductive Relatum where
  | keeper
  | store

/-- One unit, at the store. -/
def atStore : Relatum → Nat
  | .keeper => 0
  | .store => 1

/-- Across every step the keeper takes the store's unit and gives it back. -/
def flow : Flow Relatum Relatum where
  present _ := [.keeper]
  take _ x y := match x with
    | .keeper => atStore y
    | .store => 0
  give _ x y := match x with
    | .keeper => atStore y
    | .store => 0

/-- Both stand at one and are active throughout; the keeper depends on the store at need
one and draws on it. -/
def web : Web Relatum Relatum where
  level _ _ := 1
  active _ _ := True
  requires _ x y := x = .keeper ∧ y = .store
  need _ _ _ := 1
  draws _ x y := x = .keeper ∧ y = .store

end Keeping

/-- A keeper takes its store's unit and gives it back: nothing is lost. -/
def keeping : World :=
  ⟨Keeping.Relatum, Keeping.flow, Keeping.web⟩

instance keeping_decided : ∀ t x, Decidable (keeping.web.active t x) :=
  fun _ _ => isTrue trivial

theorem keeping_finite : keeping.Finite :=
  ⟨[.keeper, .store],
   ⟨fun mem => match mem with | .tail _ no => (nomatch no), fun no => (nomatch no), trivial⟩,
   fun
    | .keeper => .head _
    | .store => .tail _ (.head _)⟩

/-- Every premise but dissipation: the store, closed around, is given as much as is taken
from it. -/
theorem keeping_but : keeping.MeetsAllBut Dissipative :=
  .of (fun _ _ _ _ _ _ => Nat.le_refl 1) (fun _ _ _ => rfl) (fun _ _ _ _ _ _ => trivial)
    (fun _ _ f c present takes => match f, present, c, takes with
      | .keeper, _, .store, _ => ⟨trivial, rfl, rfl⟩
      | .keeper, _, .keeper, takes => absurd takes (Nat.lt_irrefl 0)
      | .store, .tail _ no, _, _ => nomatch no)
    (fun ne => absurd rfl ne)
    (fun _ _ _ => ⟨fun _ => Nat.zero_lt_one, fun _ => trivial⟩)
    (fun _ => keeping_finite.counted) (fun _ => steady_transmitting fun _ _ => rfl)
    fun dissipative => Nat.not_succ_le_self 1
      (dissipative [.store] 0 ⟨fun no => (nomatch no), trivial⟩
        (fun f present c outside => match f, present, c, outside with
          | .keeper, _, .keeper, _ => ⟨rfl, rfl⟩
          | .keeper, _, .store, outside => absurd (.head _) outside
          | .store, .tail _ no, _, _ => nomatch no)
        .keeper (.head _))

namespace Latent

/-- One relatum standing at one throughout and never active. -/
def web : Web Unit Unit where
  level _ _ := 1
  active _ _ := False
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

end Latent

/-- A relatum that stands and is never active, with no flow. -/
def latent : World :=
  ⟨Unit, Flow.still, Latent.web⟩

instance latent_decided : ∀ t x, Decidable (latent.web.active t x) :=
  fun _ _ => isFalse id

theorem latent_finite : latent.Finite :=
  ⟨[()], ⟨fun no => (nomatch no), trivial⟩, fun () => .head _⟩

/-- Every premise but embodiment. -/
theorem latent_but : latent.MeetsAllBut Embodied :=
  .of (fun _ _ _ no => no.elim) (fun _ _ _ => rfl) (fun _ => (still_vacuous _).1)
    (fun _ => (still_vacuous _).2.1) (fun _ => (still_vacuous _).2.2.1) (fun ne => absurd rfl ne)
    (fun _ => latent_finite.counted) (fun _ => (still_vacuous _).2.2.2)
    fun embodied => (embodied () 0).mpr Nat.zero_lt_one

namespace Multitude

/-- Every number stands at one and is active throughout. -/
def web : Web Nat Nat where
  level _ _ := 1
  active _ _ := True
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

end Multitude

/-- Infinitely many relata active at once, with no flow. -/
def multitude : World :=
  ⟨Nat, Flow.still, Multitude.web⟩

/-- Every premise but a census. -/
theorem multitude_but : multitude.MeetsAllBut Counted :=
  .of (fun _ _ _ _ _ no => no.elim) (fun _ _ _ => rfl) (fun _ => (still_vacuous _).1)
    (fun _ => (still_vacuous _).2.1) (fun _ => (still_vacuous _).2.2.1)
    (fun _ _ _ => ⟨fun _ => Nat.zero_lt_one, fun _ => trivial⟩) (fun ne => absurd rfl ne)
    (fun _ => (still_vacuous _).2.2.2)
    fun ⟨alive, census⟩ => beyond_not_mem (alive 0) (((census 0).2 (beyond (alive 0))).mp trivial)

namespace Novel

inductive Relatum where
  | parent
  | fuel
  | child

/-- `k` at the first step, nothing after. -/
def firstly (k : Nat) : Nat → Nat
  | 0 => k
  | _ + 1 => 0

/-- Nothing at the first step, one after. -/
def after : Nat → Nat
  | 0 => 0
  | _ + 1 => 1

/-- The parent stands at one throughout, the fuel at two at the first step, the child at
one after it. -/
def level (t : Nat) : Relatum → Nat
  | .parent => 1
  | .fuel => firstly 2 t
  | .child => after t

/-- What the parent takes: the fuel's two units, across the first step. -/
def fromFuel (t : Nat) : Relatum → Nat
  | .parent => 0
  | .fuel => firstly 2 t
  | .child => 0

/-- What the parent gives: one unit to the child, across the first step. -/
def toChild (t : Nat) : Relatum → Nat
  | .parent => 0
  | .fuel => 0
  | .child => firstly 1 t

def flow : Flow Relatum Relatum where
  present _ := [.parent]
  take t x y := match x with
    | .parent => fromFuel t y
    | .fuel => 0
    | .child => 0
  give t x y := match x with
    | .parent => toChild t y
    | .fuel => 0
    | .child => 0

/-- A relatum is active while it stands. The child depends on the parent at need one, a
dependence the parent never had; the parent draws on the fuel. -/
def web : Web Relatum Relatum where
  level := level
  active t x := 0 < level t x
  requires _ x y := match x with
    | .parent => False
    | .fuel => False
    | .child => y = .parent
  need _ _ _ := 1
  draws _ x y := x = .parent ∧ y = .fuel

theorem fuel_mem_or : ∀ cs : List Relatum, Relatum.fuel ∈ cs ∨ ¬ Relatum.fuel ∈ cs
  | [] => .inr fun no => (nomatch no)
  | .fuel :: _ => .inl (.head _)
  | .parent :: cs => match fuel_mem_or cs with
    | .inl mem => .inl (.tail _ mem)
    | .inr out => .inr fun mem => match mem with | .tail _ mem => out mem
  | .child :: cs => match fuel_mem_or cs with
    | .inl mem => .inl (.tail _ mem)
    | .inr out => .inr fun mem => match mem with | .tail _ mem => out mem

end Novel

/-- A parent burns fuel to give a child its standing, and the child comes to depend on the
parent. -/
def novel : World :=
  ⟨Novel.Relatum, Novel.flow, Novel.web⟩

instance novel_decided : ∀ t x, Decidable (novel.web.active t x) :=
  fun t x => Nat.decLt 0 (Novel.level t x)

theorem novel_finite : novel.Finite :=
  ⟨[.parent, .fuel, .child],
   ⟨fun mem => match mem with
     | .tail _ (.tail _ no) => (nomatch no),
    fun mem => match mem with | .tail _ no => (nomatch no), fun no => (nomatch no), trivial⟩,
   fun
    | .parent => .head _
    | .fuel => .tail _ (.head _)
    | .child => .tail _ (.tail _ (.head _))⟩

/-- Across the first step the parent gives the closed family no more than one unit and
takes two from it. -/
theorem novel_dissipative : novel.Dissipative :=
  fun cs t distinct closed f present => match f, present, t with
  | .parent, _, 0 =>
    match Novel.fuel_mem_or cs with
    | .inl mem =>
      have given : total cs (novel.flow.give 0 .parent) ≤ 1 :=
        total_le_at (a := .child) (fun b positive => match b, positive with
          | .child, _ => rfl
          | .parent, positive => absurd positive (Nat.lt_irrefl 0)
          | .fuel, positive => absurd positive (Nat.lt_irrefl 0)) distinct
      have taken : 2 ≤ total cs (novel.flow.take 0 .parent) :=
        le_total_of_mem (q := novel.flow.take 0 .parent) mem
      Nat.le_trans (Nat.add_le_add given (sign_le_one _)) taken
    | .inr out => absurd (Nat.le_of_eq (closed .parent (.head _) .fuel out).1)
        (Nat.not_succ_le_zero 1)
  | .parent, _, _ + 1 => gives_nothing (total_eq_zero fun c _ => match c with
      | .parent => rfl
      | .fuel => rfl
      | .child => rfl)
  | .fuel, .tail _ no, _ => nomatch no
  | .child, .tail _ no, _ => nomatch no

/-- Every premise but bounded transmission: the child descends from the parent and
depends on it, while the parent depended on nothing. -/
theorem novel_but : novel.MeetsAllBut Transmitting :=
  .of (fun _ _ f _ c requires => match f, c, requires with
      | .child, .parent, _ => Nat.le_refl 1
      | .child, .fuel, no => nomatch no
      | .child, .child, no => nomatch no
      | .parent, _, no => no.elim
      | .fuel, _, no => no.elim)
    (fun _ t c => match t, c with
      | _, .parent => rfl
      | 0, .fuel => rfl
      | _ + 1, .fuel => rfl
      | 0, .child => rfl
      | _ + 1, .child => rfl)
    (fun _ _ f _ present _ => match f, present with
      | .parent, _ => Nat.zero_lt_one
      | .fuel, .tail _ no => nomatch no
      | .child, .tail _ no => nomatch no)
    (fun _ _ f c present takes => match f, present, c, takes with
      | .parent, _, .fuel, _ => ⟨Nat.zero_lt_one, rfl, rfl⟩
      | .parent, _, .parent, takes => absurd takes (Nat.lt_irrefl 0)
      | .parent, _, .child, takes => absurd takes (Nat.lt_irrefl 0)
      | .fuel, .tail _ no, _, _ => nomatch no
      | .child, .tail _ no, _, _ => nomatch no)
    (fun _ => novel_dissipative) (fun _ _ _ => Iff.rfl) (fun _ => novel_finite.counted)
    (fun ne => absurd rfl ne)
    fun ⟨_, transmits⟩ => (transmits .parent 0 .child .parent
      ⟨.head _, Nat.zero_lt_one, Nat.lt_irrefl 0, Nat.zero_lt_one⟩ rfl).1

/-- The premises are independent: for each, a world meets the other seven and not it. -/
theorem independent :
    strained.MeetsAllBut Dependent ∧ unbalanced.MeetsAllBut Balanced ∧
    scatter.MeetsAllBut Acting ∧ morsel.MeetsAllBut Taking ∧
    keeping.MeetsAllBut Dissipative ∧ latent.MeetsAllBut Embodied ∧
    multitude.MeetsAllBut Counted ∧ novel.MeetsAllBut Transmitting :=
  ⟨strained_but, unbalanced_but, scatter_but, morsel_but, keeping_but, latent_but,
   multitude_but, novel_but⟩

/-- So no premise follows from the others. -/
theorem none_follows :
    ∀ P, P ∈ premises → ¬ ∀ w : World, (∀ Q, Q ∈ premises → Q ≠ P → Q w) → P w
  | _, .head _ => fun follows => strained_but.2 (follows _ strained_but.1)
  | _, .tail _ (.head _) => fun follows => unbalanced_but.2 (follows _ unbalanced_but.1)
  | _, .tail _ (.tail _ (.head _)) => fun follows => scatter_but.2 (follows _ scatter_but.1)
  | _, .tail _ (.tail _ (.tail _ (.head _))) => fun follows =>
    morsel_but.2 (follows _ morsel_but.1)
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.head _)))) => fun follows =>
    keeping_but.2 (follows _ keeping_but.1)
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))) => fun follows =>
    latent_but.2 (follows _ latent_but.1)
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))) => fun follows =>
    multitude_but.2 (follows _ multitude_but.1)
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))))) =>
    fun follows => novel_but.2 (follows _ novel_but.1)
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ no))))))) =>
    nomatch no

/-! ## All together -/

instance mutualism_decided : ∀ t x, Decidable (mutualism.web.active t x) :=
  fun _ _ => isTrue trivial

/-- Mutualists active throughout meet every premise. -/
theorem mutualism_premised : mutualism.Premised :=
  .of Mutualism.dependent (fun _ _ => rfl) (still_vacuous _).1 (still_vacuous _).2.1
    (still_vacuous _).2.2.1 mutualism_world.2.2.2.2.2 mutualism_finite.counted
    (still_vacuous _).2.2.2

/-- In a finite world the premises together bring the world to rest: neither generation
nor degeneration recurs. -/
theorem premised_rests [∀ t x, Decidable (w.web.active t x)] (finite : w.Finite)
    (premised : w.Premised) : ¬ w.Generative ∧ ¬ w.Degenerative :=
  rests finite (premised _ (.tail _ (.head _)))
    (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))))
    (Embodied.arising (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))))))

end World

end Becoming
