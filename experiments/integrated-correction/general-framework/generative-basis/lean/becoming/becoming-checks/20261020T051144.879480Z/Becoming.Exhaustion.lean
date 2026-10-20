import Becoming.Seeking
import Becoming.Exclusion

/-!
# Exhaustion: where a take that is more than now ends

`Becoming.Seeking` states that a target of "more than now", a quantity that rises across each
step (`MoreThanNow`), is met only by change, and that where what stands runs down at every step
its rises do not recur (`Flow.more_exhausted`): the pursuit ends, not the seeker.
`Becoming.Exclusion` states what taking all that is given excludes and leaves open how such
taking forms. This module reads "more than now" on what a formation takes from a condition, and
states, with no axiom and no premise beyond what each law names, where that taking leads.

* **A rising take comes to take all that is given.** A take that is more than now at each of `n`
  steps has risen by at least `n` (`more_accumulates`). From a condition given at most `B` at
  each step, after `B + 1` such steps the take exceeds what is given (`Flow.exceeds_of_more`):
  taking part, the formation takes all that is given (`Flow.takesAll_of_more`), and the taking
  across the step exceeds what is given (`Flow.excess_of_more`).
* **Taking beyond what is given cannot last.** Under balance, a formation taking part and taking
  more than is given to the condition at each of `W.level T c + 1` steps from `T` does not exist
  (`Flow.beyond_given_bounded`): every such step lowers the level by at least one
  (`Flow.excess_bounded`).
* **The seeker ends.** Under balance alone, a formation that, while active, takes part with a
  take that is more than now, from a condition given at most `B` at each step, is not active at
  each of the `B + 1 + (W.level (T + (B + 1)) c + 1)` steps from any `T`
  (`Flow.seeking_bounded`), so it does not stay active (`Flow.seeking_not_continues`); where its
  activity does not resume once it stops, it is inactive from then on (`Flow.seeking_ends`). The
  ending is derived: neither its need nor its dependence on the condition is supplied.
* **Exhaustion of the renewal.** Where renewal depends on what it renews (balance, only active
  formations giving, activity needing support, whatever gives to the condition depending on it at
  a need of at least `m`), and the seeker stays active while the condition is at least `m`, the
  level falls below `m` within that window, and from then on every formation depending on the
  condition at a need of at least `m` is inactive (`Flow.seeking_exhausts`), the renewers
  included.
* **A seeker among `Exceeding`'s members** (`Seeker.course`). The renewer gives two units across
  each step and the first takes one more at each step than at the step before. It takes all that
  is given from step one, and from step four it is inactive, which also follows from the law
  (`Seeker.ends_by_law`); the renewer is active at every step. In `Alone` of
  `Becoming.Continuation` the same first takes two, all that is given, at every step and is active
  at every step (`Alone.takes_all`): what ends the seeker is that its take rises, not that it
  takes all.

What is not derived: that a formation's take rises; which formations seek; a need or a horizon
that would stop the rise. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

/-- **More than now accumulates.** A quantity that is more than now at each of `n` steps has risen
by at least `n`. -/
theorem more_accumulates {g : Nat → Nat} {T : Nat} :
    ∀ {n : Nat}, (∀ i, i < n → MoreThanNow id g (T + i)) → g T + n ≤ g (T + n)
  | 0, _ => Nat.le_refl _
  | n + 1, more =>
    Nat.succ_le_of_lt (Nat.lt_of_le_of_lt (more_accumulates fun i below => more i (Nat.lt_succ_of_lt below))
      (more n (Nat.lt_succ_self n)))

/-- Of a bounded search below `N`: either the quantity is at least `m` at every step below `N`, or
some step below `N` finds it below `m`. -/
theorem all_or_below (h : Nat → Nat) (m : Nat) :
    ∀ N, (∀ j, j < N → m ≤ h j) ∨ ∃ j, j < N ∧ h j < m
  | 0 => .inl fun _ below => absurd below (Nat.not_lt_zero _)
  | N + 1 =>
    match all_or_below h m N with
    | .inr ⟨j, below, low⟩ => .inr ⟨j, Nat.lt_succ_of_lt below, low⟩
    | .inl all =>
      match Nat.decLt (h N) m with
      | isTrue low => .inr ⟨N, Nat.lt_succ_self N, low⟩
      | isFalse high => .inl fun j below =>
        match Nat.lt_or_eq_of_le (Nat.le_of_lt_succ below) with
        | .inl lt => all j lt
        | .inr same => Eq.subst (motive := fun x => m ≤ h x) same.symm (Nat.ge_of_not_lt high)

namespace Flow

variable {F C : Type} {L : Flow F C} {W : Web F C}

/-- What one formation taking part takes is at most what all those taking part take. -/
theorem take_le_taken {t : Nat} {f : F} {c : C} (present : f ∈ L.present t) :
    L.take t f c ≤ L.taken t c :=
  le_total_of_mem (q := fun g => L.take t g c) present

/-- **A rising take passes what is given.** A take more than now at each of `n` steps from `T`,
from a condition given at most `B` at each step, exceeds what is given at `T + n` where `B < n`. -/
theorem exceeds_of_more {f : F} {c : C} {B T n : Nat} (bounded : ∀ t, L.given t c ≤ B)
    (more : ∀ i, i < n → MoreThanNow id (fun s => L.take s f c) (T + i)) (beyond : B < n) :
    L.given (T + n) c < L.take (T + n) f c :=
  Nat.lt_of_le_of_lt (bounded (T + n))
    (Nat.lt_of_lt_of_le beyond (Nat.le_trans (Nat.le_add_left n _) (more_accumulates more)))

/-- **A rising take comes to take all that is given**, from `B + 1` steps on, while it takes part. -/
theorem takesAll_of_more {f : F} {c : C} {B T n : Nat} (bounded : ∀ t, L.given t c ≤ B)
    (more : ∀ i, i < n → MoreThanNow id (fun s => L.take s f c) (T + i)) (beyond : B < n)
    (present : f ∈ L.present (T + n)) : L.TakesAll (T + n) f c :=
  ⟨present, Nat.le_of_lt (exceeds_of_more bounded more beyond)⟩

/-- Taking part with a rising take, past `B + 1` steps the taking exceeds what is given. -/
theorem excess_of_more {f : F} {c : C} {B T n : Nat} (bounded : ∀ t, L.given t c ≤ B)
    (more : ∀ i, i < n → MoreThanNow id (fun s => L.take s f c) (T + i)) (beyond : B < n)
    (present : f ∈ L.present (T + n)) : L.given (T + n) c < L.taken (T + n) c :=
  Nat.lt_of_lt_of_le (exceeds_of_more bounded more beyond) (take_le_taken present)

/-- **Taking beyond what is given cannot last.** Under balance, no formation takes part and takes
more than is given to the condition at each of `W.level T c + 1` steps from `T`. -/
theorem beyond_given_bounded (balances : L.Balances W) {f : F} {c : C} (T : Nat) :
    ¬ ∀ j, j < W.level T c + 1 → f ∈ L.present (T + j) ∧ L.given (T + j) c < L.take (T + j) f c :=
  fun beyond =>
    have bound := excess_bounded balances (T := T) (W.level T c + 1) fun j below =>
      match beyond j below with
      | ⟨present, more⟩ => Nat.lt_of_lt_of_le more (take_le_taken present)
    Nat.lt_irrefl (W.level T c)
      (Nat.lt_of_lt_of_le (Nat.lt_succ_self _) (Nat.le_trans (Nat.le_add_left _ _) bound))

/-- **The seeker is not active through the window.** Under balance, a formation that, while
active, takes part with a take more than now, from a condition given at most `B` at each step, is
not active at each of the `B + 1 + (W.level (T + (B + 1)) c + 1)` steps from `T`. -/
theorem seeking_bounded (balances : L.Balances W) {f : F} {c : C} {B : Nat}
    (bounded : ∀ t, L.given t c ≤ B)
    (seeks : ∀ t, W.active t f → f ∈ L.present t ∧ MoreThanNow id (fun s => L.take s f c) t) (T : Nat) :
    ¬ ∀ j, j < B + 1 + (W.level (T + (B + 1)) c + 1) → W.active (T + j) f :=
  fun active => beyond_given_bounded balances (f := f) (T + (B + 1)) fun j below =>
    have inside : B + 1 + j < B + 1 + (W.level (T + (B + 1)) c + 1) := Nat.add_lt_add_left below (B + 1)
    have at_j := seeks _ (active _ inside)
    have over := exceeds_of_more (T := T) (n := B + 1 + j) bounded
      (fun i lt => (seeks _ (active i (Nat.lt_trans lt inside))).2)
      (Nat.lt_of_lt_of_le (Nat.lt_succ_self B) (Nat.le_add_right (B + 1) j))
    Eq.subst (motive := fun s => f ∈ L.present s ∧ L.given s c < L.take s f c)
      (Nat.add_assoc T (B + 1) j).symm ⟨at_j.1, over⟩

/-- **The seeker does not stay active.** -/
theorem seeking_not_continues (balances : L.Balances W) {f : F} {c : C} {B : Nat}
    (bounded : ∀ t, L.given t c ≤ B)
    (seeks : ∀ t, W.active t f → f ∈ L.present t ∧ MoreThanNow id (fun s => L.take s f c) t) (T : Nat) :
    ¬ ∀ j, W.active (T + j) f :=
  fun active => seeking_bounded balances bounded seeks T fun j _ => active j

/-- **The seeker ends.** Where its activity does not resume once it stops, it is inactive from
`T + (B + 1 + W.level (T + (B + 1)) c)` on. The ending is derived, with no need or dependence
supplied. -/
theorem seeking_ends (balances : L.Balances W) {f : F} {c : C} {B : Nat}
    (bounded : ∀ t, L.given t c ≤ B)
    (seeks : ∀ t, W.active t f → f ∈ L.present t ∧ MoreThanNow id (fun s => L.take s f c) t) {T : Nat}
    (lasting : ∀ i, W.active (T + i + 1) f → W.active (T + i) f) :
    ∀ k, ¬ W.active (T + (B + 1 + W.level (T + (B + 1)) c + k)) f :=
  fun k active => seeking_bounded balances bounded seeks T fun _ below =>
    Web.active_before lasting
      (Nat.le_trans (Nat.le_of_lt_succ (Nat.lt_of_lt_of_le below (Nat.le_of_eq (Nat.add_assoc _ _ 1).symm)))
        (Nat.le_add_right _ k)) active

/-- **Exhaustion of the renewal.** Where renewal depends on what it renews and the seeker stays
active while the condition is at least `m`, the level falls below `m` at some step of the window,
and from then on every formation depending on the condition at a need of at least `m` is
inactive. -/
theorem seeking_exhausts (balances : L.Balances W) (acting : L.Acting W) (dependent : W.Dependent)
    {f : F} {c : C} {m B T : Nat}
    (gated : ∀ t g, g ∈ L.present t → 0 < L.give t g c → W.requires t g c ∧ m ≤ W.need t g c)
    (bounded : ∀ t, L.given t c ≤ B)
    (seeks : ∀ t, W.active t f → f ∈ L.present t ∧ MoreThanNow id (fun s => L.take s f c) t)
    (persists : ∀ j, m ≤ W.level (T + j) c → W.active (T + j) f) :
    ∃ j, j < B + 1 + (W.level (T + (B + 1)) c + 1) ∧
      ∀ n g, W.requires (T + j + n) g c → m ≤ W.need (T + j + n) g c → ¬ W.active (T + j + n) g :=
  match all_or_below (fun j => W.level (T + j) c) m (B + 1 + (W.level (T + (B + 1)) c + 1)) with
  | .inl high => absurd (fun j below => persists j (high j below)) (seeking_bounded balances bounded seeks T)
  | .inr ⟨j, inside, low⟩ =>
    ⟨j, inside, ends_below dependent (stays_below balances acting dependent gated low)⟩

end Flow

/-! ## A seeker among `Exceeding`'s members -/

namespace Seeker

open Exceeding

def level : Nat → Nat
  | 0 => 3
  | 1 => 4
  | 2 => 4
  | 3 => 3
  | n + 4 => 1 + 2 * n

def present : Nat → List Member
  | 0 => [.renewer, .first]
  | 1 => [.renewer, .first]
  | 2 => [.renewer, .first]
  | 3 => [.renewer, .first]
  | _ + 4 => [.renewer]

/-- The renewer gives two units across each step; the first takes one more at each step than at
the step before. -/
def flow : Flow Member Unit where
  present := present
  take t f _ := match f with
    | .renewer => 0
    | .first => t + 1
    | .second => 0
  give _ f _ := match f with
    | .renewer => 2
    | .first => 0
    | .second => 0

/-- Each depends on the condition at need one; the first is active at the first four steps. -/
def web : Web Member Unit where
  level t _ := level t
  active t f := match f with
    | .renewer => True
    | .first => t < 4
    | .second => False
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ f _ := match f with
    | .renewer => False
    | .first => True
    | .second => False

theorem balances : flow.Balances web
  | 0, () => rfl
  | 1, () => rfl
  | 2, () => rfl
  | 3, () => rfl
  | _ + 4, () => rfl

theorem bounded : ∀ t, flow.given t () ≤ 2
  | 0 => Nat.le_refl 2
  | 1 => Nat.le_refl 2
  | 2 => Nat.le_refl 2
  | 3 => Nat.le_refl 2
  | _ + 4 => Nat.le_refl 2

theorem level_pos : ∀ t, 1 ≤ level t
  | 0 => Nat.le_add_left 1 2
  | 1 => Nat.le_add_left 1 3
  | 2 => Nat.le_add_left 1 3
  | 3 => Nat.le_add_left 1 2
  | _ + 4 => Nat.le_add_right 1 _

theorem dependent : web.Dependent :=
  fun t _ _ _ _ => level_pos t

theorem present_first : ∀ t, t < 4 → Witnesses.Member.first ∈ present t
  | 0, _ => .tail _ (.head _)
  | 1, _ => .tail _ (.head _)
  | 2, _ => .tail _ (.head _)
  | 3, _ => .tail _ (.head _)
  | _ + 4, lt => absurd lt (Nat.not_lt_of_le (Nat.le_add_left 4 _))

/-- While active, the first takes part with a take more than now. -/
theorem seeks : ∀ t, web.active t .first →
    Witnesses.Member.first ∈ flow.present t ∧ MoreThanNow id (fun s => flow.take s .first ()) t :=
  fun t active => ⟨present_first t active, Nat.lt_succ_self (t + 1)⟩

/-- The first's activity does not resume once it stops. -/
theorem lasting : ∀ i, web.active (0 + i + 1) .first → web.active (0 + i) .first :=
  fun _ active => Nat.lt_of_succ_lt active

/-- The first takes all that is given from step one while it takes part. -/
theorem takes_all : ∀ t, 1 ≤ t → t < 4 → flow.TakesAll t .first ()
  | 1, _, _ => ⟨present_first 1 (by decide), Nat.le_refl 2⟩
  | 2, _, _ => ⟨present_first 2 (by decide), Nat.le_succ 2⟩
  | 3, _, _ => ⟨present_first 3 (by decide), Nat.le_trans (Nat.le_succ 2) (Nat.le_succ 3)⟩
  | 0, early, _ => absurd early (Nat.not_succ_le_zero 0)
  | _ + 4, _, lt => absurd lt (Nat.not_lt_of_le (Nat.le_add_left 4 _))

/-- From step four the first is inactive. -/
theorem ends : ∀ k, ¬ web.active (4 + k) .first :=
  fun k => Nat.not_lt_of_le (Nat.le_add_right 4 k)

/-- The ending also follows from the law, from the window's end on. -/
theorem ends_by_law : ∀ k, ¬ web.active (0 + (2 + 1 + web.level (0 + (2 + 1)) () + k)) .first :=
  Flow.seeking_ends balances bounded seeks lasting

/-- **The course.** The renewer is active at every step; the first is active at the first four
steps, takes all that is given from step one, and is inactive from step four. -/
theorem course :
    flow.Balances web ∧ web.Dependent ∧ (∀ t, web.active t .renewer) ∧ (∀ t, t < 4 → web.active t .first) ∧
      (∀ t, 1 ≤ t → t < 4 → flow.TakesAll t .first ()) ∧ ∀ k, ¬ web.active (4 + k) .first :=
  ⟨balances, dependent, fun _ => trivial, fun _ lt => lt, takes_all, ends⟩

end Seeker

namespace Alone

/-- In `Alone` the first takes all that is given at every step and is active at every step. -/
theorem takes_all : ∀ t, flow.TakesAll t .first () ∧ web.active t .first :=
  fun _ => ⟨⟨.tail _ (.head _), Nat.le_refl 2⟩, trivial⟩

end Alone

end Becoming
