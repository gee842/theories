import Becoming.Dissipation

/-!
# Roles: formations and conditions are roles of one relatum

`Web` and `Flow` relate formations to conditions of another type. The split is a
reading, not two kinds of being: a formation can be a condition of others and of itself,
as parents are of their young, a forest of its understory and a flower of the bee. Read
with two kinds, that is representable only through a proxy condition, and nothing ties a
formation's activity to its standing as a condition. This module reads one kind of
relatum in both roles.

Results:
* The two-kind reading embeds in the one-kind reading as the one in which no formation
  is a condition (`Web.roles`, `Flow.roles`). Read so, a web keeps support,
  `Dependent`, renewal, consumption, the classes of formations, undermining, the living
  events of the stepwise reading, arising, unceasing generation and a census of the
  active formations. A flow keeps what is taken and given, balance, `Acting`, `Taking`,
  each formation taking part listed once, the takers and renewers of a family, more
  without end and dissipation (`Flow.roles_dissipative`). These are the readings listed
  here, not every reading stated. In this reading no active formation is embodied or
  bears on itself (`roles_not_embodied`, `roles_not_selfBearing`).
* Which condition is which relatum. A one-kind web `Web X X` is itself a two-kind web
  whose index types coincide. What the one-kind reading adds is that condition `x` and
  formation `x` are one relatum, and the shared index supplies that identification.
  Relabelling the condition side onto itself keeps `Dependent` and undermining
  (`relabel_dependent`, `relabel_undermining`), hence the living events and, in
  `Becoming.Correspondence`, the connection of both valuations; it changes which relata
  are embodied and which bear on themselves (`Mutualism.apart_relabelled`,
  `Wilting.relabelled_not_embodied`). Embodiment and bearing on oneself are readings
  under the identification, which the representation supplies as a correspondence
  premise and the two-kind readings do not check.
* A relatum is *embodied* when it stands as a condition exactly while it is active
  (`Embodied`). It *bears on itself* when, while active, it depends on its own standing
  at a positive need (`SelfBearing`); under `Dependent` it then stands while active
  (`SelfBearing.stands`), and if it is embodied its self-dependence is met exactly while
  it is active (`SelfBearing.met_iff`).
* Life as a condition of life. Under `Dependent`, a formation depending on an embodied
  relatum at a positive need is active only while that relatum is
  (`Embodied.active_of_bearing`). Activity passes along every chain of such dependence
  (`active_along`), so a relatum that is not active ends every formation whose chain
  reaches it (`coextinct`). Consuming an embodied relatum at a need of one ends it
  (`Embodied.ends_when_consumed`).
* Drawing at an ending. Drawing on an embodied relatum that bears on itself, across the
  step at which it ends, breaks its own dependence whether or not any other formation
  depends on it, so the drawing event is not living (`Embodied.ending_breaks`). This is
  co-occurrence with the ending, whatever ends it: a bee that takes nothing, drawing on
  a flower that wilts by its own taking, is not living at that step, and neither is the
  flower's own last event (`Wilting`). That the drawing ends the relatum would need a
  counterfactual relation, which is not stated here.
* Arising through another's giving. In a balanced flow in which only active formations
  give, an embodied relatum arises only as another active formation gives to it
  (`Embodied.arises_given`). The giver need not be embodied, bear on itself or depend on
  anything (`SunSeed`); where only embodied relata give, a premise the representation
  supplies, the giver is embodied too (`Embodied.arises_from_embodied`).
* Generation is replenishment. In a balanced flow an embodied relatum is given at least
  the standing it arises with (`Embodied.given_of_arises`), so its arising replenishes
  every family containing it (`Embodied.replenishes`). Where embodied members of a family
  arise at arbitrarily late steps, its replenishment recurs whatever is taken
  (`generation_needs_replenishment`): generation carries the requirement itself, not
  through the uptake it brings as in `Flow.uptake_needs_replenishment`.
* Generation under dissipation. Dissipated on, whatever gives to a family takes from it
  (`Flow.DissipatesOn.takes_of_gives`), so the arising of an embodied member of a closed
  family lowers the family's stock (`Embodied.arising_lowers`): the premise of
  `Web.dissipation_ceases`, supplied there as physical, here follows from balance,
  dissipation and embodiment. A finite family without repetition in which embodied
  members arise at arbitrarily late steps is not closed from any step on
  (`generation_opens`). If finitely many relata are all there is, embodied relata do not
  arise at arbitrarily late steps (`generation_ceases`).
* Witnesses. A bee and a flower, each depending on itself and on the other and drawing
  on the other, renew each other with no third condition, and every event is living
  (`Mutualism`); in `Mutualism.apart` each depends only on the other, and neither bears
  on itself. A fox depending on the hare it draws on ends with it, and its drawing
  across the step at which the hare ends breaks the hare's own dependence
  (`Predation`). Generation after generation arises, each given by the one before, with
  nothing else (`Brood`); giving without taking, the brood is not dissipative
  (`Brood.not_dissipative`).
* Each premise of `generation_ceases` is needed. Two sides handing one standing back and
  forth, each embodied, bear unceasing generation in a closed world of two relata
  without dissipation (`Handing`). Burning a fresh fuel at every step, they bear it under
  dissipation, and every finite family containing a side is open at arbitrarily late
  steps (`Kindling`). A relatum whose activity is not its standing arises again and
  again in a world of one relatum under dissipation (`Flicker`).

`Becoming.Correspondence` reads the relations: the one-kind reading keeps the connection
of the valuations, and formations bearing on themselves relate directly. Embodiment
itself does not enter either valuation (`Mutualism.apart_embodied`).

Which relata are embodied, and whether a formation bears on itself, are
representational choices: remains stand after activity ends, and a condition such as
water stands without being active. Generation carries a requirement of its own where
the arising relatum is embodied, and need not where it is not (`Flicker`), so that is
where the choice has consequences. `ending_breaks` counts drawing on a relatum that
bears on itself, at the step at which it ends, against living, whatever ends it;
whether it should, and for which drawers, belongs to the reading of 生生, which is
Ren's. Dissipation is the physical premise of `Becoming.Dissipation`. No ethical
predicate, ranking or axiom occurs.
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

theorem inl_injective : ∀ a b : F, (Sum.inl a : F ⊕ C) = Sum.inl b → a = b
  | _, _, rfl => rfl

theorem inr_injective : ∀ a b : C, (Sum.inr a : F ⊕ C) = Sum.inr b → a = b
  | _, _, rfl => rfl

/-- No condition is listed among formations. -/
theorem inr_not_mem {c : C} : ∀ {l : List F}, ¬ (Sum.inr c : F ⊕ C) ∈ l.map Sum.inl
  | [], mem => nomatch mem
  | _ :: l, mem => match mem_cons_cases mem with
    | .inr mem => inr_not_mem (l := l) mem

/-- The conditions listed in a family of relata. -/
def conditionsOf : List (F ⊕ C) → List C
  | [] => []
  | .inl _ :: l => conditionsOf l
  | .inr c :: l => c :: conditionsOf l

theorem mem_of_conditionsOf {c : C} : ∀ {l : List (F ⊕ C)}, c ∈ conditionsOf l → Sum.inr c ∈ l
  | .inl _ :: l, mem => .tail _ (mem_of_conditionsOf (l := l) mem)
  | .inr _ :: l, mem => match mem_cons_cases (q := conditionsOf l) mem with
    | .inl same =>
      Eq.subst (motive := fun z => (Sum.inr c : F ⊕ C) ∈ Sum.inr z :: l) same (.head _)
    | .inr mem => .tail _ (mem_of_conditionsOf (l := l) mem)

theorem conditionsOf_of_mem {c : C} : ∀ {l : List (F ⊕ C)}, Sum.inr c ∈ l → c ∈ conditionsOf l
  | .inl _ :: l, mem => match mem_cons_cases mem with
    | .inr mem => (conditionsOf_of_mem (l := l) mem : c ∈ conditionsOf l)
  | .inr d :: l, mem => match mem_cons_cases mem with
    | .inl rfl => (.head _ : c ∈ c :: conditionsOf l)
    | .inr mem => (.tail _ (conditionsOf_of_mem (l := l) mem) : c ∈ d :: conditionsOf l)

theorem distinct_conditionsOf : ∀ {l : List (F ⊕ C)}, Distinct l → Distinct (conditionsOf l)
  | [], _ => trivial
  | .inl _ :: l, ⟨_, distinct⟩ =>
    (distinct_conditionsOf (l := l) distinct : Distinct (conditionsOf l))
  | .inr _ :: l, ⟨fresh, distinct⟩ =>
    ⟨fun mem => fresh (mem_of_conditionsOf (l := l) mem), distinct_conditionsOf (l := l) distinct⟩

/-- A quantity that is zero on formations totals over a family of relata what it totals
over the family's conditions. -/
theorem total_conditionsOf {p : F ⊕ C → Nat} {q : C → Nat} (zero : ∀ f, p (.inl f) = 0)
    (same : ∀ c, p (.inr c) = q c) : ∀ l : List (F ⊕ C), total l p = total (conditionsOf l) q
  | [] => rfl
  | .inl f :: l => (congrArg (· + total l p) (zero f)).trans
      ((Nat.zero_add _).trans (total_conditionsOf zero same l))
  | .inr c :: l => congr (congrArg (· + ·) (same c)) (total_conditionsOf zero same l)

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

/-- A census of the active formations is a census of the active relata. -/
theorem roles_census {alive : Nat → List F} (census : W.Census alive) :
    W.roles.Census fun t => (alive t).map Sum.inl :=
  fun t => ⟨distinct_map inl_injective (census t).1, fun x => match x with
    | .inl f => ⟨fun active => mem_map_of (g := Sum.inl) (((census t).2 f).mp active),
        fun mem => ((census t).2 f).mpr (mem_of_map inl_injective mem)⟩
    | .inr _ => ⟨False.elim, fun mem => absurd mem inr_not_mem⟩⟩

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

theorem roles_acting {W : Web F C} : L.roles.Acting W.roles ↔ L.Acting W :=
  ⟨fun acting t f c mem gives =>
    acting t (.inl f) (.inr c) (mem_map_of (g := Sum.inl) mem) gives,
   fun acting t x y mem gives => match x, y, mem, gives with
    | .inl f, .inr c, mem, gives => acting t f c (mem_of_map inl_injective mem) gives
    | .inl _, .inl _, _, gives => absurd gives (Nat.lt_irrefl 0)
    | .inr _, _, _, gives => absurd gives (Nat.lt_irrefl 0)⟩

theorem roles_taking {W : Web F C} : L.roles.Taking W.roles ↔ L.Taking W :=
  ⟨fun taking t f c mem takes =>
    taking t (.inl f) (.inr c) (mem_map_of (g := Sum.inl) mem) takes,
   fun taking t x y mem takes => match x, y, mem, takes with
    | .inl f, .inr c, mem, takes => taking t f c (mem_of_map inl_injective mem) takes
    | .inl _, .inl _, _, takes => absurd takes (Nat.lt_irrefl 0)
    | .inr _, _, _, takes => absurd takes (Nat.lt_irrefl 0)⟩

theorem roles_distinct {t : Nat} (distinct : Distinct (L.present t)) :
    Distinct (L.roles.present t) :=
  distinct_map inl_injective distinct

/-- Dissipation reads the same with one kind of relatum. -/
theorem roles_dissipative : L.roles.Dissipative ↔ L.Dissipative :=
  ⟨fun dissipative ds t distinct closed f present =>
    have closed' : L.roles.ClosedAt (ds.map .inr) t := fun x mem y outside =>
      match x, y, mem with
      | .inl g, .inr c, mem => closed g (mem_of_map inl_injective mem) c
          fun inside => outside (mem_map_of inside)
      | .inl _, .inl _, _ => ⟨rfl, rfl⟩
      | .inr _, _, _ => ⟨rfl, rfl⟩
    have dissipates := dissipative (ds.map .inr) t (distinct_map inr_injective distinct) closed'
      (.inl f) (mem_map_of present)
    have gives := total_map Sum.inr (L.roles.give t (.inl f)) ds
    have takes := total_map Sum.inr (L.roles.take t (.inl f)) ds
    Nat.le_trans (Nat.le_of_eq (congr (congrArg (· + ·) gives) (congrArg sign takes)).symm)
      (Nat.le_trans dissipates (Nat.le_of_eq takes)),
   fun dissipative ds t distinct closed x mem => match x, mem with
    | .inr _, mem => absurd mem inr_not_mem
    | .inl f, mem =>
      have closed' : L.ClosedAt (conditionsOf ds) t := fun g present c outside =>
        closed (.inl g) (mem_map_of (g := Sum.inl) present) (.inr c)
          fun inside => outside (conditionsOf_of_mem inside)
      have dissipates := dissipative (conditionsOf ds) t (distinct_conditionsOf distinct)
        closed' f (mem_of_map inl_injective mem)
      have gives := total_conditionsOf (p := L.roles.give t (.inl f)) (q := L.give t f)
        (fun _ => rfl) (fun _ => rfl) ds
      have takes := total_conditionsOf (p := L.roles.take t (.inl f)) (q := L.take t f)
        (fun _ => rfl) (fun _ => rfl) ds
      Nat.le_trans (Nat.le_of_eq (congr (congrArg (· + ·) gives) (congrArg sign takes)))
        (Nat.le_trans dissipates (Nat.le_of_eq takes.symm))⟩

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

/-- Under `Dependent`, the self-dependence of an embodied relatum is met exactly while the
relatum is active: it records nothing beyond the activity. -/
theorem SelfBearing.met_iff (dependent : W.Dependent) {x : X} (embodied : W.Embodied x)
    (self : W.SelfBearing x) (t : Nat) :
    (W.requires t x x ∧ 0 < W.need t x x ∧ W.need t x x ≤ W.level t x) ↔ W.active t x :=
  ⟨fun ⟨_, positive, met⟩ => (embodied t).mpr (Nat.lt_of_lt_of_le positive met),
   fun active => ⟨(self t active).1, (self t active).2,
     dependent t x active x (self t active).1⟩⟩

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
step at which it ends, breaks its own dependence, whatever ends it; no other formation
need depend on it. -/
theorem Embodied.ending_breaks (dependent : W.Dependent) {x : X} (embodied : W.Embodied x)
    (self : W.SelfBearing x) {t : Nat} (active : W.active t x) (ends : ¬ W.active (t + 1) x)
    {f : X} (drawn : W.draws t f x) : W.BreakingOn t f x :=
  ⟨drawn, x, (self t active).1, dependent t x active x (self t active).1,
    Nat.lt_of_le_of_lt (Nat.ge_of_not_lt fun stands => ends ((embodied (t + 1)).mpr stands))
      (self t active).2⟩

/-- Arising through another's giving: in a balanced flow in which only active formations
give, an embodied relatum arises only as an active formation taking part gives to it, and
that formation is another. -/
theorem Embodied.arises_given {L : Flow X X} (balances : L.Balances W) (acting : L.Acting W)
    {x : X} (embodied : W.Embodied x) {t : Nat} (arises : W.Arises t x) :
    ∃ f, W.active t f ∧ f ∈ L.present t ∧ 0 < L.give t f x ∧ f ≠ x :=
  match balances.renewedBy acting t x (Nat.lt_of_le_of_lt
      (Nat.ge_of_not_lt fun stands => arises.1 ((embodied t).mpr stands))
      ((embodied (t + 1)).mp arises.2)) with
  | ⟨f, active, present, gives⟩ => ⟨f, active, present, gives, fun same => arises.1 (same ▸ active)⟩

/-- Where only embodied relata give, a premise supplied by the representation, the giver
of an arising embodied relatum is embodied too, and stands as a condition while it
gives. -/
theorem Embodied.arises_from_embodied {L : Flow X X} (balances : L.Balances W)
    (acting : L.Acting W) (givers : ∀ t f c, f ∈ L.present t → 0 < L.give t f c → W.Embodied f)
    {x : X} (embodied : W.Embodied x) {t : Nat} (arises : W.Arises t x) :
    ∃ f, W.Embodied f ∧ 0 < W.level t f ∧ f ∈ L.present t ∧ 0 < L.give t f x ∧ f ≠ x :=
  match embodied.arises_given balances acting arises with
  | ⟨f, active, present, gives, other⟩ =>
    have bodied := givers t f x present gives
    ⟨f, bodied, (bodied t).mp active, present, gives, other⟩

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

/-! ## Which condition is which relatum -/

namespace Web

/-- The same web with its condition side relabelled by `π`: condition `y` is what
condition `π y` was, and the formations are unchanged. -/
def relabel (W : Web X X) (π : X → X) : Web X X where
  level t y := W.level t (π y)
  active := W.active
  requires t g y := W.requires t g (π y)
  need t g y := W.need t g (π y)
  draws t g y := W.draws t g (π y)

variable {W : Web X X} {π : X → X}

/-- What holds of some condition holds of one as relabelled onto the conditions. -/
theorem exists_of_onto (onto : ∀ c, ∃ y, π y = c) {p : X → Prop} : (∃ c, p c) → ∃ y, p (π y)
  | ⟨c, holds⟩ => match onto c with
    | ⟨y, same⟩ => ⟨y, Eq.subst (motive := p) same.symm holds⟩

/-- Relabelling the conditions onto them keeps whether activity needs support. -/
theorem relabel_dependent (onto : ∀ c, ∃ y, π y = c) : (W.relabel π).Dependent ↔ W.Dependent :=
  ⟨fun dependent t f active c depends => match onto c with
    | ⟨y, same⟩ => Eq.subst (motive := fun z => W.need t f z ≤ W.level t z) same
        (dependent t f active y (Eq.subst (motive := fun z => W.requires t f z) same.symm depends)),
   fun dependent t f active y depends => dependent t f active (π y) depends⟩

/-- Relabelling the conditions onto them keeps undermining, so the living events of the
stepwise reading. -/
theorem relabel_undermining (onto : ∀ c, ∃ y, π y = c) (t : Nat) (f : X) :
    (W.relabel π).UnderminingAt t f ↔ W.UnderminingAt t f :=
  ⟨fun ⟨y, undermining⟩ => ⟨π y, undermining⟩, exists_of_onto onto⟩

theorem relabel_alive (onto : ∀ c, ∃ y, π y = c) (t : Nat) (f : X) :
    ((W.relabel π).active t f ∧ ¬ (W.relabel π).UnderminingAt t f) ↔
      (W.active t f ∧ ¬ W.UnderminingAt t f) :=
  ⟨fun ⟨active, sound⟩ => ⟨active, fun u => sound ((relabel_undermining onto t f).mpr u)⟩,
   fun ⟨active, sound⟩ => ⟨active, fun u => sound ((relabel_undermining onto t f).mp u)⟩⟩

end Web

/-! ## Generation is replenishment -/

namespace Web

variable {W : Web X X} {L : Flow X X}

/-- In a balanced flow, an embodied relatum is given at least the standing it arises
with: its arising is a rise of its standing. -/
theorem Embodied.given_of_arises (balances : L.Balances W) {x : X} (embodied : W.Embodied x)
    {t : Nat} (arises : W.Arises t x) : W.level (t + 1) x ≤ L.given t x :=
  Nat.le_trans (Nat.le_add_right _ (L.taken t x)) (Nat.le_of_eq ((balances t x).trans
    ((congrArg (· + L.given t x) (eq_zero_of_not_pos fun stands =>
      arises.1 ((embodied t).mpr stands))).trans (Nat.zero_add _))))

/-- So the arising of an embodied member of a family replenishes the family. -/
theorem Embodied.replenishes (balances : L.Balances W) {x : X} (embodied : W.Embodied x)
    {cs : List X} (mem : x ∈ cs) {t : Nat} (arises : W.Arises t x) :
    0 < L.replenishment cs t :=
  total_pos_of_mem mem (Nat.lt_of_lt_of_le ((embodied (t + 1)).mp arises.2)
    (embodied.given_of_arises balances arises))

/-- Generation carries the requirement itself: where embodied members of a family arise at
arbitrarily late steps, replenishment of the family recurs, whatever is taken. -/
theorem generation_needs_replenishment (balances : L.Balances W) {cs : List X}
    (arising : ∀ N, ∃ t x, N ≤ t ∧ x ∈ cs ∧ W.Embodied x ∧ W.Arises t x) (T : Nat) :
    ¬ ∀ t, T ≤ t → L.replenishment cs t = 0 :=
  fun none => match arising T with
  | ⟨t, _, later, mem, embodied, arises⟩ => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le
      (embodied.replenishes balances mem arises) (Nat.le_of_eq (none t later)))

/-- Under dissipation, the arising of an embodied member of a family closed across the
step lowers the family's stock: whatever gives to it takes more from the family. -/
theorem Embodied.arising_lowers (balances : L.Balances W) (dissipative : L.Dissipative)
    {ds : List X} (distinct : Distinct ds) {t : Nat} (closed : L.ClosedAt ds t) {x : X}
    (embodied : W.Embodied x) (mem : x ∈ ds) (arises : W.Arises t x) :
    W.stock ds (t + 1) < W.stock ds t :=
  have dissipates := dissipative ds t distinct closed
  match total_pos (L.present t) (Nat.lt_of_lt_of_le ((embodied (t + 1)).mp arises.2)
      (embodied.given_of_arises balances arises)) with
  | ⟨_, present, gives⟩ => Nat.lt_of_lt_of_le
      (Nat.lt_add_of_pos_right (total_pos_of_mem (q := fun f => sign (total ds (L.take t f)))
        present (sign_pos (dissipates.takes_of_gives present (total_pos_of_mem mem gives)))))
      (balances.runs_down dissipates)

/-- Under dissipation, a finite family without repetition in which embodied members arise
at arbitrarily late steps is not closed from any step on: generation in it needs exchange
beyond it. -/
theorem generation_opens (balances : L.Balances W) (dissipative : L.Dissipative)
    {ds : List X} (distinct : Distinct ds)
    (arising : ∀ N, ∃ t x, N ≤ t ∧ x ∈ ds ∧ W.Embodied x ∧ W.Arises t x) (T : Nat) :
    ¬ ∀ t, T ≤ t → L.ClosedAt ds t :=
  fun closed => falls_finitely (W.stock ds) T
    (fun t later => Nat.le_trans (Nat.le_add_right _ _)
      (balances.runs_down (dissipative ds t distinct (closed t later))))
    fun N => match arising (N + T) with
    | ⟨t, _, later, mem, embodied, arises⟩ => ⟨t, Nat.le_trans (Nat.le_add_right N T) later,
        embodied.arising_lowers balances dissipative distinct
          (closed t (Nat.le_trans (Nat.le_add_left T N) later)) mem arises⟩

/-- If finitely many relata are all there is, embodied relata do not arise at arbitrarily
late steps under dissipation. -/
theorem generation_ceases (balances : L.Balances W) (dissipative : L.Dissipative)
    {all : List X} (distinct : Distinct all) (every : ∀ x, x ∈ all) :
    ¬ ∀ N, ∃ t x, N ≤ t ∧ W.Embodied x ∧ W.Arises t x :=
  fun arising => generation_opens balances dissipative distinct
    (fun N => match arising N with
      | ⟨t, x, later, embodied, arises⟩ => ⟨t, x, later, every x, embodied, arises⟩) 0
    fun _ _ _ _ c outside => absurd (every c) outside

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

theorem other_twice : ∀ x : Relatum, other (other x) = x
  | .bee => rfl
  | .flower => rfl

/-- Relabelled by `other`, `apart` is a web in which each relatum bears on itself, while
`Dependent` is unchanged: which condition is which relatum is not seen by `Dependent`. -/
theorem apart_relabelled :
    (∀ x, ¬ apart.SelfBearing x) ∧ (∀ x, (apart.relabel other).SelfBearing x) ∧
    ((apart.relabel other).Dependent ↔ apart.Dependent) :=
  ⟨apart_not_selfBearing, fun _ _ _ => ⟨rfl, Nat.zero_lt_one⟩,
   Web.relabel_dependent fun c => ⟨other c, other_twice c⟩⟩

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

/-- The fox's drawing across the step at which the hare ends breaks the hare's own
dependence, so it is not living. -/
theorem breaking : web.BreakingOn 2 .fox .hare :=
  (embodied .hare).ending_breaks (t := 2) dependent (selfBearing .hare) Nat.zero_lt_one
    (hare_ends 3 (Nat.lt_succ_self 2)) ⟨rfl, rfl⟩

/-- The fox depends on the hare, so it ends with it. -/
theorem fox_ends : ∀ t, 2 < t → ¬ web.active t .fox :=
  fun t later => Web.coextinct dependent
    (Reach.of_step (a := ()) ⟨⟨.inr rfl, Nat.zero_lt_one⟩, embodied .hare⟩) (hare_ends t later)

end Predation

namespace Wilting

inductive Relatum where
  | bee
  | flower

/-- One unit at step two: the flower's own taking as it wilts. -/
def fade : Nat → Nat
  | 0 => 0
  | 1 => 0
  | 2 => 1
  | _ + 3 => 0

/-- The bee stands at one throughout; the flower stands while unwilted, on the schedule
`Predation.uneaten`. The flower depends on itself at need one and draws on itself; the bee
draws on the flower and depends on nothing. -/
def web : Web Relatum Relatum where
  level t x := match x with
    | .bee => 1
    | .flower => Predation.uneaten t
  active t x := match x with
    | .bee => True
    | .flower => 0 < Predation.uneaten t
  requires _ x y := match x, y with
    | .flower, .flower => True
    | .flower, .bee => False
    | .bee, _ => False
  need _ _ _ := 1
  draws _ x y := match x, y with
    | .bee, .flower => True
    | .flower, .flower => True
    | .bee, .bee => False
    | .flower, .bee => False

/-- Only the flower takes, one unit from itself across step two; the bee takes
nothing. -/
def flow : Flow Relatum Relatum where
  present _ := [.bee, .flower]
  take t x y := match x, y with
    | .flower, .flower => fade t
    | .flower, .bee => 0
    | .bee, _ => 0
  give _ _ _ := 0

theorem fade_active : ∀ t, 0 < fade t → 0 < Predation.uneaten t
  | 0, h => absurd h (Nat.lt_irrefl 0)
  | 1, h => absurd h (Nat.lt_irrefl 0)
  | 2, _ => Nat.zero_lt_one
  | _ + 3, h => absurd h (Nat.lt_irrefl 0)

theorem embodied : web.Embodied .flower := fun _ => Iff.rfl

theorem selfBearing : web.SelfBearing .flower := fun _ _ => ⟨trivial, Nat.zero_lt_one⟩

theorem dependent : web.Dependent := fun _ x active y depends => match x, y, active, depends with
  | .flower, .flower, active, _ => active
  | .flower, .bee, _, h => (nomatch h)
  | .bee, _, _, h => (nomatch h)

theorem ends : ¬ web.active 3 .flower := Nat.lt_irrefl 0

/-- The flow balances, only active relata take, from what they draw on, and activity needs
support. The flower is embodied, bears on itself and wilts across step two by its own
taking; the bee takes nothing, ever. Still, by `ending_breaks`, the bee's drawing at step
two breaks the flower's dependence and is undermining, and so is the flower's own last
event. -/
theorem wilting :
    flow.Balances web ∧ flow.Acting web ∧ flow.Taking web ∧ web.Dependent ∧
    web.Embodied .flower ∧ web.SelfBearing .flower ∧
    (∀ t c, flow.take t .bee c = 0) ∧ (∀ t f, 0 < flow.take t f .flower → f = .flower) ∧
    web.BreakingOn 2 .bee .flower ∧ web.UnderminingAt 2 .bee ∧ web.UnderminingAt 2 .flower :=
  have bee := embodied.ending_breaks (t := 2) dependent selfBearing Nat.zero_lt_one ends
    (f := .bee) trivial
  have own := embodied.ending_breaks (t := 2) dependent selfBearing Nat.zero_lt_one ends
    (f := .flower) trivial
  ⟨fun t c => match c, t with
    | .bee, _ => rfl
    | .flower, 0 => rfl
    | .flower, 1 => rfl
    | .flower, 2 => rfl
    | .flower, _ + 3 => rfl,
   fun _ _ _ _ gives => absurd gives (Nat.lt_irrefl 0),
   fun t f c _ takes => match f, c, takes with
    | .flower, .flower, takes => ⟨fade_active t takes, trivial⟩
    | .flower, .bee, takes => absurd takes (Nat.lt_irrefl 0)
    | .bee, .bee, takes => absurd takes (Nat.lt_irrefl 0)
    | .bee, .flower, takes => absurd takes (Nat.lt_irrefl 0),
   dependent, embodied, selfBearing,
   fun _ c => match c with
    | .bee => rfl
    | .flower => rfl,
   fun _ f takes => match f, takes with
    | .flower, _ => rfl
    | .bee, takes => absurd takes (Nat.lt_irrefl 0),
   bee, ⟨.flower, bee.undermining⟩, ⟨.flower, own.undermining⟩⟩

/-- Exchanging the bee and the flower. -/
def swap : Relatum → Relatum
  | .bee => .flower
  | .flower => .bee

/-- Relabelled by `swap`, the wilting flower is not embodied. -/
theorem relabelled_not_embodied :
    web.Embodied .flower ∧ ¬ (web.relabel swap).Embodied .flower :=
  ⟨embodied, fun embodied' => Nat.lt_irrefl 0 ((embodied' 3).mpr Nat.zero_lt_one)⟩

end Wilting

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

/-- Giving without taking, the brood is not dissipative: generation one is given by
generation zero, which takes nothing. -/
theorem not_dissipative : ¬ flow.Dissipative :=
  fun dissipative => Nat.not_succ_le_zero 0 (dissipative [1] 0 ⟨fun no => (nomatch no), trivial⟩
    (fun f present c outside => match f, present, c with
      | _, _, 0 => ⟨rfl, rfl⟩
      | _, _, 1 => absurd (.head []) outside
      | _, _, _ + 2 => ⟨rfl, rfl⟩) 0 (.head []))

end Brood

namespace SunSeed

inductive Relatum where
  | sun
  | seed

/-- Zero at step zero, one after. -/
def sprout : Nat → Nat
  | 0 => 0
  | _ + 1 => 1

/-- The sun is always active and stands at zero as a condition; the seed stands, and is
active, from step one. Nothing depends on or draws on anything. -/
def web : Web Relatum Relatum where
  level t x := match x with
    | .sun => 0
    | .seed => sprout t
  active t x := match x with
    | .sun => True
    | .seed => 0 < sprout t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- The sun gives the seed one unit across step zero. -/
def flow : Flow Relatum Relatum where
  present _ := [.sun]
  take _ _ _ := 0
  give t x y := match x, y with
    | .sun, .seed => Brood.first t
    | .sun, .sun => 0
    | .seed, _ => 0

/-- The flow balances and only active relata give; the seed is embodied and arises across
step zero, given by the sun alone. The sun is not embodied, does not bear on itself and
depends on nothing: the giver `arises_given` names need not be a life. -/
theorem sun_gives :
    flow.Balances web ∧ flow.Acting web ∧ web.Embodied .seed ∧ web.Arises 0 .seed ∧
    (∀ f, web.active 0 f ∧ f ∈ flow.present 0 ∧ 0 < flow.give 0 f .seed ∧ f ≠ .seed →
      f = .sun) ∧
    ¬ web.Embodied .sun ∧ ¬ web.SelfBearing .sun ∧ ∀ t c, ¬ web.requires t .sun c :=
  ⟨fun t c => match c, t with
    | .sun, _ => rfl
    | .seed, 0 => rfl
    | .seed, _ + 1 => rfl,
   fun _ f _ mem _ => match f, mem with
    | .sun, _ => trivial
    | .seed, .tail _ mem => (nomatch mem),
   fun _ => Iff.rfl,
   ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩,
   fun f ⟨_, mem, _, _⟩ => match f, mem with
    | .sun, _ => rfl
    | .seed, .tail _ mem => (nomatch mem),
   fun embodied => Nat.lt_irrefl 0 ((embodied 0).mp trivial),
   fun self => (self 0 trivial).1,
   fun _ _ h => h⟩

end SunSeed

namespace Handing

/-- One at even steps, zero at odd steps. -/
def even : Nat → Nat
  | 0 => 1
  | 1 => 0
  | n + 2 => even n

/-- The side holding the standing at step `t`: `true` at even steps. -/
def holder : Nat → Bool
  | 0 => true
  | 1 => false
  | n + 2 => holder n

/-- `true` stands at even steps and `false` at odd steps. -/
def stands : Bool → Nat → Nat
  | true, t => even t
  | false, t => even (t + 1)

/-- Across each step the holder takes its own unit and gives it to the other side. -/
def flow : Flow Bool Bool where
  present t := [holder t]
  take _ x y := match x, y with
    | true, true => 1
    | false, false => 1
    | true, false => 0
    | false, true => 0
  give _ x y := match x, y with
    | true, true => 0
    | false, false => 0
    | true, false => 1
    | false, true => 1

/-- Each side is active while it stands and depends on itself at need one. -/
def web : Web Bool Bool where
  level t x := stands x t
  active t x := 0 < stands x t
  requires _ x y := y = x
  need _ _ _ := 1
  draws _ _ _ := False

theorem every : ∀ x : Bool, x ∈ [true, false]
  | true => .head _
  | false => .tail _ (.head _)

theorem distinct : Distinct [true, false] :=
  ⟨fun mem => match mem with | .tail _ no => (nomatch no), fun no => (nomatch no), trivial⟩

theorem stands_two : ∀ x t, stands x (t + 2) = stands x t
  | true, _ => rfl
  | false, _ => rfl

theorem holder_stands : ∀ t, 0 < stands (holder t) t
  | 0 => Nat.zero_lt_one
  | 1 => Nat.zero_lt_one
  | t + 2 => Nat.lt_of_lt_of_le (holder_stands t) (Nat.le_of_eq (stands_two (holder t) t).symm)

theorem balances : flow.Balances web
  | 0, true => rfl
  | 0, false => rfl
  | 1, true => rfl
  | 1, false => rfl
  | t + 2, true => balances t true
  | t + 2, false => balances t false

theorem acting : flow.Acting web :=
  fun t f _ present _ => match f, (present : f ∈ [holder t]) with
  | _, .head _ => holder_stands t
  | _, .tail _ no => (nomatch no)

theorem dependent : web.Dependent :=
  fun _ _ active _ same => match same with
  | rfl => active

theorem embodied (x : Bool) : web.Embodied x ∧ web.SelfBearing x :=
  ⟨fun _ => Iff.rfl, fun _ _ => ⟨rfl, Nat.zero_lt_one⟩⟩

/-- Each side arises at a step or the next. -/
theorem arises : ∀ t x, web.Arises t x ∨ web.Arises (t + 1) x
  | 0, true => .inr ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩
  | 0, false => .inl ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩
  | 1, true => .inl ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩
  | 1, false => .inr ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩
  | t + 2, true => arises t true
  | t + 2, false => arises t false

/-- Each side arises at arbitrarily late steps. -/
theorem recurs (x : Bool) (N : Nat) : ∃ t, N ≤ t ∧ web.Arises t x :=
  match arises N x with
  | .inl now => ⟨N, Nat.le_refl N, now⟩
  | .inr next => ⟨N + 1, Nat.le_succ N, next⟩

/-- Two sides hand one standing back and forth: finitely many relata are all there is,
the flow balances, only active sides give, each side is embodied and bears on itself,
activity needs support, the family of both is closed at every step, and generation is
unceasing. Only dissipation fails: the holder gives back all it takes. -/
theorem handing : flow.Balances web ∧ flow.Acting web ∧ web.Dependent ∧
    (∀ x, web.Embodied x ∧ web.SelfBearing x) ∧ (∀ t, flow.ClosedAt [true, false] t) ∧
    web.Unceasing ∧ ¬ flow.Dissipative :=
  ⟨balances, acting, dependent, embodied,
   fun _ _ _ c outside => absurd (every c) outside,
   fun N => match recurs true N with
    | ⟨t, later, arises⟩ => ⟨t, true, later, arises⟩,
   fun dissipative => Nat.not_succ_le_self 1 (dissipative [true, false] 0 distinct
     (fun _ _ c outside => absurd (every c) outside) true (.head _))⟩

end Handing

namespace Kindling

/-- The two sides of `Handing`, and fuels, one for each step. -/
inductive Relatum where
  | side (x : Bool)
  | fuel (n : Nat)

/-- As in `Handing`, and across the step from `t` the holder also burns two units of the
`t`th fuel. -/
def flow : Flow Relatum Relatum where
  present t := [.side (Handing.holder t)]
  take t f c := match f, c with
    | .side x, .side y => Handing.flow.take t x y
    | .side _, .fuel n => 2 * Frontier.burning n t
    | .fuel _, _ => 0
  give t f c := match f, c with
    | .side x, .side y => Handing.flow.give t x y
    | .side _, .fuel _ => 0
    | .fuel _, _ => 0

/-- The sides as in `Handing`; the `n`th fuel holds two units until it burns and is never
active. -/
def web : Web Relatum Relatum where
  level t c := match c with
    | .side x => Handing.stands x t
    | .fuel n => 2 * Frontier.unburnt n t
  active t c := match c with
    | .side x => 0 < Handing.stands x t
    | .fuel _ => False
  requires _ c d := match c with
    | .side _ => d = c
    | .fuel _ => False
  need _ _ _ := 1
  draws _ _ _ := False

theorem balances : flow.Balances web
  | t, .side y => Handing.balances t y
  | t, .fuel n => show 2 * Frontier.unburnt n (t + 1) + (2 * Frontier.burning n t + 0) =
        2 * Frontier.unburnt n t + (0 + 0) from
      (Nat.left_distrib 2 _ _).symm.trans (congrArg (2 * ·) (Frontier.burns n t))

theorem acting : flow.Acting web :=
  fun t f _ present _ => match f, (present : f ∈ [.side (Handing.holder t)]) with
  | _, .head _ => Handing.holder_stands t
  | _, .tail _ no => (nomatch no)

theorem dependent : web.Dependent :=
  fun _ c active d depends => match c, d, depends with
  | .side _, _, rfl => active

/-- The holder gives a family at most one unit: a positive gift goes to the other side. -/
theorem gives_other : ∀ (t : Nat) (x : Bool) (c : Relatum),
    0 < flow.give t (.side x) c → c = .side (!x)
  | _, true, .side false, _ => rfl
  | _, false, .side true, _ => rfl
  | _, true, .side true, given => absurd given (Nat.lt_irrefl 0)
  | _, false, .side false, given => absurd given (Nat.lt_irrefl 0)
  | _, _, .fuel _, given => absurd given (Nat.lt_irrefl 0)

theorem gives_one : ∀ (t : Nat) (x : Bool), flow.give t (.side x) (.side (!x)) ≤ 1
  | _, true => Nat.le_refl 1
  | _, false => Nat.le_refl 1

/-- A side taking part dissipates on every family without repetition closed across the
step: it gives at most one unit and burns two. -/
theorem side_dissipates {ds : List Relatum} {t : Nat} (distinct : Distinct ds)
    (closed : flow.ClosedAt ds t) {x : Bool} (present : Relatum.side x ∈ flow.present t) :
    total ds (flow.give t (.side x)) + sign (total ds (flow.take t (.side x))) ≤
      total ds (flow.take t (.side x)) :=
  have gives : total ds (flow.give t (.side x)) ≤ 1 :=
    Nat.le_trans (total_le_at (gives_other t x) distinct) (gives_one t x)
  have burnt : flow.take t (.side x) (.fuel t) = 2 :=
    congrArg (2 * ·) (Frontier.burning_self t)
  match Nat.decLe (total ds (flow.give t (.side x)) + sign (total ds (flow.take t (.side x))))
      (total ds (flow.take t (.side x))) with
  | isTrue le => le
  | isFalse not => absurd (fun inside : Relatum.fuel t ∈ ds => not
      (Nat.le_trans (Nat.add_le_add gives (sign_le_one _))
        (Nat.le_trans (Nat.le_of_eq burnt.symm) (le_total_of_mem inside))))
      fun outside => Nat.noConfusion (burnt.symm.trans (closed _ present _ outside).1)

/-- Every family without repetition closed across a step is dissipated on. -/
theorem dissipative : flow.Dissipative
  | _, t, distinct, closed, f, present =>
    match f, (present : f ∈ [.side (Handing.holder t)]) with
    | _, .tail _ no => (nomatch no)
    | _, .head _ => side_dissipates distinct closed (.head _)

/-- The handing of `Handing`, burning a fresh fuel at every step: the flow balances, only
active sides give, the sides are embodied and bear on themselves, activity needs support,
the flow is dissipative, and each side arises at arbitrarily late steps. -/
theorem kindling : flow.Balances web ∧ flow.Acting web ∧ web.Dependent ∧
    (∀ x, web.Embodied (.side x) ∧ web.SelfBearing (.side x)) ∧ flow.Dissipative ∧
    ∀ x N, ∃ t, N ≤ t ∧ web.Arises t (.side x) :=
  ⟨balances, acting, dependent,
   fun _ => ⟨fun _ => Iff.rfl, fun _ _ => ⟨rfl, Nat.zero_lt_one⟩⟩, dissipative,
   Handing.recurs⟩

/-- So every finite family without repetition containing a side is open at arbitrarily
late steps: the fuels burnt are not contained in any finite family. -/
theorem frontier {ds : List Relatum} (distinct : Distinct ds) {x : Bool}
    (side : Relatum.side x ∈ ds) (T : Nat) : ¬ ∀ t, T ≤ t → flow.ClosedAt ds t :=
  Web.generation_opens balances dissipative distinct (fun N => match Handing.recurs x N with
    | ⟨t, later, arises⟩ => ⟨t, .side x, later, side, fun _ => Iff.rfl, arises⟩) T

end Kindling

namespace Flicker

/-- One relatum, active at odd steps and never standing as a condition. -/
def web : Web Unit Unit where
  level _ _ := 0
  active t _ := 0 < Handing.stands false t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- Nothing takes part. -/
def flow : Flow Unit Unit := ⟨fun _ => [], fun _ _ _ => 0, fun _ _ _ => 0⟩

/-- A relatum whose activity is not its standing arises with nothing given to it: one
relatum is all there is, the flow balances and is dissipative, and generation is
unceasing. Only embodiment fails. -/
theorem flicker : flow.Balances web ∧ flow.Dissipative ∧ web.Unceasing ∧
    ¬ web.Embodied () :=
  ⟨fun _ _ => rfl, fun _ _ _ _ _ present => (nomatch present),
   fun N => match Handing.recurs false N with
    | ⟨t, later, arises⟩ => ⟨t, (), later, arises⟩,
   fun embodied => Nat.lt_irrefl 0 ((embodied 1).mp Nat.zero_lt_one)⟩

end Flicker

end Becoming
