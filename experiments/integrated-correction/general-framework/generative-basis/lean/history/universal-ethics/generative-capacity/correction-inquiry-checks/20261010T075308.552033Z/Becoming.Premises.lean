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
  active relata give across an enclosed step, since giving needs uptake there
  (`World.acting_across`); so only active relata give where every step is enclosed,
  as every step of a finite world is (`World.acting_of_enclosed`,
  `World.Finite.acting`).
* **The rest are independent.** Eight premises remain: activity needing support,
  balance, only active relata giving, only active relata taking and only from what they
  draw on, dissipation, embodiment, a census and bounded transmission (`World.premises`).
  For each, a world meets the other seven and not it (`World.independent`), so none
  follows from the others (`World.none_follows`). The worlds failing a census or only
  active relata giving are infinite, as the implications require. Independence is
  relative to these eight: finiteness, enclosure and decidability, on which the rest
  theorems turn, are not among them, and with them only active relata giving and a
  census follow. Several witnesses have no flow, so the four premises about the flow
  hold there vacuously; that suffices for independence. For balance a second witness
  takes from a closed family at every step, so taking and dissipation bind there
  (`World.draining_but`).
* **All together.** Mutualists active throughout meet all eight
  (`World.mutualism_premised`), the four about the flow vacuously, since nothing flows.
  A finite world whose activity is decided and which meets the eight comes to rest:
  neither arising nor ceasing recurs (`World.premised_rests`). The proof uses three of
  them: balance, dissipation and embodiment.
* **Each binding.** A premise binds where something meets its condition (`World.Binds`).
  In `hatch` all eight hold and each binds (`World.hatch_binds`): a parent takes two
  units of food and its own unit and gives its young one unit; the young comes to stand
  depending on the food as the parent did, and the parent ceases. Activity needing
  support binds without being tight, the food never falling below the need, and the four
  premises about the flow bind at the first step only. A census binds in that the world
  is not finite, its infinitely many ground relata idle (`World.hatch_idle`): only the
  food, the parent and the child are ever active (`World.hatch_ever`), and a census exists
  wherever some list holds every relatum ever active and activity is decided
  (`World.counted_of_ever`). In every world that comes to rest under the rest theorem,
  not unboundedly many relata are ever active or stand (`World.rest_few` in
  `Becoming.Openness`), so there a census binds only so.
* **Counting under the premises.** Relata queuing with nothing flowing meet every premise
  but embodiment, and relata queuing that stand exactly while active meet every premise
  but balance (`World.queue_premised`, `World.embodiedQueue_premised`). So a property of
  the counts of a census holds in every world meeting either seven exactly when it holds
  of every tally (`World.counting_free`): premises lacking balance or embodiment leave
  counting free. Together, with only active relata giving, they bind it: what arises is
  given by a relatum active at the step, so under a census nothing arises across a step at
  which nothing is active, which is no law of tallies (`World.counting_binds_jointly`).
  That is all the eight premises add. A queue tended by its front, which gives to each
  relatum joining, takes from each leaving and, while active, exchanges a unit each way
  with every ground relatum, meets all eight wherever nothing joins an empty queue
  (`World.tendedQueue_premised`). So a property of the counts holds in every world meeting
  the eight exactly when it holds of every tally in which nothing arises across a step at
  which nothing is active (`World.premised_counting`). Three of the eight hold idly in the
  tended queue: nothing taking part takes from a closed family, and nothing depends on
  anything (`World.tended_not_binds`). Where every premise binds, every census counts
  something arising (`World.binds_arising`), which is no law under the eight alone
  (`World.binds_adds`). No step at which the front is active is enclosed; under enclosure
  from some step on change is bounded as well (`Becoming.Openness`).

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

/-- Where every member of which a decided determination ever holds is on one list
without repetition, what holds is listed at each step. -/
theorem listed_of_ever {α : Type} {p : α → Nat → Prop} [∀ a t, Decidable (p a t)]
    {L : List α} (distinct : Distinct L) (ever : ∀ t a, p a t → a ∈ L) :
    Listed p (fun t => keep (fun a => p a t) L) :=
  fun t => ⟨keep_distinct distinct, fun a =>
    ⟨fun holds => mem_keep.mpr ⟨ever t a holds, holds⟩, fun mem => (mem_keep.mp mem).2⟩⟩

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

/-- A world whose activity is decided and whose relata ever active lie on one list has a
census (the eleventh review's probe). -/
theorem counted_of_ever [∀ t x, Decidable (w.web.active t x)] {L : List w.Relatum}
    (distinct : Distinct L) (ever : ∀ t x, w.web.active t x → x ∈ L) : w.Counted :=
  ⟨_, listed_of_ever (p := fun x t => w.web.active t x) distinct ever⟩

/-- In a finite world the exchange of every step lies within the finitely many relata. -/
theorem Finite.enclosed (finite : w.Finite) (t : Nat) : w.flow.Enclosed t :=
  match finite with
  | ⟨all, distinct, every⟩ => ⟨all, distinct, fun _ _ c outside => absurd (every c) outside⟩

/-- Where only active relata take and the flow dissipates, only active relata give across
an enclosed step: giving needs uptake there (`Flow.Dissipative.giving_needs_uptake`). -/
theorem acting_across (taking : w.Taking) (dissipative : w.Dissipative) {t : Nat}
    (enclosed : w.flow.Enclosed t) {f c : w.Relatum} (present : f ∈ w.flow.present t)
    (gives : 0 < w.flow.give t f c) : w.web.active t f :=
  match Flow.Dissipative.giving_needs_uptake dissipative enclosed present gives with
  | ⟨_, takes⟩ => (taking t _ _ present takes).1

/-- So where every step is enclosed, only active relata give. -/
theorem acting_of_enclosed (taking : w.Taking) (dissipative : w.Dissipative)
    (enclosed : ∀ t, w.flow.Enclosed t) : w.Acting :=
  fun t _ _ present gives => acting_across taking dissipative (enclosed t) present gives

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

/-- The flow of `leaking` on the web of `spending`: the holder takes its own unit at every
step, drawing on it, and gives nothing (the tenth review's probe). -/
def draining : World :=
  ⟨Bool, Leaking.flow, Spending.web⟩

instance draining_decided : ∀ t x, Decidable (draining.web.active t x) :=
  fun t x => Nat.decLt 0 (Handing.stands x t)

/-- Every premise but balance, with taking and dissipation binding: the family of both
sides is closed and taken from at every step. -/
theorem draining_but :
    draining.MeetsAllBut Balanced ∧
    ∀ t, Leaking.flow.ClosedAt [true, false] t ∧
      0 < total [true, false] (Leaking.flow.take t (Handing.holder t)) :=
  ⟨.of (fun _ => Handing.dependent) (fun ne => absurd rfl ne)
     (fun _ _ _ _ _ gives => absurd gives (Nat.lt_irrefl 0))
     (fun _ => Spending.taking) (fun _ => leaking_world.2.2.1)
     (fun _ _ _ => Iff.rfl)
     (fun _ => Finite.counted (w := draining) ⟨[true, false], Handing.distinct, Handing.every⟩)
     (fun _ => ⟨0, fun _ _ _ _ descends _ => absurd descends.2.1 (Nat.lt_irrefl 0)⟩)
     leaking_world.2.2.2.2.1,
   leaking_world.2.2.2.2.2⟩

namespace Scatter

inductive Relatum where
  | taker
  | source
  | ground (n : Nat)

/-- One unit at each ground relatum and nothing elsewhere. -/
def unit : Relatum → Nat
  | .taker => 0
  | .source => 0
  | .ground _ => 1

/-- The taker stands at one; the source and the ground stand at nothing. -/
def level : Relatum → Nat
  | .taker => 1
  | .source => 0
  | .ground _ => 0

/-- Across every step the source gives a unit to every ground relatum and the taker takes
it back. -/
def flow : Flow Relatum Relatum where
  present _ := [.taker, .source]
  take _ x y := match x with
    | .taker => unit y
    | .source => 0
    | .ground _ => 0
  give _ x y := match x with
    | .taker => 0
    | .source => unit y
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
  | .source => 0
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
      | .source => rfl
      | .ground _ => rfl)
    (fun ne => absurd rfl ne)
    (fun _ _ f _ present takes => match f, present, takes with
      | .taker, _, _ => ⟨Nat.zero_lt_one, rfl⟩
      | .source, _, takes => absurd takes (Nat.lt_irrefl 0)
      | .ground _, .tail _ (.tail _ no), _ => nomatch no)
    (fun _ cs _ _ closed => absurd
      (closed .taker (.head _) (.ground (beyond (cs.map Scatter.index)))
        (Scatter.outside cs)).1.symm Nat.zero_ne_one)
    (fun _ _ _ => Iff.rfl)
    (fun _ => ⟨fun _ => [.taker], fun _ => ⟨⟨fun no => (nomatch no), trivial⟩, fun x =>
      match x with
      | .taker => ⟨fun _ => .head _, fun _ => Nat.zero_lt_one⟩
      | .source => ⟨fun no => absurd no (Nat.lt_irrefl 0),
          fun mem => match mem with | .tail _ no => (nomatch no)⟩
      | .ground _ => ⟨fun no => absurd no (Nat.lt_irrefl 0),
          fun mem => match mem with | .tail _ no => (nomatch no)⟩⟩⟩)
    (fun _ => steady_transmitting fun _ _ => rfl)
    fun acting => Nat.lt_irrefl 0 (acting 0 .source (.ground 0) (.tail _ (.head _))
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

/-- A finite world whose activity is decided and which meets the premises comes to rest:
neither arising nor ceasing recurs. The proof uses balance, dissipation and embodiment. -/
theorem premised_rests [∀ t x, Decidable (w.web.active t x)] (finite : w.Finite)
    (premised : w.Premised) : ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  rests finite (premised _ (.tail _ (.head _)))
    (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))))
    (Embodied.arising (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))))))

/-- Each premise binds: something meets its condition, so the premise constrains the
world rather than holding vacuously. Activity needing support binds where an active
relatum depends on a condition at a positive need; balance where a level changes; only
active relata giving, and only active relata taking, where something taking part gives,
and takes; dissipation where something taking part takes from a closed family; embodiment
where a relatum arises; a census where the world is not finite, which says only that the
census does not follow from the world being finite, not that it does work beyond finitely
many relata ever active (`rest_few`); and bounded transmission where a descendant depends
on a condition at its first standing step. -/
structure Binds (w : World) : Prop where
  dependent : ∃ t f c, w.web.active t f ∧ w.web.requires t f c ∧ 0 < w.web.need t f c
  balanced : ∃ t c, w.web.level (t + 1) c ≠ w.web.level t c
  acting : ∃ t f c, f ∈ w.flow.present t ∧ 0 < w.flow.give t f c
  taking : ∃ t f c, f ∈ w.flow.present t ∧ 0 < w.flow.take t f c
  dissipative : ∃ cs t f, Distinct cs ∧ w.flow.ClosedAt cs t ∧ f ∈ w.flow.present t ∧
    0 < total cs (w.flow.take t f)
  embodied : ∃ t x, w.web.Arises t x
  counted : ¬ w.Finite
  transmitting : ∃ t x g c, w.flow.DescendsAt w.web t x g ∧ w.web.requires (t + 1) x c

namespace Hatch

inductive Relatum where
  | food
  | parent
  | child
  | ground (n : Nat)

/-- The food stands at three at the first step and one after it, the parent at one at the
first step and nothing after, the child at nothing at the first step and one after; the
ground relata stand at nothing. -/
def level (t : Nat) : Relatum → Nat
  | .food => Novel.firstly 2 t + 1
  | .parent => Novel.firstly 1 t
  | .child => Novel.after t
  | .ground _ => 0

/-- What the parent takes: two units of food and its own unit. -/
def fed : Relatum → Nat
  | .food => 2
  | .parent => 1
  | .child => 0
  | .ground _ => 0

/-- What the parent gives: one unit to the child. -/
def toChild : Relatum → Nat
  | .food => 0
  | .parent => 0
  | .child => 1
  | .ground _ => 0

/-- Across the first step the parent takes two units of food and its own unit, and gives
the child one unit. -/
def flow : Flow Relatum Relatum where
  present
    | 0 => [.parent]
    | _ + 1 => []
  take _ x y := match x with
    | .food => 0
    | .parent => fed y
    | .child => 0
    | .ground _ => 0
  give _ x y := match x with
    | .food => 0
    | .parent => toChild y
    | .child => 0
    | .ground _ => 0

/-- The parent and the child live on the food. -/
def eats : Relatum → Prop
  | .food => False
  | .parent => True
  | .child => True
  | .ground _ => False

/-- A relatum is active while it stands. The parent and the child depend on the food at
need one; the parent draws on the food and on itself. -/
def web : Web Relatum Relatum where
  level := level
  active t x := 0 < level t x
  requires _ x y := eats x ∧ y = .food
  need _ _ _ := 1
  draws _ x y := x = .parent ∧ (y = .food ∨ y = .parent)

/-- Only the parent takes part, and only across the first step. -/
theorem taking_part : ∀ {t : Nat} {g : Relatum}, g ∈ flow.present t → t = 0 ∧ g = .parent
  | 0, _, .head _ => ⟨rfl, rfl⟩
  | 0, _, .tail _ no => nomatch no
  | _ + 1, _, no => nomatch no

/-- The food, the parent and the child. -/
abbrev kin : List Relatum :=
  [.food, .parent, .child]

theorem kin_distinct : Distinct kin :=
  ⟨fun mem => match mem with | .tail _ (.tail _ no) => (nomatch no),
   fun mem => match mem with | .tail _ no => (nomatch no), fun no => (nomatch no), trivial⟩

/-- Every step's exchange lies within the food, the parent and the child. -/
theorem closed (t : Nat) : flow.ClosedAt kin t :=
  fun f present c out => match f, taking_part present, c, out with
  | _, ⟨_, rfl⟩, .food, out => absurd (.head _) out
  | _, ⟨_, rfl⟩, .parent, out => absurd (.tail _ (.head _)) out
  | _, ⟨_, rfl⟩, .child, out => absurd (.tail _ (.tail _ (.head _))) out
  | _, ⟨_, rfl⟩, .ground _, _ => ⟨rfl, rfl⟩

/-- The food and the parent are active at the first step, the food and the child after it. -/
def alive : Nat → List Relatum
  | 0 => [.food, .parent]
  | _ + 1 => [.food, .child]

def index : Relatum → Nat
  | .food => 0
  | .parent => 0
  | .child => 0
  | .ground n => n

/-- No finite family holds every ground relatum. -/
theorem outside (cs : List Relatum) : ¬ Relatum.ground (beyond (cs.map index)) ∈ cs :=
  fun mem => beyond_not_mem _ (mem_map_of (g := index) mem)

end Hatch

/-- A parent takes food and its own unit to give its young one unit; the young comes to
stand depending on the food as the parent did, and the parent ceases. Infinitely many
ground relata stand at nothing and take no part (`hatch_idle`). -/
def hatch : World :=
  ⟨Hatch.Relatum, Hatch.flow, Hatch.web⟩

theorem hatch_balanced : hatch.Balanced
  | 0, .food => rfl
  | 0, .parent => rfl
  | 0, .child => rfl
  | 0, .ground _ => rfl
  | _ + 1, .food => rfl
  | _ + 1, .parent => rfl
  | _ + 1, .child => rfl
  | _ + 1, .ground _ => rfl

/-- Across the first step the parent gives the closed family one unit and takes at least
the food's two. -/
theorem hatch_dissipative : hatch.Dissipative :=
  fun cs t distinct closed f present => match t, f, Hatch.taking_part present with
  | _, _, ⟨rfl, rfl⟩ =>
    have given : total cs (hatch.flow.give 0 .parent) ≤ 1 :=
      total_le_at (a := .child) (fun b positive => match b, positive with
        | .child, _ => rfl
        | .food, positive => absurd positive (Nat.lt_irrefl 0)
        | .parent, positive => absurd positive (Nat.lt_irrefl 0)
        | .ground _, positive => absurd positive (Nat.lt_irrefl 0)) distinct
    Decidable.of_not_not fun wrong => absurd (Nat.le_of_eq (closed .parent present .food
      fun mem => wrong (Nat.le_trans (Nat.add_le_add given (sign_le_one _))
        (le_total_of_mem (q := hatch.flow.take 0 .parent) mem))).1) (Nat.not_succ_le_zero 1)

theorem hatch_counted : hatch.Counted :=
  ⟨Hatch.alive, fun
    | 0 => ⟨⟨fun mem => match mem with | .tail _ no => (nomatch no), fun no => (nomatch no),
        trivial⟩, fun
      | .food => ⟨fun _ => .head _, fun _ => Nat.zero_lt_succ _⟩
      | .parent => ⟨fun _ => .tail _ (.head _), fun _ => Nat.zero_lt_one⟩
      | .child => ⟨fun no => absurd no (Nat.lt_irrefl 0),
          fun mem => match mem with | .tail _ (.tail _ no) => nomatch no⟩
      | .ground _ => ⟨fun no => absurd no (Nat.lt_irrefl 0),
          fun mem => match mem with | .tail _ (.tail _ no) => nomatch no⟩⟩
    | _ + 1 => ⟨⟨fun mem => match mem with | .tail _ no => (nomatch no), fun no => (nomatch no),
        trivial⟩, fun
      | .food => ⟨fun _ => .head _, fun _ => Nat.zero_lt_one⟩
      | .parent => ⟨fun no => absurd no (Nat.lt_irrefl 0),
          fun mem => match mem with | .tail _ (.tail _ no) => nomatch no⟩
      | .child => ⟨fun _ => .tail _ (.head _), fun _ => Nat.zero_lt_one⟩
      | .ground _ => ⟨fun no => absurd no (Nat.lt_irrefl 0),
          fun mem => match mem with | .tail _ (.tail _ no) => nomatch no⟩⟩⟩

/-- All eight premises hold in `hatch`, and each binds: the parent depends on the food,
the food falls, the parent gives and takes, taking from the closed family of food, parent
and child, the child arises, the world is not finite, and the child depends on the food at
its first standing step as the parent did. -/
theorem hatch_binds : hatch.Premised ∧ hatch.Binds :=
  ⟨.of (fun _ _ _ c requires => match c, requires with | _, ⟨_, rfl⟩ => Nat.le_add_left 1 _)
      hatch_balanced
      (fun t f _ present _ => match t, f, Hatch.taking_part present with
        | _, _, ⟨rfl, rfl⟩ => Nat.zero_lt_one)
      (fun t f c present takes => match t, f, Hatch.taking_part present, c, takes with
        | _, _, ⟨rfl, rfl⟩, .food, _ => ⟨Nat.zero_lt_one, rfl, .inl rfl⟩
        | _, _, ⟨rfl, rfl⟩, .parent, _ => ⟨Nat.zero_lt_one, rfl, .inr rfl⟩
        | _, _, ⟨rfl, rfl⟩, .child, takes => absurd takes (Nat.lt_irrefl 0)
        | _, _, ⟨rfl, rfl⟩, .ground _, takes => absurd takes (Nat.lt_irrefl 0))
      hatch_dissipative (fun _ _ => Iff.rfl) hatch_counted
      ⟨0, fun _ _ _ g descends requires => match g, Hatch.taking_part descends.1 with
        | _, ⟨_, rfl⟩ => ⟨⟨trivial, requires.2⟩, Nat.le_refl 1⟩⟩,
   ⟨⟨0, .parent, .food, Nat.zero_lt_one, ⟨trivial, rfl⟩, Nat.zero_lt_one⟩,
    ⟨0, .food, Nat.ne_of_lt (Nat.succ_lt_succ (Nat.zero_lt_succ 1))⟩,
    ⟨0, .parent, .child, .head _, Nat.zero_lt_one⟩,
    ⟨0, .parent, .food, .head _, Nat.zero_lt_two⟩,
    ⟨Hatch.kin, 0, .parent, Hatch.kin_distinct, Hatch.closed 0, .head _,
      Nat.lt_of_lt_of_le Nat.zero_lt_two (le_total_of_mem (a := Hatch.Relatum.food)
        (q := hatch.flow.take 0 Hatch.Relatum.parent) (.head _))⟩,
    ⟨0, .child, Nat.lt_irrefl 0, Nat.zero_lt_one⟩,
    fun ⟨all, _, every⟩ => Hatch.outside all (every _),
    ⟨0, .child, .parent, .food, ⟨.head _, Nat.zero_lt_one, Nat.lt_irrefl 0, Nat.zero_lt_one⟩,
      ⟨trivial, rfl⟩⟩⟩⟩

/-- Only the food, the parent and the child are ever active in `hatch`, so its census is a
census of these three (`counted_of_ever`). -/
theorem hatch_ever : ∀ t x, hatch.web.active t x → x ∈ Hatch.kin
  | _, .food, _ => .head _
  | _, .parent, _ => .tail _ (.head _)
  | _, .child, _ => .tail _ (.tail _ (.head _))
  | _, .ground _, active => absurd active (Nat.lt_irrefl 0)

/-- The ground relata of `hatch` are idle: at every step each stands at nothing and is not
active, takes no part in the flow, is neither taken from nor given to, and is neither
depended on nor drawn on (the eleventh review's probe). -/
theorem hatch_idle (t n : Nat) :
    hatch.web.level t (.ground n) = 0 ∧ ¬ hatch.web.active t (.ground n) ∧
    ¬ Hatch.Relatum.ground n ∈ hatch.flow.present t ∧
    (∀ f, hatch.flow.take t f (.ground n) = 0 ∧ hatch.flow.give t f (.ground n) = 0) ∧
    (∀ f, ¬ hatch.web.requires t f (.ground n)) ∧ (∀ f, ¬ hatch.web.draws t f (.ground n)) :=
  ⟨rfl, Nat.lt_irrefl 0,
   fun mem => match t, mem with
     | 0, .tail _ no => (nomatch no)
     | _ + 1, no => (nomatch no),
   fun f => match f with
     | .food => ⟨rfl, rfl⟩
     | .parent => ⟨rfl, rfl⟩
     | .child => ⟨rfl, rfl⟩
     | .ground _ => ⟨rfl, rfl⟩,
   fun _ requires => (nomatch requires.2),
   fun _ draws => match draws.2 with
     | .inl no => (nomatch no)
     | .inr no => (nomatch no)⟩


/-! ## Counting under the premises -/

/-- `Q` holds of the counts of every census of the world: how many are active at each step,
how many cease and how many arise across it. -/
def CountsObey (w : World) [∀ t x, Decidable (w.web.active t x)]
    (Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop) : Prop :=
  ∀ alive, w.web.Census alive → Q (fun t => (alive t).length)
    (fun t => ceasings (alive t) (fun x s => w.web.active s x) t)
    (fun t => comings (alive (t + 1)) (fun x s => w.web.active s x) t)

end World

namespace Queue

/-- Relata in a queue, each active from the step it joins to the step it leaves; nothing
stands, depends or draws. -/
def web (n c : Nat → Nat) : Web Nat Nat where
  level _ _ := 0
  active t k := holds n c k t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- The same queue, each relatum standing exactly while it is active. -/
def embodied (n c : Nat → Nat) : Web Nat Nat :=
  { web n c with level := fun t k => mark (holds n c k t) }

/-- None at the first step, one from then on. -/
def lone : Nat → Nat
  | 0 => 0
  | _ + 1 => 1

/-- One joins across the first step and none after. -/
def joins : Nat → Nat
  | 0 => 1
  | _ + 1 => 0

/-- One relatum comes to be across the first step, from none, and stays. -/
theorem lone_tally : Tally lone (fun _ => 0) joins
  | 0 => ⟨0, rfl, rfl⟩
  | _ + 1 => ⟨1, rfl, rfl⟩

end Queue

namespace World

/-- Relata queue, with nothing flowing. -/
def queue (n c : Nat → Nat) : World :=
  ⟨Nat, Flow.still, Queue.web n c⟩

/-- Relata queue, each standing exactly while it is active, with nothing flowing. -/
def embodiedQueue (n c : Nat → Nat) : World :=
  ⟨Nat, Flow.still, Queue.embodied n c⟩

instance queue_decided (n c : Nat → Nat) : ∀ t x, Decidable ((queue n c).web.active t x) :=
  fun t x => inferInstanceAs (Decidable (Queue.holds n c x t))

instance embodiedQueue_decided (n c : Nat → Nat) :
    ∀ t x, Decidable ((embodiedQueue n c).web.active t x) :=
  fun t x => inferInstanceAs (Decidable (Queue.holds n c x t))

/-- A queue meets every premise but embodiment: nothing depends, stands or flows. -/
theorem queue_premised (n c : Nat → Nat) :
    (queue n c).Dependent ∧ (queue n c).Balanced ∧ (queue n c).Acting ∧
      (queue n c).Taking ∧ (queue n c).Dissipative ∧ (queue n c).Counted ∧
      (queue n c).Transmitting :=
  ⟨fun _ _ _ _ no => (nomatch no), fun _ _ => rfl, (still_vacuous _).1, (still_vacuous _).2.1,
   (still_vacuous _).2.2.1, ⟨_, Queue.listed⟩, (still_vacuous _).2.2.2⟩

/-- A queue standing while active meets every premise but balance: its standing changes
with nothing flowing. -/
theorem embodiedQueue_premised (n c : Nat → Nat) :
    (embodiedQueue n c).Dependent ∧ (embodiedQueue n c).Acting ∧
      (embodiedQueue n c).Taking ∧ (embodiedQueue n c).Dissipative ∧
      (embodiedQueue n c).Embodied ∧ (embodiedQueue n c).Counted ∧
      (embodiedQueue n c).Transmitting :=
  ⟨fun _ _ _ _ no => (nomatch no), (still_vacuous _).1, (still_vacuous _).2.1,
   (still_vacuous _).2.2.1, fun _ _ => mark_pos.symm, ⟨_, Queue.listed⟩,
   (still_vacuous _).2.2.2⟩

/-- The premises leave counting free. A property of the counts holds of every tally exactly
when it holds of the census of every world; and already when it holds of the census of
every world meeting every premise but embodiment, or of every world meeting every premise
but balance. -/
theorem counting_free {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop}
    (pointwise : Pointwise Q) :
    ((∀ n c a, Tally n c a → Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.CountsObey Q) ∧
    ((∀ n c a, Tally n c a → Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Dependent → w.Balanced →
        w.Acting → w.Taking → w.Dissipative → w.Transmitting → w.CountsObey Q) ∧
    ((∀ n c a, Tally n c a → Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Dependent → w.Acting →
        w.Taking → w.Dissipative → w.Embodied → w.Transmitting → w.CountsObey Q) :=
  have every : (∀ n c a, Tally n c a → Q n c a) →
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.CountsObey Q :=
    fun law _ _ _ census => law _ _ _ census.tally
  ⟨⟨every, fun law n c _ tally => pointwise (fun t => Queue.counts tally t)
      (law (queue n c) _ Queue.listed)⟩,
   ⟨fun law w _ _ _ _ _ _ _ => every law w, fun law n c _ tally =>
      match queue_premised n c with
      | ⟨dependent, balanced, acting, taking, dissipative, _, transmitting⟩ =>
        pointwise (fun t => Queue.counts tally t) (law (queue n c) dependent balanced acting
          taking dissipative transmitting _ Queue.listed)⟩,
   ⟨fun law w _ _ _ _ _ _ _ => every law w, fun law n c _ tally =>
      match embodiedQueue_premised n c with
      | ⟨dependent, acting, taking, dissipative, embodied, _, transmitting⟩ =>
        pointwise (fun t => Queue.counts tally t) (law (embodiedQueue n c) dependent acting
          taking dissipative embodied transmitting _ Queue.listed)⟩⟩

/-- Together, balance and embodiment bind the counts. Where the flow balances, only active
relata give and whatever arises is embodied, what arises is given by a relatum active at
the step (`Web.Embodied.arises_given`), so under a census nothing arises across a step at
which nothing is active. This is no law of tallies: one relatum arising from none is
counted by a queue meeting every premise but embodiment, and by one meeting every premise
but balance. -/
theorem counting_binds_jointly :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Balanced → w.Acting →
      w.ArisingEmbodied → w.CountsObey fun n _ a => ∀ t, 0 < a t → 0 < n t) ∧
    ¬ (queue Queue.lone fun _ => 0).CountsObey (fun n _ a => ∀ t, 0 < a t → 0 < n t) ∧
    ¬ (embodiedQueue Queue.lone fun _ => 0).CountsObey
      (fun n _ a => ∀ t, 0 < a t → 0 < n t) :=
  ⟨fun _ _ balanced acting embodied alive census t arising =>
    match total_pos _ arising with
    | ⟨x, _, comes⟩ => match Web.Embodied.arises_given balanced acting
        (embodied t x (mark_pos.mp comes)) (mark_pos.mp comes) with
      | ⟨f, active, _⟩ => Nat.lt_of_lt_of_le (total_pos_of_mem (((census t).2 f).mp active)
          Nat.zero_lt_one) (Nat.le_of_eq (total_ones (alive t))),
   fun obeys => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (obeys _ Queue.listed 0
      (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq
        (Queue.comings_eq Queue.lone_tally 0).symm)))
      (Nat.le_of_eq (Queue.counts Queue.lone_tally 0).1)),
   fun obeys => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (obeys _ Queue.listed 0
      (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq
        (Queue.comings_eq Queue.lone_tally 0).symm)))
      (Nat.le_of_eq (Queue.counts Queue.lone_tally 0).1))⟩


end World

/-! ## Counting under all the premises -/

namespace Tended

/-- The members of a queue, and ground relata. -/
inductive Relatum
  | member (k : Nat)
  | ground (k : Nat)

variable (n c : Nat → Nat)

/-- Members stand and are active exactly while in the queue; ground relata stand at nothing
and are never active. -/
def web : Web Relatum Relatum where
  level t x := match x with
    | .member k => mark (Queue.holds n c k t)
    | .ground _ => 0
  active t x := match x with
    | .member k => Queue.holds n c k t
    | .ground _ => False
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

/-- The front of the queue takes part at every step. It gives one unit to each member
joining and takes one from each member leaving; while active it also gives one unit to every
ground relatum and takes one from each. -/
def flow : Flow Relatum Relatum where
  present t := [.member (Queue.gone c t)]
  take t _ x := match x with
    | .member k => mark (CeasesToBe (Queue.holds n c k) t)
    | .ground _ => mark (Queue.holds n c (Queue.gone c t) t)
  give t _ x := match x with
    | .member k => mark (ComesToBe (Queue.holds n c k) t)
    | .ground _ => mark (Queue.holds n c (Queue.gone c t) t)

def index : Relatum → Nat
  | .member k => k
  | .ground k => k

/-- No finite family holds every ground relatum. -/
theorem outside (cs : List Relatum) : ¬ Relatum.ground (beyond (cs.map index)) ∈ cs :=
  fun mem => beyond_not_mem _ (mem_map_of (g := index) mem)

theorem member_inj : ∀ a b : Nat, Relatum.member a = Relatum.member b → a = b :=
  fun _ _ same => Relatum.noConfusion same id

theorem ground_not_member {g : Nat} : ∀ {l : List Nat}, ¬ Relatum.ground g ∈ l.map .member
  | [], no => nomatch no
  | _ :: _, .tail _ mem => ground_not_member mem

variable {n c}

/-- The front of the queue is in it exactly while the queue is not empty. -/
theorem front {t : Nat} : Queue.holds n c (Queue.gone c t) t ↔ 0 < n t :=
  ⟨fun holds => Nat.lt_of_add_lt_add_left (n := Queue.gone c t) (k := 0) holds.2,
   fun pos => ⟨Nat.le_refl _, Nat.lt_add_of_pos_right pos⟩⟩

/-- A member in the queue means the queue is not empty. -/
theorem occupied {k t : Nat} (holds : Queue.holds n c k t) : 0 < n t :=
  Nat.lt_of_add_lt_add_left (n := Queue.gone c t) (k := 0) (Nat.lt_of_le_of_lt holds.1 holds.2)

/-- Where something joins only across a step at which the queue is not empty, a member
joining means the queue was not empty. -/
theorem joined {a : Nat → Nat} (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    {k t : Nat} (comes : ComesToBe (Queue.holds n c k) t) : 0 < n t :=
  company t (Nat.lt_of_lt_of_le (total_pos_of_mem (q := fun j => mark (ComesToBe
    (Queue.holds n c j) t)) (steps_of_within comes.2.1 comes.2.2) (mark_pos.mpr comes))
    (Nat.le_of_eq (Queue.comings_eq tally t)))

end Tended

namespace World

/-- A queue tended by its front: the front gives to each relatum joining, takes from each
leaving, and while active exchanges one unit each way with every ground relatum. -/
def tendedQueue (n c : Nat → Nat) : World :=
  ⟨Tended.Relatum, Tended.flow n c, Tended.web n c⟩

instance tendedQueue_decided (n c : Nat → Nat) :
    ∀ t x, Decidable ((tendedQueue n c).web.active t x)
  | t, .member k => inferInstanceAs (Decidable (Queue.holds n c k t))
  | _, .ground _ => isFalse id

/-- The census of a tended queue is its members, listed as the queue lists them. -/
theorem tendedQueue_census (n c : Nat → Nat) :
    (tendedQueue n c).web.Census fun t => (Queue.line n c t).map .member :=
  fun _ => ⟨distinct_map Tended.member_inj (steps_distinct _ _), fun x => match x with
    | .member _ => ⟨fun holds => mem_map_of (steps_of_within holds.1 holds.2),
        fun mem => match mem_of_map Tended.member_inj mem with
          | listed => ⟨steps_mem listed, steps_within listed⟩⟩
    | .ground _ => ⟨False.elim, fun mem => Tended.ground_not_member mem⟩⟩

/-- Its census counts what the queue counts. -/
theorem tendedQueue_counts {n c a : Nat → Nat} (tally : Tally n c a) (t : Nat) :
    ((Queue.line n c t).map Tended.Relatum.member).length = n t ∧
      ceasings ((Queue.line n c t).map .member)
        (fun x s => (tendedQueue n c).web.active s x) t = c t ∧
      comings ((Queue.line n c (t + 1)).map .member)
        (fun x s => (tendedQueue n c).web.active s x) t = a t :=
  ⟨(total_ones _).symm.trans ((total_map _ _ _).trans ((total_ones _).trans (steps_length _ _))),
   (total_map Tended.Relatum.member _ (Queue.line n c t)).trans (Queue.ceasings_eq tally t),
   (total_map Tended.Relatum.member _ (Queue.line n c (t + 1))).trans
     (Queue.comings_eq tally t)⟩

/-- Where something arises only across a step at which something is active, a tended queue
meets all eight premises. Not all of them bind: no step at which the front is active is
enclosed, and nothing depends on anything (`tended_not_binds`). -/
theorem tendedQueue_premised {n c a : Nat → Nat} (tally : Tally n c a)
    (company : ∀ t, 0 < a t → 0 < n t) : (tendedQueue n c).Premised :=
  .of (fun _ _ _ _ no => (nomatch no))
    (fun t x => match x with
      | .member k => mark_turn (Queue.holds n c k t) (Queue.holds n c k (t + 1))
      | .ground _ => rfl)
    (fun _ f x present gives => match f, present, x, gives with
      | _, .head _, .member _, gives => Tended.front.mpr (Tended.joined tally company
          (mark_pos.mp gives))
      | _, .head _, .ground _, gives => mark_pos.mp gives
      | _, .tail _ no, _, _ => (nomatch no))
    (fun _ f x present takes => match f, present, x, takes with
      | _, .head _, .member _, takes => ⟨Tended.front.mpr (Tended.occupied
          (mark_pos.mp takes).1), trivial⟩
      | _, .head _, .ground _, takes => ⟨mark_pos.mp takes, trivial⟩
      | _, .tail _ no, _, _ => (nomatch no))
    (fun cs t _ closed _ _ => match Nat.eq_zero_or_pos (n t) with
      | .inr pos => absurd ((mark_one (Tended.front.mpr pos)).symm.trans
          (closed _ (.head _) _ (Tended.outside cs)).2) (fun no => Nat.noConfusion no)
      | .inl empty => gives_nothing ((total_congr_on (g := fun _ => 0) fun x _ => match x with
          | .member _ => mark_zero fun comes => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le
              (Tended.joined tally company comes) (Nat.le_of_eq empty))
          | .ground _ => mark_zero fun holds => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le
              (Tended.front.mp holds) (Nat.le_of_eq empty))).trans (total_zero cs)))
    (fun x => match x with
      | .member _ => fun _ => mark_pos.symm
      | .ground _ => fun _ => ⟨False.elim, fun no => absurd no (Nat.lt_irrefl 0)⟩)
    ⟨_, tendedQueue_census n c⟩
    ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩

/-- Under all eight premises the laws of counting are the tally and that nothing arises
across a step at which nothing is active: a property of the counts holds of every census of
every world meeting the eight exactly when it holds of every tally in which something arises
only across a step at which something is active. -/
theorem premised_counting {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop}
    (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.CountsObey Q :=
  ⟨fun law w _ premised alive census =>
    law _ _ _ census.tally (counting_binds_jointly.1 w (premised _ (.tail _ (.head _)))
      (premised _ (.tail _ (.tail _ (.head _))))
      (Embodied.arising (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _
        (.head _))))))))
      alive census),
   fun law n c _ tally company => pointwise (tendedQueue_counts tally)
      (law (tendedQueue n c) (tendedQueue_premised tally company) _
        (tendedQueue_census n c))⟩

/-- In a tended queue dissipation, activity needing support and bounded transmission hold
idly. Nothing taking part takes from a closed family: where something is taken the front is
active, and then it gives to a ground relatum beyond every finite family. Nothing depends on
anything. So not every premise binds there (the thirteenth review's probe). -/
theorem tended_not_binds {n c : Nat → Nat} :
    (¬ ∃ cs t f, Distinct cs ∧ (tendedQueue n c).flow.ClosedAt cs t ∧
      f ∈ (tendedQueue n c).flow.present t ∧ 0 < total cs ((tendedQueue n c).flow.take t f)) ∧
    (¬ ∃ t f x, (tendedQueue n c).web.active t f ∧ (tendedQueue n c).web.requires t f x ∧
      0 < (tendedQueue n c).web.need t f x) ∧
    (¬ ∃ t x g y, (tendedQueue n c).flow.DescendsAt (tendedQueue n c).web t x g ∧
      (tendedQueue n c).web.requires (t + 1) x y) ∧
    ¬ (tendedQueue n c).Binds :=
  have idle : ¬ ∃ cs t f, Distinct cs ∧ (tendedQueue n c).flow.ClosedAt cs t ∧
      f ∈ (tendedQueue n c).flow.present t ∧ 0 < total cs ((tendedQueue n c).flow.take t f) :=
    fun ⟨cs, t, f, _, closed, present, takes⟩ => match total_pos cs takes with
      | ⟨x, _, positive⟩ =>
        have occupied : 0 < n t := match x, positive with
          | .member _, positive => Tended.occupied (mark_pos.mp positive).1
          | .ground _, positive => Tended.front.mp (mark_pos.mp positive)
        Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq
          ((mark_one (Tended.front.mpr occupied)).symm.trans
            (closed f present _ (Tended.outside cs)).2)))
  ⟨idle, fun ⟨_, _, _, _, no, _⟩ => no, fun ⟨_, _, _, _, _, no⟩ => no,
   fun binds => idle binds.dissipative⟩

/-- Where every premise binds, every census counts something arising: embodiment binds only
where something arises (the thirteenth review's probe). -/
theorem binds_arising (w : World) [∀ t x, Decidable (w.web.active t x)] (binds : w.Binds) :
    w.CountsObey fun _ _ a => ∃ t, 0 < a t := fun _ census =>
  match binds.embodied with
  | ⟨t, x, arises⟩ =>
    ⟨t, Nat.lt_of_lt_of_le (mark_pos.mpr arises)
      (le_total_of_mem (q := fun y => mark (ComesToBe (fun s => w.web.active s y) t))
        (((census (t + 1)).2 x).mp arises.2))⟩

/-- Under the eight premises something arising is no law of counting, as the empty tally
shows; where every premise binds it is one (`binds_arising`). The laws of
`premised_counting` hold of worlds in which some premises hold idly (the thirteenth
review's probe). -/
theorem binds_adds :
    ¬ ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised →
      w.CountsObey fun _ _ a => ∃ t, 0 < a t :=
  fun law => match (premised_counting (Q := fun _ _ a => ∃ t, 0 < a t)
      (fun same ⟨t, pos⟩ => ⟨t, Nat.lt_of_lt_of_le pos (Nat.le_of_eq (same t).2.2)⟩)).mpr
      law (fun _ => 0) (fun _ => 0) (fun _ => 0) (fun _ => ⟨0, rfl, rfl⟩) (fun _ no => no) with
    | ⟨_, no⟩ => Nat.lt_irrefl 0 no

end World

end Becoming
