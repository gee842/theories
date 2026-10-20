import Becoming.Identity

/-!
# Wholes: a persisting whole of brief parts, or of ending listed parts, needs their generation

`Becoming.Identity` names a lineage either as one formation or as its members (`Lineage`).
`Layered` names both, with no relation saying that the lineage is constituted by its
members. This module states one part–whole relation, coincidence of activity, and proves
what it carries.

* A formation is the *whole* of some parts when it is active exactly while some part is
  (`Web.Whole`). This is coincidence of activity, not constitution: every formation is the
  whole of itself (`Web.whole_self`), and two formations active at every step are each the
  whole of the other (`Immortal.each_other`). Parts *cover* the steps from `T` on when
  some part is active at each of them (`Web.Covered`). The active parts are *listed* when
  at each step a finite list names exactly them (`Web.Listed`). A formation's activity
  *ends* when from some step on it is never active (`Web.Ends`); it is *brief* for `d`
  when it is never active at two steps `d` apart (`Web.Brief`).
* A whole arises only as some part arises (`Whole.arises_part`), so a whole arising at
  arbitrarily late steps has parts arising at arbitrarily late steps
  (`Whole.parts_unceasing`).
* A cover needs the generation of parts. If no part is active at two steps `d` apart, a
  part arises within every `d` consecutive steps (`Covered.arises_within`). If each part's
  activity ends and the active parts are listed, parts arise at arbitrarily late steps
  (`Covered.needs_arising`), and outside every finite list of parts: ever new parts
  (`Covered.needs_new`). A whole active at every step from some step on is covered by its
  parts (`Whole.covered`), so it persists only through the generation of its parts
  (`Whole.arises_within`, `Whole.needs_arising`, `Whole.needs_new`). Under brevity that
  generation may be the same parts arising again (`Layered`); where parts end and are
  listed, it is ever new parts, though not more of them (`Generations` has two active at
  every step).
* Each premise is needed. With a part whose activity never ends, a whole persists while
  nothing arises (`Immortal`). With infinitely many parts active at once, each ending at
  a different step, it persists while nothing arises, so no finite list names its active
  parts (`Countless`). The premises are consistent: generation after generation, each
  active for two steps, makes a lineage active at every step that never arises, while a
  new generation arises at every step (`Generations`). The bound `d` is attained: members
  working in shifts of two steps arise only across odd steps (`Shifts`). The converse
  fails: parts arising at arbitrarily late steps, each active once, leave the whole
  inactive between them (`Gaps`).
* `Layered`'s lineage is the whole of its members (`Layered.composed`). Its members are
  brief for one step, so one arises at every step (`Layered.brief`, `Layered.within`);
  every arising is of one of the two, whose activity does not end (`Layered.arise_again`).

Which formations are parts of which, and whether a lineage is read as the whole of its
members, are representational choices. On Ren's delegation of 15 October 2026 生生不息 is read at
the level of the whole, as arising that recurs through renewal, lineages and members being levels
within it (DELEGATED-CHOICES D5). No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {F C : Type}

namespace Web

variable (W : Web F C)

/-- `w` is the whole of the formations satisfying `parts`: it is active exactly while
some part is. -/
def Whole (parts : F → Prop) (w : F) : Prop :=
  ∀ t, W.active t w ↔ ∃ p, parts p ∧ W.active t p

/-- At each step the list names exactly the active parts. -/
def Listed (parts : F → Prop) (alive : Nat → List F) : Prop :=
  ∀ t p, p ∈ alive t ↔ parts p ∧ W.active t p

/-- The formation's activity ends: from some step on it is never active. -/
def Ends (f : F) : Prop :=
  ∃ T, ∀ t, T ≤ t → ¬ W.active t f

/-- The formation is never active at two steps `d` apart: active over one stretch of
steps, it is active for at most `d` of them. -/
def Brief (d : Nat) (f : F) : Prop :=
  ∀ t, W.active t f → ¬ W.active (t + d) f

/-- The formations satisfying `parts` cover the steps from `T` on: at each of them some
part is active. -/
def Covered (parts : F → Prop) (T : Nat) : Prop :=
  ∀ t, T ≤ t → ∃ p, parts p ∧ W.active t p

/-- Every formation is the whole of itself: `Whole` is coincidence of activity, not
constitution. -/
theorem whole_self (f : F) : W.Whole (· = f) f :=
  fun _ => ⟨fun active => ⟨f, rfl, active⟩,
    fun ⟨_, same, active⟩ => Eq.subst (motive := fun g => W.active _ g) same active⟩

variable {W} {parts : F → Prop} {w : F}

/-- A whole arises only as some part arises. -/
theorem Whole.arises_part (whole : W.Whole parts w) {t : Nat} (arises : W.Arises t w) :
    ∃ p, parts p ∧ W.Arises t p :=
  match (whole (t + 1)).mp arises.2 with
  | ⟨p, part, active⟩ => ⟨p, part, fun before => arises.1 ((whole t).mpr ⟨p, part, before⟩),
      active⟩

/-- So a whole arising at arbitrarily late steps has parts arising at arbitrarily late
steps. -/
theorem Whole.parts_unceasing (whole : W.Whole parts w)
    (unceasing : ∀ N, ∃ t, N ≤ t ∧ W.Arises t w) :
    ∀ N, ∃ t p, N ≤ t ∧ parts p ∧ W.Arises t p :=
  fun N => match unceasing N with
  | ⟨t, later, arises⟩ => match whole.arises_part arises with
    | ⟨p, part, arising⟩ => ⟨t, p, later, part, arising⟩

/-- Finitely many formations whose activity ends all end by one step. -/
theorem Ends.all : ∀ {l : List F}, (∀ f, f ∈ l → W.Ends f) →
    ∃ M, ∀ f, f ∈ l → ∀ t, M ≤ t → ¬ W.active t f
  | [], _ => ⟨0, fun _ mem => (nomatch mem)⟩
  | _ :: _, ends => match ends _ (.head _), Ends.all fun f mem => ends f (.tail _ mem) with
    | ⟨T, gone⟩, ⟨M, rest⟩ => ⟨T + M, fun f mem t later => match f, mem with
      | _, .head _ => gone t (Nat.le_trans (Nat.le_add_right T M) later)
      | f, .tail _ mem => rest f mem t (Nat.le_trans (Nat.le_add_left M T) later)⟩

/-- With no part arising across the `k` steps from `S`, a part active `k` steps later was
not inactive at `S`. -/
theorem active_back {S : Nat} : ∀ {k : Nat},
    (∀ j, j < k → ∀ p, parts p → ¬ W.Arises (S + j) p) →
    ∀ {p : F}, parts p → W.active (S + k) p → ¬ ¬ W.active S p
  | 0, _, _, _, active => fun inactive => inactive active
  | k + 1, quiet, p, part, active => fun inactive => quiet k (Nat.lt_succ_self k) p part
      ⟨fun before => active_back (fun j below => quiet j (Nat.lt_succ_of_lt below)) part before
        inactive, active⟩

/-- Parts covering the steps from `T` on, none of them active at two steps `d` apart,
have a part arising within every `d` consecutive steps from `T` on. -/
theorem Covered.arises_within {d T : Nat} (covered : W.Covered parts T)
    (brief : ∀ p, parts p → W.Brief d p) {S : Nat} (after : T ≤ S) :
    ¬ ∀ j, j < d → ∀ p, parts p → ¬ W.Arises (S + j) p :=
  fun quiet => match covered (S + d) (Nat.le_trans after (Nat.le_add_right S d)) with
  | ⟨_, part, active⟩ =>
    active_back quiet part active fun before => brief _ part S before active

/-- Parts covering the steps from some step on, each of whose activity ends, with the
active ones listed, arise at arbitrarily late steps. -/
theorem Covered.needs_arising {T : Nat} {alive : Nat → List F} (covered : W.Covered parts T)
    (listed : W.Listed parts alive) (ends : ∀ p, parts p → W.Ends p) (N : Nat) :
    ¬ ∀ t, N ≤ t → ∀ p, parts p → ¬ W.Arises t p :=
  fun quiet => match Ends.all (l := alive (N + T)) fun p mem => ends p ((listed _ p).mp mem).1 with
  | ⟨M, gone⟩ =>
    match covered (N + T + M) (Nat.le_trans (Nat.le_add_left T N)
        (Nat.le_add_right (N + T) M)) with
    | ⟨p, part, active⟩ =>
      active_back (fun j _ p part => quiet (N + T + j)
          (Nat.le_trans (Nat.le_add_right N T) (Nat.le_add_right (N + T) j)) p part) part
        active fun before => gone p ((listed _ p).mpr ⟨part, before⟩) (N + T + M)
          (Nat.le_add_left M (N + T)) active

/-- So no finite list of parts carries the cover: parts outside it arise at arbitrarily
late steps. -/
theorem Covered.needs_new {T : Nat} {alive : Nat → List F} (covered : W.Covered parts T)
    (listed : W.Listed parts alive) (ends : ∀ p, parts p → W.Ends p) {l : List F}
    (within : ∀ p, p ∈ l → parts p) (N : Nat) :
    ¬ ∀ t, N ≤ t → ∀ p, parts p → ¬ p ∈ l → ¬ W.Arises t p :=
  fun quiet => match Ends.all (l := l) fun p mem => ends p (within p mem) with
  | ⟨M, gone⟩ => covered.needs_arising listed ends (N + M)
      fun t later p part arises => quiet t (Nat.le_trans (Nat.le_add_right N M) later) p part
        (fun mem => gone p mem (t + 1)
          (Nat.le_trans (Nat.le_add_left M N) (Nat.le_trans later (Nat.le_succ t))) arises.2)
        arises

/-- A whole active at every step from `T` on is covered by its parts from `T` on. -/
theorem Whole.covered (whole : W.Whole parts w) {T : Nat}
    (persists : ∀ t, T ≤ t → W.active t w) : W.Covered parts T :=
  fun t later => (whole t).mp (persists t later)

/-- A whole active at every step from `T` on, made of parts none of which is active at two
steps `d` apart, has a part arising within every `d` consecutive steps from `T` on. -/
theorem Whole.arises_within {d : Nat} (whole : W.Whole parts w)
    (brief : ∀ p, parts p → W.Brief d p) {T : Nat} (persists : ∀ t, T ≤ t → W.active t w)
    {S : Nat} (after : T ≤ S) : ¬ ∀ j, j < d → ∀ p, parts p → ¬ W.Arises (S + j) p :=
  (whole.covered persists).arises_within brief after

/-- A whole active at every step from some step on, made of parts each of whose activity
ends, with its active parts listed, has parts arising at arbitrarily late steps: it
persists only through the unceasing generation of its parts. -/
theorem Whole.needs_arising {alive : Nat → List F} (whole : W.Whole parts w)
    (listed : W.Listed parts alive) (ends : ∀ p, parts p → W.Ends p) {T : Nat}
    (persists : ∀ t, T ≤ t → W.active t w) (N : Nat) :
    ¬ ∀ t, N ≤ t → ∀ p, parts p → ¬ W.Arises t p :=
  (whole.covered persists).needs_arising listed ends N

/-- Such a whole persists only through ever new parts: parts outside any finite list of
parts arise at arbitrarily late steps. -/
theorem Whole.needs_new {alive : Nat → List F} (whole : W.Whole parts w)
    (listed : W.Listed parts alive) (ends : ∀ p, parts p → W.Ends p) {T : Nat}
    (persists : ∀ t, T ≤ t → W.active t w) {l : List F} (within : ∀ p, p ∈ l → parts p)
    (N : Nat) : ¬ ∀ t, N ≤ t → ∀ p, parts p → ¬ p ∈ l → ¬ W.Arises t p :=
  (whole.covered persists).needs_new listed ends within N

end Web

/-! ## Witnesses -/

namespace Generations

/-- A lineage, and its members, one given at each step. -/
inductive Formation where
  | lineage
  | member (n : Nat)

/-- The members. -/
def parts : Formation → Prop
  | .lineage => False
  | .member _ => True

/-- The `n`th member is active at steps `n` and `n + 1`; the lineage at every step. -/
def web : Web Formation Unit where
  level _ _ := 0
  active t f := match f with
    | .lineage => True
    | .member n => t = n ∨ t = n + 1
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- The members active at each step. -/
def alive : Nat → List Formation
  | 0 => [.member 0]
  | t + 1 => [.member (t + 1), .member t]

theorem whole : web.Whole parts .lineage :=
  fun t => ⟨fun _ => ⟨.member t, trivial, .inl rfl⟩, fun _ => trivial⟩

theorem listed : web.Listed parts alive
  | 0, .lineage => ⟨fun mem => match mem with | .tail _ no => (nomatch no),
      fun ⟨no, _⟩ => no.elim⟩
  | 0, .member n => ⟨fun mem => match n, (mem : Formation.member n ∈ [.member 0]) with
      | _, .head _ => ⟨trivial, .inl rfl⟩
      | _, .tail _ no => (nomatch no),
      fun ⟨_, active⟩ => match active with
      | .inl same => show Formation.member n ∈ [.member 0] from same ▸ .head _
      | .inr same => Nat.noConfusion same⟩
  | _ + 1, .lineage => ⟨fun mem => match mem with | .tail _ (.tail _ no) => (nomatch no),
      fun ⟨no, _⟩ => no.elim⟩
  | t + 1, .member n => ⟨fun mem =>
      match n, (mem : Formation.member n ∈ [.member (t + 1), .member t]) with
      | _, .head _ => ⟨trivial, .inl rfl⟩
      | _, .tail _ (.head _) => ⟨trivial, .inr rfl⟩
      | _, .tail _ (.tail _ no) => (nomatch no),
      fun ⟨_, active⟩ => match active with
      | .inl same => show Formation.member n ∈ [.member (t + 1), .member t] from same ▸ .head _
      | .inr same => show Formation.member n ∈ [.member (t + 1), .member t] from
          Nat.succ.inj same ▸ .tail _ (.head _)⟩

theorem ends : ∀ p, parts p → web.Ends p
  | .member n, _ => ⟨n + 2, fun _ later active => match active with
    | .inl same => Nat.lt_irrefl n (Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right (Nat.succ_pos 1))
        (Eq.subst (motive := (n + 2 ≤ ·)) same later))
    | .inr same => Nat.not_succ_le_self (n + 1) (Eq.subst (motive := (n + 2 ≤ ·)) same later)⟩

theorem brief : ∀ p, parts p → web.Brief 2 p
  | .member _, _ => fun t active later => match active, later with
    | .inl now, .inl two =>
      Nat.ne_of_lt (Nat.lt_add_of_pos_right (Nat.succ_pos 1)) (now.trans two.symm)
    | .inl now, .inr two =>
      Nat.ne_of_lt (Nat.lt_succ_self (t + 1)) ((congrArg (· + 1) now).trans two.symm)
    | .inr now, .inl two => Nat.ne_of_lt (Nat.lt_add_of_pos_right (Nat.succ_pos 2))
        ((congrArg (· + 2) now).symm.trans two).symm
    | .inr now, .inr two => Nat.ne_of_lt (Nat.lt_add_of_pos_right (Nat.succ_pos 1))
        (now.trans (congrArg (· + 1) (Nat.succ.inj two).symm))

/-- Generation after generation, each active for two steps, makes a lineage active at
every step: every premise of `Whole.arises_within` and `Whole.needs_arising` holds, a
member arises at every step, and the lineage never arises. -/
theorem generations : web.Whole parts .lineage ∧ web.Listed parts alive ∧
    (∀ p, parts p → web.Ends p) ∧ (∀ p, parts p → web.Brief 2 p) ∧
    (∀ t, web.active t .lineage) ∧
    (∀ t, web.Arises t (.member (t + 1))) ∧ ∀ t, ¬ web.Arises t .lineage :=
  ⟨whole, listed, ends, brief, fun _ => trivial,
   fun t => ⟨fun active => match active with
      | .inl same => Nat.ne_of_lt (Nat.lt_succ_self t) same
      | .inr same => Nat.ne_of_lt (Nat.lt_add_of_pos_right (Nat.succ_pos 1)) same,
    .inl rfl⟩,
   fun _ arises => arises.1 trivial⟩

end Generations

namespace Shifts

theorem odd_two (t : Nat) : odd (t + 2) = odd t :=
  show (!!odd t) = odd t from match odd t with
  | true => rfl
  | false => rfl

theorem half_even : ∀ t, odd t = false → Pulse.half (t + 1) = Pulse.half t
  | 0, _ => rfl
  | 1, odd' => (nomatch odd')
  | t + 2, even => congrArg (· + 1) (half_even t ((odd_two t).symm.trans even))

/-- The members of `Generations`, the `n`th active at steps `2n` and `2n + 1`; the lineage
at every step. -/
def web : Web Generations.Formation Unit where
  level _ _ := 0
  active t f := match f with
    | .lineage => True
    | .member n => Pulse.half t = n
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- Members working in shifts of two steps: the lineage is their whole and is active at
every step, no member is active at two steps two apart, and no member arises across an
even step. So a part arises within every two consecutive steps but not within every
one: the bound of `Whole.arises_within` is attained. -/
theorem shifts : web.Whole Generations.parts .lineage ∧
    (∀ p, Generations.parts p → web.Brief 2 p) ∧ (∀ t, web.active t .lineage) ∧
    ∀ t, odd t = false → ∀ p, ¬ web.Arises t p :=
  ⟨fun t => ⟨fun _ => ⟨.member (Pulse.half t), trivial, rfl⟩, fun _ => trivial⟩,
   fun p _ => match p with
    | .member _ => fun _ now later => Nat.succ_ne_self _ (later.trans now.symm),
   fun _ => trivial,
   fun t even p arises => match p with
    | .lineage => arises.1 trivial
    | .member _ => arises.1 ((half_even t even).symm.trans arises.2)⟩

end Shifts

namespace Immortal

/-- A whole (`false`) of one part (`true`) that is always active. -/
def web : Web Bool Unit where
  level _ _ := 0
  active _ _ := True
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- With a part whose activity never ends, the whole persists, its active parts are listed,
and nothing ever arises. -/
theorem immortal : web.Whole (· = true) false ∧ web.Listed (· = true) (fun _ => [true]) ∧
    (∀ t, web.active t false) ∧ (∀ t p, ¬ web.Arises t p) ∧ ¬ web.Ends true :=
  ⟨fun _ => ⟨fun _ => ⟨true, rfl, trivial⟩, fun _ => trivial⟩,
   fun _ p => ⟨fun mem => match p, mem with
      | _, .head _ => ⟨rfl, trivial⟩,
      fun ⟨same, _⟩ => match p, same with
      | _, rfl => .head _⟩,
   fun _ => trivial, fun _ _ arises => arises.1 trivial,
   fun ⟨T, gone⟩ => gone T (Nat.le_refl T) trivial⟩

/-- The two formations, active at every step, are each the whole of the other. -/
theorem each_other : web.Whole (· = true) false ∧ web.Whole (· = false) true :=
  ⟨fun _ => ⟨fun _ => ⟨true, rfl, trivial⟩, fun _ => trivial⟩,
   fun _ => ⟨fun _ => ⟨false, rfl, trivial⟩, fun _ => trivial⟩⟩

end Immortal

namespace Countless

/-- The parts: every `some n`; `none` is the whole. -/
def parts : Option Nat → Prop
  | none => False
  | some _ => True

/-- The whole is active at every step; the `n`th part up to step `n`. -/
def web : Web (Option Nat) Unit where
  level _ _ := 0
  active t f := match f with
    | none => True
    | some n => t ≤ n
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

theorem whole : web.Whole parts none :=
  fun t => ⟨fun _ => ⟨some t, trivial, Nat.le_refl t⟩, fun _ => trivial⟩

theorem ends : ∀ p, parts p → web.Ends p
  | some n, _ => ⟨n + 1, fun _ later active => Nat.not_succ_le_self n
      (Nat.le_trans later active)⟩

theorem never : ∀ t p, ¬ web.Arises t p
  | _, none, arises => arises.1 trivial
  | _, some _, arises => arises.1 (Nat.le_of_succ_le arises.2)

/-- With infinitely many parts active at once, each ending at a different step, the whole
persists and nothing ever arises; so no finite list names its active parts. -/
theorem countless : web.Whole parts none ∧ (∀ p, parts p → web.Ends p) ∧
    (∀ t, web.active t none) ∧ (∀ t p, ¬ web.Arises t p) ∧
    ¬ ∃ alive, web.Listed parts alive :=
  ⟨whole, ends, fun _ => trivial, never,
   fun ⟨_, listed⟩ => Web.Whole.needs_arising whole listed ends (T := 0) (fun _ _ => trivial) 0
     fun t _ p _ => never t p⟩

end Countless

namespace Gaps

/-- One at the odd steps, as a list: the member of that step. -/
def alive (t : Nat) : List Generations.Formation :=
  match odd t with
  | true => [.member t]
  | false => []

/-- The `n`th member is active only at step `n`, and only if `n` is odd; the lineage
while some member is. -/
def web : Web Generations.Formation Unit where
  level _ _ := 0
  active t f := match f with
    | .lineage => odd t = true
    | .member n => t = n ∧ odd t = true
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

theorem whole : web.Whole Generations.parts .lineage :=
  fun t => ⟨fun odd' => ⟨.member t, trivial, rfl, odd'⟩,
    fun ⟨p, part, active⟩ => match p, part, active with
    | .member _, _, ⟨_, odd'⟩ => odd'⟩

theorem alive_odd {t : Nat} (h : odd t = true) : alive t = [.member t] := by
  unfold alive; rw [h]

theorem alive_even {t : Nat} (h : odd t = false) : alive t = [] := by
  unfold alive; rw [h]

theorem listed : web.Listed Generations.parts alive :=
  fun t p => match h : odd t with
  | true => (alive_odd h) ▸ match p with
    | .lineage => ⟨fun mem => match mem with | .tail _ no => (nomatch no),
        fun ⟨no, _⟩ => no.elim⟩
    | .member n => ⟨fun mem => match mem with
        | .head _ => ⟨trivial, rfl, h⟩
        | .tail _ no => (nomatch no),
        fun ⟨_, same, _⟩ => show Generations.Formation.member n ∈ [.member t] from
          same ▸ .head _⟩
  | false => (alive_even h) ▸ ⟨fun mem => (nomatch mem), fun ⟨part, active⟩ =>
      match p, part, active with
      | .member _, _, ⟨_, odd'⟩ => (nomatch h.symm.trans odd')⟩

theorem ends : ∀ p, Generations.parts p → web.Ends p
  | .member n, _ => ⟨n + 1, fun _ later active => Nat.not_succ_le_self n (active.1 ▸ later)⟩

/-- Members active once each, at the odd steps: they arise at arbitrarily late steps,
their activity ends and the active ones are listed, yet the whole is inactive at every
even step. -/
theorem gaps : web.Whole Generations.parts .lineage ∧ web.Listed Generations.parts alive ∧
    (∀ p, Generations.parts p → web.Ends p) ∧
    (∀ N, ∃ t p, N ≤ t ∧ Generations.parts p ∧ web.Arises t p) ∧
    ∀ t, odd t = false → ¬ web.active t .lineage :=
  ⟨whole, listed, ends,
   fun N => match h : odd N with
    | false => ⟨N, .member (N + 1), Nat.le_refl N, trivial,
        fun ⟨same, _⟩ => Nat.ne_of_lt (Nat.lt_succ_self N) same,
        rfl, congrArg (!·) h⟩
    | true => ⟨N + 1, .member (N + 2), Nat.le_succ N, trivial,
        fun ⟨same, _⟩ => Nat.ne_of_lt (Nat.lt_succ_self (N + 1)) same,
        rfl, show (!!odd N) = true from congrArg (fun b => !!b) h⟩,
   fun _ even odd' => (nomatch even.symm.trans odd')⟩

end Gaps

namespace Layered

/-- The lineage is the whole of its members. -/
theorem composed : web.Whole (· ≠ .lineage) .lineage :=
  fun t => ⟨fun _ => match h : odd t with
      | true => ⟨.second, Level.noConfusion, h⟩
      | false => ⟨.first, Level.noConfusion, h⟩,
    fun _ => trivial⟩

/-- Neither member is active at two consecutive steps. -/
theorem brief : ∀ p, p ≠ Level.lineage → web.Brief 1 p
  | .first, _ => fun t now later =>
      Bool.noConfusion ((congrArg (!·) now).symm.trans (later : (!odd t) = false))
  | .second, _ => fun t now later =>
      Bool.noConfusion ((congrArg (!·) now).symm.trans (later : (!odd t) = true))
  | .lineage, other => absurd rfl other

/-- So `Whole.arises_within` applies with `d = 1`: a member arises across every step. -/
theorem within (S : Nat) : ¬ ∀ j, j < 1 → ∀ p, p ≠ Level.lineage → ¬ web.Arises (S + j) p :=
  composed.arises_within brief (T := 0) (fun _ _ => trivial) (Nat.zero_le S)

/-- Every arising is the arising of one of the two members, and neither member's activity
ends: under brevity the generation that carries the lineage is the same two members
arising again, nothing new. -/
theorem arise_again :
    (∀ t p, web.Arises t p → p ∈ [Level.first, .second]) ∧ ¬ web.Ends .first ∧
    ¬ web.Ends .second :=
  ⟨fun _ p arises => match p, arises with
    | .first, _ => .head _
    | .second, _ => .tail _ (.head _)
    | .lineage, arises => absurd trivial arises.1,
   fun ⟨T, gone⟩ => match h : odd T with
    | false => gone T (Nat.le_refl T) h
    | true => gone (T + 1) (Nat.le_succ T) (congrArg (!·) h),
   fun ⟨T, gone⟩ => match h : odd T with
    | true => gone T (Nat.le_refl T) h
    | false => gone (T + 1) (Nat.le_succ T) (congrArg (!·) h)⟩

end Layered

end Becoming
