import Becoming.Premises

/-!
# Openness: continued change needs exchange beyond what stands

`Becoming.Space` brings a finite, balanced, dissipative world whose arising is embodied to
rest. This module states what does the work: not finiteness but enclosure. Under balance
and dissipation, across a step whose exchange, together with whatever stands before or
after it, lies within finitely many conditions, the total standing does not rise, and it
falls whenever any condition's standing changes: a rise is given to, and giving needs
uptake there; a fall is taken from.

* **Total standing runs down.** Where what stands at each step is listed, each once
  (`Web.StandingCensus`), the total standing across a step enclosed around what stands
  (`Flow.AroundStanding`) does not rise (`Flow.standing_never_rises`), and any rise or
  fall of a condition's standing lowers it (`Flow.change_lowers`).
* **Standing comes to rest.** So where every step from some step on is enclosed around
  what stands, no condition's standing changes at arbitrarily late steps
  (`Flow.stills`).
* **Read of worlds.** A world with a census whose relata are embodied, with a balanced,
  dissipative flow, in which every step from some step on is enclosed around what stands,
  comes to rest: neither generation nor degeneration recurs (`World.rests_around`). Where
  equality of relata is decided, an enclosed step is enclosed around what stands, so
  enclosure from some step on suffices (`World.rests_enclosed`). Finiteness is not
  needed. Read the other way, generation without end in such a world needs, at
  arbitrarily late steps, a step not enclosed: exchange beyond every finite family
  (`World.generation_opens`).
* **Openness cannot be dropped.** The sides of `Handing`, also taking a unit from each of
  infinitely many ground relata and giving it back at every step, meet all eight premises
  of `Becoming.Premises` and generate without end. No step is enclosed, so dissipation,
  which binds only at enclosed steps, binds at none (`World.exposed_world`).

What stands and what is active coincide only for embodied relata; the standing laws need
no embodiment, and the reading of worlds uses it to turn arising and ceasing into rising
and falling. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {α : Type} {F C : Type}

/-! ## Lists -/

theorem mem_append_left {a : α} {l : List α} (m : List α) : a ∈ l → a ∈ l ++ m
  | .head _ => .head _
  | .tail _ mem => .tail _ (mem_append_left m mem)

theorem mem_append_right {a : α} : ∀ (l : List α) {m : List α}, a ∈ m → a ∈ l ++ m
  | [], _, mem => mem
  | _ :: l, _, mem => .tail _ (mem_append_right l mem)

/-! ## Total standing -/

/-- What stands at each step is listed, each once: finitely many conditions stand at each
step. -/
def Web.StandingCensus (W : Web F C) (stand : Nat → List C) : Prop :=
  ∀ t, Distinct (stand t) ∧ ∀ c, 0 < W.level t c ↔ c ∈ stand t

/-- The step from `t` is enclosed around what stands across it: some family without
repetition, closed across the step, holds whatever stands before or after it. -/
def Flow.AroundStanding (L : Flow F C) (stand : Nat → List C) (t : Nat) : Prop :=
  ∃ es, Distinct es ∧ (∀ c, c ∈ stand t → c ∈ es) ∧ (∀ c, c ∈ stand (t + 1) → c ∈ es) ∧
    L.ClosedAt es t

/-- The total standing over the list of what stands is the stock of any family without
repetition holding it. -/
theorem Web.StandingCensus.stock_eq {W : Web F C} {stand : Nat → List C}
    (census : W.StandingCensus stand) {es : List C} (distinct : Distinct es) {t : Nat}
    (within : ∀ c, c ∈ stand t → c ∈ es) : W.stock (stand t) t = W.stock es t :=
  Nat.le_antisymm (total_le_of_support (census t).1 fun c mem _ => within c mem)
    (total_le_of_support distinct fun c _ positive => ((census t).2 c).mp positive)

namespace Flow

variable {L : Flow F C} {W : Web F C} {stand : Nat → List C}

/-- With equality decided, a step enclosed by some family is enclosed around what
stands. -/
theorem Enclosed.aroundStanding [DecidableEq C] {t : Nat} (enclosed : L.Enclosed t)
    (stand : Nat → List C) : L.AroundStanding stand t :=
  match enclosed.around (stand t ++ stand (t + 1)) with
  | ⟨es, distinct, within, closed⟩ =>
    ⟨es, distinct, fun c mem => within c (mem_append_left _ mem),
     fun c mem => within c (mem_append_right _ mem), closed⟩

/-- A member of a family dissipated on across the step falling lowers the family's stock:
it is taken from. -/
theorem fall_lowers_on (balances : L.Balances W) {ds : List C} {t : Nat}
    (dissipates : L.DissipatesOn ds t) {c : C} (mem : c ∈ ds) (falls : W.Falls t c) :
    W.stock ds (t + 1) < W.stock ds t :=
  match total_pos (L.present t) (balances.fall_taken falls) with
  | ⟨_, present, takes⟩ => Nat.lt_of_lt_of_le
      (Nat.lt_add_of_pos_right (total_pos_of_mem (q := fun f => sign (total ds (L.take t f)))
        present (sign_pos (total_pos_of_mem mem takes))))
      (balances.runs_down dissipates)

/-- Under dissipation, across a step enclosed around what stands, the total standing falls
by at least the number of formations taking from the enclosing family. -/
theorem standing_runs_down (balances : L.Balances W) (dissipative : L.Dissipative)
    (census : W.StandingCensus stand) {t : Nat} :
    L.AroundStanding stand t →
      ∃ es, W.stock (stand (t + 1)) (t + 1) + L.takers es t ≤ W.stock (stand t) t
  | ⟨es, distinct, before, after, closed⟩ =>
    ⟨es, Nat.le_trans (Nat.le_of_eq (congrArg (· + L.takers es t) (census.stock_eq distinct after)))
      (Nat.le_trans (balances.runs_down (dissipative es t distinct closed))
        (Nat.le_of_eq (census.stock_eq distinct before).symm))⟩

/-- So the total standing does not rise. -/
theorem standing_never_rises (balances : L.Balances W) (dissipative : L.Dissipative)
    (census : W.StandingCensus stand) {t : Nat} (around : L.AroundStanding stand t) :
    W.stock (stand (t + 1)) (t + 1) ≤ W.stock (stand t) t :=
  match standing_runs_down balances dissipative census around with
  | ⟨_, runs⟩ => Nat.le_trans (Nat.le_add_right _ _) runs

/-- And any condition's standing rising or falling across the step lowers it. -/
theorem change_lowers (balances : L.Balances W) (dissipative : L.Dissipative)
    (census : W.StandingCensus stand) {t : Nat} (around : L.AroundStanding stand t) {c : C}
    (changes : W.Rises t c ∨ W.Falls t c) :
    W.stock (stand (t + 1)) (t + 1) < W.stock (stand t) t :=
  match around with
  | ⟨es, distinct, before, after, closed⟩ =>
    have dissipates := dissipative es t distinct closed
    have lowers : W.stock es (t + 1) < W.stock es t := match changes with
      | .inl rises => rise_lowers_on balances dissipates
          (after c (((census (t + 1)).2 c).mp (Nat.lt_of_le_of_lt (Nat.zero_le _) rises))) rises
      | .inr falls => fall_lowers_on balances dissipates
          (before c (((census t).2 c).mp (Nat.lt_of_le_of_lt (Nat.zero_le _) falls))) falls
    Nat.lt_of_le_of_lt (Nat.le_of_eq (census.stock_eq distinct after))
      (Nat.lt_of_lt_of_le lowers (Nat.le_of_eq (census.stock_eq distinct before).symm))

/-- Standing comes to rest: where every step from some step on is enclosed around what
stands, no condition's standing changes at arbitrarily late steps. -/
theorem stills (balances : L.Balances W) (dissipative : L.Dissipative)
    (census : W.StandingCensus stand) {T : Nat}
    (around : ∀ t, T ≤ t → L.AroundStanding stand t) :
    ¬ ∀ N, ∃ t c, N ≤ t ∧ (W.Rises t c ∨ W.Falls t c) :=
  fun changing => falls_finitely (fun t => W.stock (stand t) t) T
    (fun t later => standing_never_rises balances dissipative census (around t later))
    fun N => match changing (N + T) with
    | ⟨t, _, later, changes⟩ => ⟨t, Nat.le_trans (Nat.le_add_right N T) later,
        change_lowers balances dissipative census
          (around t (Nat.le_trans (Nat.le_add_left T N) later)) changes⟩

end Flow

/-! ## Worlds -/

namespace World

variable {w : World}

/-- With a census of the active relata, every relatum embodied, what stands is listed. -/
theorem standingCensus {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    (embodied : w.Embodied) : w.web.StandingCensus alive :=
  fun t => ⟨(census t).1, fun x => (embodied x t).symm.trans ((census t).2 x)⟩

/-- An embodied relatum arising rises. -/
theorem rises_of_arises (embodied : w.Embodied) {t : Nat} {x : w.Relatum}
    (arises : w.web.Arises t x) : w.web.Rises t x :=
  Web.ComesToStand.rises (W := w.web)
    ⟨fun standing => arises.1 ((embodied x t).mpr standing), (embodied x (t + 1)).mp arises.2⟩

/-- An embodied relatum ceasing falls. -/
theorem falls_of_ceases (embodied : w.Embodied) {t : Nat} {x : w.Relatum}
    (ceases : w.web.Ceases t x) : w.web.Falls t x :=
  Nat.lt_of_le_of_lt
    (Nat.le_of_eq (eq_zero_of_not_pos fun standing => ceases.2 ((embodied x (t + 1)).mpr standing)))
    ((embodied x t).mp ceases.1)

/-- A world with a census whose relata are embodied, with a balanced, dissipative flow, in
which every step from some step on is enclosed around what stands, comes to rest: neither
generation nor degeneration recurs. -/
theorem rests_around {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    (embodied : w.Embodied) (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (around : ∀ t, T ≤ t → w.flow.AroundStanding alive t) :
    ¬ w.Generative ∧ ¬ w.Degenerative :=
  have still := Flow.stills balanced dissipative (standingCensus census embodied) around
  ⟨fun generative => still fun N => match generative N with
    | ⟨t, x, later, arises⟩ => ⟨t, x, later, .inl (rises_of_arises embodied arises)⟩,
   fun degenerative => still fun N => match degenerative N with
    | ⟨t, x, later, ceases⟩ => ⟨t, x, later, .inr (falls_of_ceases embodied ceases)⟩⟩

/-- Where equality of relata is decided, enclosure from some step on suffices. -/
theorem rests_enclosed [DecidableEq w.Relatum] (counted : w.Counted) (embodied : w.Embodied)
    (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) : ¬ w.Generative ∧ ¬ w.Degenerative :=
  match counted with
  | ⟨_, census⟩ => rests_around census embodied balanced dissipative
      fun t later => (enclosed t later).aroundStanding _

/-- So generation without end, in a world with a census whose relata are embodied and
whose flow balances and dissipates, needs at arbitrarily late steps a step not enclosed:
exchange beyond every finite family. -/
theorem generation_opens [DecidableEq w.Relatum] (counted : w.Counted)
    (embodied : w.Embodied) (balanced : w.Balanced) (dissipative : w.Dissipative)
    (generative : w.Generative) (T : Nat) : ¬ ∀ t, T ≤ t → w.flow.Enclosed t :=
  fun enclosed => (rests_enclosed counted embodied balanced dissipative enclosed).1 generative

end World

/-! ## Openness cannot be dropped -/

namespace Exposed

inductive Relatum where
  | side (b : Bool)
  | ground (n : Nat)

/-- The sides stand as in `Handing`; the ground relata stand at nothing. -/
def level (t : Nat) : Relatum → Nat
  | .side b => Handing.stands b t
  | .ground _ => 0

/-- Across every step the side holding the standing hands it to the other, as in
`Handing`, and takes a unit from each ground relatum and gives it back. -/
def flow : Flow Relatum Relatum where
  present t := [.side (Handing.holder t)]
  take t x y := match x, y with
    | .side b, .side c => Handing.flow.take t b c
    | .side _, .ground _ => 1
    | .ground _, .side _ => 0
    | .ground _, .ground _ => 0
  give t x y := match x, y with
    | .side b, .side c => Handing.flow.give t b c
    | .side _, .ground _ => 1
    | .ground _, .side _ => 0
    | .ground _, .ground _ => 0

/-- A relatum is active while it stands; nothing depends on anything, and the sides draw
on everything. -/
def web : Web Relatum Relatum where
  level := level
  active t x := 0 < level t x
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

/-- Which side a side relatum is. -/
def sideOf : Relatum → Bool
  | .side b => b
  | .ground _ => false

/-- The index of a ground relatum. -/
def index : Relatum → Nat
  | .side _ => 0
  | .ground n => n

/-- No finite family holds every ground relatum. -/
theorem outside (cs : List Relatum) : ¬ Relatum.ground (beyond (cs.map index)) ∈ cs :=
  fun mem => beyond_not_mem _ (mem_map_of (g := index) mem)

/-- No step is enclosed: the side taking part takes from every ground relatum. -/
theorem open_at (t : Nat) : ¬ flow.Enclosed t :=
  fun ⟨cs, _, closed⟩ => Nat.zero_ne_one
    (closed (.side (Handing.holder t)) (.head _) _ (outside cs)).1.symm

/-- A side stands exactly when it holds the standing. -/
theorem stands_iff : ∀ (b : Bool) (t : Nat), 0 < Handing.stands b t ↔ b = Handing.holder t
  | true, 0 => ⟨fun _ => rfl, fun _ => Nat.zero_lt_one⟩
  | false, 0 => ⟨fun no => absurd no (Nat.lt_irrefl 0), fun no => Bool.noConfusion no⟩
  | true, 1 => ⟨fun no => absurd no (Nat.lt_irrefl 0), fun no => Bool.noConfusion no⟩
  | false, 1 => ⟨fun _ => rfl, fun _ => Nat.zero_lt_one⟩
  | true, t + 2 => stands_iff true t
  | false, t + 2 => stands_iff false t

/-- The side holding the standing is the one active relatum. -/
theorem census : web.Census fun t => [.side (Handing.holder t)] :=
  fun t => ⟨⟨fun no => (nomatch no), trivial⟩, fun x => match x with
    | .side b => ⟨fun standing => Eq.subst
          (motive := fun c => Relatum.side c ∈ [Relatum.side (Handing.holder t)])
          ((stands_iff b t).mp standing).symm (.head _),
        fun mem => (stands_iff b t).mpr (match mem_cons_cases mem with
          | .inl same => congrArg sideOf same
          | .inr no => nomatch no)⟩
    | .ground n => ⟨fun no => absurd no (Nat.lt_irrefl 0),
        fun (mem : Relatum.ground n ∈ [Relatum.side (Handing.holder t)]) => match mem with
          | .tail _ no => (nomatch no)⟩⟩

end Exposed

namespace World

/-- The sides of `Handing` exchanging with an unbounded ground. -/
def exposed : World :=
  ⟨Exposed.Relatum, Exposed.flow, Exposed.web⟩

/-- A world meeting all eight premises generates without end: no step is enclosed, so
dissipation binds at none. -/
theorem exposed_world : exposed.Premised ∧ exposed.Generative ∧ ∀ t, ¬ exposed.flow.Enclosed t :=
  ⟨.of (fun _ _ _ _ no => no.elim)
     (fun t c => match c with
      | .side c => Handing.balances t c
      | .ground _ => rfl)
     (fun t f _ present _ => match f, present with
      | _, .head _ => Handing.holder_stands t
      | _, .tail _ no => (nomatch no))
     (fun t f _ present _ => match f, present with
      | _, .head _ => ⟨Handing.holder_stands t, trivial⟩
      | _, .tail _ no => (nomatch no))
     (fun cs t distinct closed => absurd ⟨cs, distinct, closed⟩ (Exposed.open_at t))
     (fun _ _ => Iff.rfl) ⟨_, Exposed.census⟩ ⟨0, fun _ _ _ _ _ no => no.elim⟩,
   fun N => match Handing.recurs true N with
    | ⟨t, later, arises⟩ => ⟨t, .side true, later, arises⟩,
   Exposed.open_at⟩

end World

end Becoming
