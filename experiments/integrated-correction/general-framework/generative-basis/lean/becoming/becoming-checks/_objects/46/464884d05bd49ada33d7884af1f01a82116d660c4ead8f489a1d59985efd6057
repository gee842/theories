import Becoming.Roles

/-!
# Reserve: activity beyond support, standing beyond activity

`Dependent` lets a formation be active only where the conditions it then depends on
support it, and `Embodied` lets a relatum stand as a condition only while it is active.
Both exclude what is held: buffers, reserves, lag and dormancy. This module states what
a reserve carries, and what generation bears where activity and standing are out of
step.

* **A reserve.** A reserve is an amount for each formation that does not rise across a
  step at which the formation is unsupported, and falls across each such step at which
  it is active (`Web.Carries`). `Dependent` is exactly the zero reserve
  (`carries_zero`): relaxing it means a positive reserve, not activity outside
  dependence.
* **A reserve is a held condition.** In a balanced flow, a condition that nothing gives
  to while its holder is unsupported, and that its holder takes from while active there,
  carries the holder, its standing being the reserve (`Flow.carries_of_held`). An active
  formation whose dependences fail has a positive reserve (`Carries.pos`), so a
  dependence on what it holds, at need one, is met. The same unfolding can then be read
  with the dependence transformed onto the held condition, under `Dependent`
  (`Famine.transformed_dependent`).
* **A reserve defers the end and does not escape it.** A formation unsupported from some
  step on is active only finitely often (`Carries.active_finitely`), and over any stretch
  at most as often as its reserve at the start (`Carries.lasts`, `Carries.lasts_within`).
  So after a loss without return with the dependence unchanged
  (`Carries.consumed_lasts`), and after the end of an embodied relatum it depends on at a
  positive need (`Carries.coextinct_lasts`), a formation is active beyond its support at
  most as often as its reserve: lagged ending and lagged coextinction. Dormancy defers
  the end the same way: unsupported, a formation arises only finitely often
  (`Carries.arising_finitely`), and a reserve that decays while dormant, as a seed's
  viability, bounds the time as well (`Web.Decays`, `Carries.ends_within`). The bounds
  are attained, with their premises, by a seed waking twice in the dark on its reserve
  (`Seed`), by a seed waking once before its viability is spent (`Viable`) and by a fox
  outliving the hare by its fat (`Famine`).
* **Standing beyond activity.** Generation bears replenishment where a relatum comes to
  stand (`Becoming.Flow`, `Becoming.Dissipation`); an embodied relatum comes to stand as
  it arises (`Becoming.Roles`). A relatum that stands while it is active, and did not
  stand at some earlier step, came to stand across some step in between, perhaps long
  before it is active (`came_to_stand`): a seed is given its standing while dormant and
  arises later with nothing given to it (`Provisioned`). Waking from dormancy is arising without coming to stand, and nothing
  need be given to it, though the relatum stands as a condition throughout (`Sleeper`).

A reserve, like `Dependent`, is a premise supplied by the representation; which
condition a formation holds is supplied by the application. That what is held is finite
is the physical content. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {F C : Type}

namespace Web

variable (W : Web F C)

/-- A reserve `r` *carries* activity beyond support: across a step at which a formation is
not supported, its reserve does not rise, and it falls if the formation is active there. -/
def Carries (r : Nat → F → Nat) : Prop :=
  ∀ t f, ¬ W.Supported t f → r (t + 1) f ≤ r t f ∧ (W.active t f → r (t + 1) f < r t f)

/-- A reserve `r` *decays* when it falls across every step at which its formation is not
supported and it is positive, whether or not the formation is active there: a seed's
viability. -/
def Decays (r : Nat → F → Nat) : Prop :=
  ∀ t f, ¬ W.Supported t f → 0 < r t f → r (t + 1) f < r t f

variable {W} {r : Nat → F → Nat}

/-- `Dependent` is exactly the zero reserve. -/
theorem carries_zero : W.Carries (fun _ _ => 0) ↔ W.Dependent :=
  ⟨fun carries t f active c depends => Nat.ge_of_not_lt fun short => Nat.lt_irrefl 0
      ((carries t f fun supported => Nat.not_le_of_gt short (supported c depends)).2 active),
   fun dependent _ _ unsupported =>
      ⟨Nat.le_refl 0, fun active => absurd (dependent _ _ active) unsupported⟩⟩

/-- An active formation whose dependences fail has a positive reserve. -/
theorem Carries.pos (carries : W.Carries r) {t : Nat} {f : F} (active : W.active t f)
    (unsupported : ¬ W.Supported t f) : 0 < r t f :=
  Nat.lt_of_le_of_lt (Nat.zero_le _) ((carries t f unsupported).2 active)

/-- Unsupported from step `T` on, a formation is active only finitely often. -/
theorem Carries.active_finitely (carries : W.Carries r) {f : F} {T : Nat}
    (unsupported : ∀ t, T ≤ t → ¬ W.Supported t f) : ¬ ∀ N, ∃ t, N ≤ t ∧ W.active t f :=
  fun recurs => falls_finitely (fun t => r t f) T
    (fun t later => (carries t f (unsupported t later)).1)
    fun N => match recurs (N + T) with
      | ⟨t, later, active⟩ => ⟨t, Nat.le_trans (Nat.le_add_right N T) later,
          (carries t f (unsupported t (Nat.le_trans (Nat.le_add_left T N) later))).2 active⟩

/-- Across an unsupported step, the reserve falls by at least one if the formation is
active. -/
theorem Carries.step (carries : W.Carries r) {t : Nat} {f : F} [Decidable (W.active t f)]
    (unsupported : ¬ W.Supported t f) : r (t + 1) f + mark (W.active t f) ≤ r t f :=
  mark_cases (q := fun m => r (t + 1) f + m ≤ r t f) (carries t f unsupported).2
    fun _ => (carries t f unsupported).1

/-- Unsupported from step `S` on, a formation is active over any stretch of steps from
`S` at most as often as its reserve at `S`. -/
theorem Carries.lasts (carries : W.Carries r) {f : F} [∀ t, Decidable (W.active t f)] :
    ∀ S N, (∀ t, S ≤ t → ¬ W.Supported t f) →
      r (S + N) f + total (steps S N) (fun t => mark (W.active t f)) ≤ r S f
  | _, 0, _ => Nat.le_refl _
  | S, N + 1, unsupported =>
    have later := carries.lasts (S + 1) N fun t after => unsupported t (Nat.le_of_succ_le after)
    Nat.le_trans
      (Nat.le_of_eq ((Nat.add_left_comm _ _ _).trans (congrArg
        (fun n => mark (W.active S f) + (r n f + total (steps (S + 1) N) fun t =>
          mark (W.active t f)))
        (Nat.add_right_comm S 1 N).symm)))
      (Nat.le_trans (Nat.add_le_add_left later _)
        (Nat.le_trans (Nat.le_of_eq (Nat.add_comm _ _))
          (carries.step (unsupported S (Nat.le_refl S)))))

/-- With a reserve of capacity `k`, a formation unsupported from some step on is active
over any later stretch at most `k` times. -/
theorem Carries.lasts_within (carries : W.Carries r) {f : F} [∀ t, Decidable (W.active t f)]
    {k : Nat} (capacity : ∀ t, r t f ≤ k) (S N : Nat)
    (unsupported : ∀ t, S ≤ t → ¬ W.Supported t f) :
    total (steps S N) (fun t => mark (W.active t f)) ≤ k :=
  Nat.le_trans (Nat.le_trans (Nat.le_add_left _ _) (carries.lasts S N unsupported))
    (capacity S)

/-- Unsupported from step `T` on, a formation arises only finitely often: dormancy defers
the end and does not escape it. -/
theorem Carries.arising_finitely (carries : W.Carries r) {f : F} {T : Nat}
    (unsupported : ∀ t, T ≤ t → ¬ W.Supported t f) : ¬ ∀ N, ∃ t, N ≤ t ∧ W.Arises t f :=
  fun arising => carries.active_finitely unsupported fun N => match arising N with
    | ⟨t, later, arises⟩ => ⟨t + 1, Nat.le_succ_of_le later, arises.2⟩

/-- Unsupported from step `S` on, a carried reserve that decays has, after `n` steps, fallen
by `n` or been spent. -/
theorem Carries.decays_by (carries : W.Carries r) (decays : W.Decays r) {f : F} {S : Nat}
    (unsupported : ∀ t, S ≤ t → ¬ W.Supported t f) :
    ∀ n, r (S + n) f + n ≤ r S f ∨ r (S + n) f = 0
  | 0 => .inl (Nat.le_refl _)
  | n + 1 =>
    have step := carries (S + n) f (unsupported (S + n) (Nat.le_add_right S n))
    have spent (empty : r (S + n) f = 0) : r (S + n + 1) f = 0 :=
      Nat.le_antisymm (Nat.le_trans step.1 (Nat.le_of_eq empty)) (Nat.zero_le _)
    match carries.decays_by decays unsupported n, Nat.eq_zero_or_pos (r (S + n) f) with
    | .inr empty, _ => .inr (spent empty)
    | .inl _, .inl empty => .inr (spent empty)
    | .inl fell, .inr left => .inl (Nat.le_trans
        (Nat.le_of_eq (Nat.add_right_comm (r (S + n + 1) f) 1 n).symm)
        (Nat.le_trans (Nat.add_le_add_right (Nat.succ_le_of_lt
          (decays (S + n) f (unsupported (S + n) (Nat.le_add_right S n)) left)) n) fell))

/-- Bounded dormancy: unsupported from step `S` on, a formation whose carried reserve decays
is not active once as many steps have passed as its reserve at `S`. -/
theorem Carries.ends_within (carries : W.Carries r) (decays : W.Decays r) {f : F} {S : Nat}
    (unsupported : ∀ t, S ≤ t → ¬ W.Supported t f) {n : Nat} (spent : r S f ≤ n) :
    ¬ W.active (S + n) f :=
  fun active =>
    have left := carries.pos active (unsupported (S + n) (Nat.le_add_right S n))
    match carries.decays_by decays unsupported n with
    | .inl fell => Nat.not_le_of_gt (Nat.lt_add_of_pos_left left)
        (Nat.le_trans fell (Nat.le_trans spent (Nat.le_refl n)))
    | .inr empty => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le left (Nat.le_of_eq empty))

/-- After a loss without return with the dependence unchanged, a formation is not supported
at any later step. -/
theorem unsupported_after_loss {T : Nat} {g : F} {c : C}
    (fixed : ∀ t, T < t → W.requires t g c ∧ W.need T g c ≤ W.need t g c)
    (below : ∀ t, T < t → W.level t c < W.need T g c) : ∀ t, T < t → ¬ W.Supported t g :=
  fun t later supported => Nat.not_le_of_gt (below t later)
    (Nat.le_trans (fixed t later).2 (supported c (fixed t later).1))

/-- Lagged ending: after a loss without return with the dependence unchanged, a formation
with a reserve is active only finitely often, at most as often as its reserve after the
loss (`Carries.lasts`). Under `Dependent`, the zero reserve, it is not active at all
(`consumed_ends_when_fixed`). -/
theorem Carries.consumed_lasts (carries : W.Carries r) {T : Nat} {g : F} {c : C}
    (fixed : ∀ t, T < t → W.requires t g c ∧ W.need T g c ≤ W.need t g c)
    (below : ∀ t, T < t → W.level t c < W.need T g c) : ¬ ∀ N, ∃ t, N ≤ t ∧ W.active t g :=
  carries.active_finitely (T := T + 1) (unsupported_after_loss fixed below)

end Web

/-! ## A reserve is a held condition -/

namespace Flow

variable {L : Flow F C} {W : Web F C}

/-- In a balanced flow, a condition that nothing gives to while its holder is unsupported,
and that its holder takes from while active there, carries the holder: its standing is the
holder's reserve. -/
theorem carries_of_held (balances : L.Balances W) (hold : F → C)
    (unreplenished : ∀ t f, ¬ W.Supported t f → L.given t (hold f) = 0)
    (drawn : ∀ t f, ¬ W.Supported t f → W.active t f → 0 < L.taken t (hold f)) :
    W.Carries fun t f => W.level t (hold f) :=
  fun t f unsupported =>
    have balance : W.level (t + 1) (hold f) + L.taken t (hold f) = W.level t (hold f) :=
      (balances t (hold f)).trans
        (congrArg (W.level t (hold f) + ·) (unreplenished t f unsupported))
    ⟨Nat.le_trans (Nat.le_add_right _ _) (Nat.le_of_eq balance),
     fun active => Nat.lt_of_lt_of_le
       (Nat.lt_add_of_pos_right (drawn t f unsupported active)) (Nat.le_of_eq balance)⟩

end Flow

/-! ## One kind of relatum -/

namespace Web

variable {X : Type} {W : Web X X}

/-- After an embodied relatum ends, a formation depending on it at a positive need is not
supported. -/
theorem unsupported_after_end {y g : X} (embodied : W.Embodied y) {T : Nat}
    (bears : ∀ t, T ≤ t → W.requires t g y ∧ 0 < W.need t g y)
    (ended : ∀ t, T ≤ t → ¬ W.active t y) : ∀ t, T ≤ t → ¬ W.Supported t g :=
  fun t later supported => ended t later ((embodied t).mpr
    (Nat.lt_of_lt_of_le (bears t later).2 (supported y (bears t later).1)))

/-- Lagged coextinction: after an embodied relatum ends, a formation depending on it at a
positive need, with a reserve, is active only finitely often, at most as often as its
reserve when the relatum ended (`Carries.lasts`). Under `Dependent` it ends with it
(`coextinct`). -/
theorem Carries.coextinct_lasts {r : Nat → X → Nat} (carries : W.Carries r) {y g : X}
    (embodied : W.Embodied y) {T : Nat}
    (bears : ∀ t, T ≤ t → W.requires t g y ∧ 0 < W.need t g y)
    (ended : ∀ t, T ≤ t → ¬ W.active t y) : ¬ ∀ N, ∃ t, N ≤ t ∧ W.active t g :=
  carries.active_finitely (unsupported_after_end embodied bears ended)

/-- A relatum standing while it is active, without standing at `T` and active at a later
`t`, came to stand across some step between them. -/
theorem came_to_stand {x : X} (stands : ∀ t, W.active t x → 0 < W.level t x) {T t : Nat}
    (le : T ≤ t) (absent : ¬ 0 < W.level T x) (active : W.active t x) :
    ¬ ∀ s, T ≤ s → s < t → ¬ W.ComesToStand s x :=
  arises_at_a_step (p := fun s => 0 < W.level s x) le absent (stands t active)

end Web

/-! ## Witnesses -/

namespace Seed

/-- Awake at steps one and three. -/
def wake : Nat → Nat
  | 1 => 1
  | 3 => 1
  | _ => 0

/-- Two units until the seed first wakes, one until it wakes again, then none. -/
def reserve : Nat → Nat
  | 0 => 2
  | 1 => 2
  | 2 => 1
  | 3 => 1
  | _ => 0

/-- A seed in the dark, depending on light at need one, awake at steps one and three. -/
def web : Web Unit Unit where
  level _ _ := 0
  active t _ := 0 < wake t
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ _ _ := False

instance decAwake (t : Nat) : Decidable (web.active t ()) := Nat.decLt 0 (wake t)

/-- The seed is never supported. -/
theorem dark (t : Nat) : ¬ web.Supported t () :=
  fun supported => Nat.not_succ_le_zero 0 (supported () trivial)

/-- The reserve carries the seed. -/
theorem carries : web.Carries fun t _ => reserve t
  | 0, (), _ => ⟨Nat.le_refl 2, fun awake => absurd awake (Nat.lt_irrefl 0)⟩
  | 1, (), _ => ⟨Nat.le_succ 1, fun _ => Nat.lt_succ_self 1⟩
  | 2, (), _ => ⟨Nat.le_refl 1, fun awake => absurd awake (Nat.lt_irrefl 0)⟩
  | 3, (), _ => ⟨Nat.zero_le 1, fun _ => Nat.zero_lt_one⟩
  | _ + 4, (), _ => ⟨Nat.le_refl 0, fun awake => absurd awake (Nat.lt_irrefl 0)⟩

/-- Dormant and awake by turns in the dark, the seed arises twice and then never: it is not
`Dependent`, its reserve carries it, and it is awake exactly as often as its reserve at
the start. -/
theorem seed : ¬ web.Dependent ∧ web.Carries (fun t _ => reserve t) ∧
    web.Arises 0 () ∧ web.Arises 2 () ∧ (∀ t, ¬ web.active (t + 4) ()) ∧
    total (steps 0 4) (fun t => mark (web.active t ())) = reserve 0 :=
  ⟨fun dependent => dark 1 (dependent 1 () Nat.zero_lt_one), carries,
   ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩, ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩,
   fun _ awake => Nat.lt_irrefl 0 awake, rfl⟩

/-- The seed's reserve does not decay: it keeps both units while the seed is dormant at
step zero. -/
theorem not_decays : ¬ web.Decays fun t _ => reserve t :=
  fun decays => Nat.lt_irrefl 2 (decays 0 () (dark 0) (Nat.succ_pos 1))

end Seed

namespace Viable

/-- Viability: three units, falling by one at every step until none is left. -/
def viability : Nat → Nat
  | 0 => 3
  | 1 => 2
  | 2 => 1
  | _ => 0

/-- A seed in the dark, depending on light at need one, awake only at step two. -/
def web : Web Unit Unit where
  level _ _ := 0
  active t _ := t = 2
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ _ _ := False

/-- The seed is never supported. -/
theorem dark (t : Nat) : ¬ web.Supported t () :=
  fun supported => Nat.not_succ_le_zero 0 (supported () trivial)

/-- Its viability carries it. -/
theorem carries : web.Carries fun t _ => viability t
  | 0, (), _ => ⟨Nat.le_succ 2, fun _ => Nat.lt_succ_self 2⟩
  | 1, (), _ => ⟨Nat.le_succ 1, fun _ => Nat.lt_succ_self 1⟩
  | 2, (), _ => ⟨Nat.zero_le 1, fun _ => Nat.zero_lt_one⟩
  | _ + 3, (), _ => ⟨Nat.le_refl 0, fun awake => absurd awake (Nat.ne_of_gt
      (Nat.lt_of_lt_of_le (Nat.lt_succ_self 2) (Nat.le_add_left 3 _)))⟩

/-- Its viability decays. -/
theorem decays : web.Decays fun t _ => viability t
  | 0, (), _, _ => Nat.lt_succ_self 2
  | 1, (), _, _ => Nat.lt_succ_self 1
  | 2, (), _, _ => Nat.zero_lt_one
  | _ + 3, (), _, positive => absurd positive (Nat.lt_irrefl 0)

/-- Dormant in the dark on a decaying reserve of three, the seed wakes at step two and never
after: it is not `Dependent`, and it is inactive from the step its viability is spent, so
the bound of `Carries.ends_within` is attained. -/
theorem viable : ¬ web.Dependent ∧ web.Carries (fun t _ => viability t) ∧
    web.Decays (fun t _ => viability t) ∧ web.Arises 1 () ∧ ∀ t, ¬ web.active (t + 3) () :=
  ⟨fun dependent => dark 2 (dependent 2 () rfl), carries, decays,
   ⟨fun awake => Nat.succ_ne_self 1 awake.symm, rfl⟩,
   fun t awake => Nat.ne_of_gt (Nat.lt_of_lt_of_le (Nat.lt_succ_self 2) (Nat.le_add_left 3 t))
     awake⟩

end Viable

namespace Famine

/-- A hare, a fox, and the fox's fat. -/
inductive Relatum where
  | hare
  | fox
  | fat

/-- The hare stands at step zero only. -/
def hare : Nat → Nat
  | 0 => 1
  | _ => 0

/-- The fat stands at two units through step one, at one at step two, then at none. -/
def fat : Nat → Nat
  | 0 => 2
  | 1 => 2
  | 2 => 1
  | _ => 0

/-- The fox eats the hare across step zero. -/
def eats : Nat → Nat
  | 0 => 1
  | _ => 0

/-- The fox burns a unit of fat across steps one and two. -/
def burns : Nat → Nat
  | 1 => 1
  | 2 => 1
  | _ => 0

/-- The fox takes part through step two. -/
def present : Nat → List Relatum
  | 0 => [.fox]
  | 1 => [.fox]
  | 2 => [.fox]
  | _ => []

/-- The hare is active exactly while it stands; the fox, through step two, depends on the
hare at need one and draws on the hare and its fat; the fat is never active. -/
def web : Web Relatum Relatum where
  level t x := match x with
    | .hare => hare t
    | .fox => 0
    | .fat => fat t
  active t x := match x with
    | .hare => 0 < hare t
    | .fox => t < 3
    | .fat => False
  requires _ g y := g = .fox ∧ y = .hare
  need _ _ _ := 1
  draws _ g y := g = .fox ∧ (y = .hare ∨ y = .fat)

/-- The fox eats the hare, then burns its fat. -/
def flow : Flow Relatum Relatum where
  present := present
  take t g y := match g, y with
    | .fox, .hare => eats t
    | .fox, .fat => burns t
    | .fox, .fox => 0
    | .hare, _ => 0
    | .fat, _ => 0
  give _ _ _ := 0

/-- Each relatum holds itself, except the fox, which holds its fat. -/
def hold : Relatum → Relatum
  | .hare => .hare
  | .fox => .fat
  | .fat => .fat

theorem balances : flow.Balances web
  | 0, .hare | 0, .fox | 0, .fat => rfl
  | 1, .hare | 1, .fox | 1, .fat => rfl
  | 2, .hare | 2, .fox | 2, .fat => rfl
  | _ + 3, .hare | _ + 3, .fox | _ + 3, .fat => rfl

/-- Only the fox depends on anything. -/
theorem supported_of_ne_fox {t : Nat} : (x : Relatum) → ¬ x = .fox → web.Supported t x
  | .hare, _ => fun _ depends => nomatch depends.1
  | .fat, _ => fun _ depends => nomatch depends.1
  | .fox, ne => absurd rfl ne

/-- The fox is supported at step zero, while the hare stands. -/
theorem fed : web.Supported 0 .fox :=
  fun _ depends => Eq.subst (motive := fun y => 1 ≤ web.level 0 y) depends.2.symm
    (Nat.le_refl 1)

/-- The fat carries the fox: the flow balances, nothing gives to the fat, and the fox takes
from it at each unsupported active step. -/
theorem carries : web.Carries fun t x => web.level t (hold x) :=
  Flow.carries_of_held balances hold (fun _ _ _ => total_zero _) fun t x unsupported active =>
    match x, t, unsupported, active with
    | .hare, _, unsupported, _ =>
      absurd (supported_of_ne_fox .hare fun same => nomatch same) unsupported
    | .fat, _, unsupported, _ =>
      absurd (supported_of_ne_fox .fat fun same => nomatch same) unsupported
    | .fox, 0, unsupported, _ => absurd fed unsupported
    | .fox, 1, _, _ => Nat.zero_lt_one
    | .fox, 2, _, _ => Nat.zero_lt_one
    | .fox, _ + 3, _, active => absurd active (Nat.not_lt_of_le (Nat.le_add_left 3 _))

/-- The hare is embodied. -/
theorem hare_embodied : web.Embodied .hare :=
  fun _ => Iff.rfl

/-- What the fox depends on: the hare at step zero, its fat after. -/
def source : Nat → Relatum
  | 0 => .hare
  | _ => .fat

/-- The same unfolding read with the fox's dependence transformed onto its fat once the
hare is gone. -/
def transformed : Web Relatum Relatum :=
  { web with requires := fun t g y => g = .fox ∧ y = source t }

/-- Read so, activity needs support: the fox's lag is its dependence transformed onto the
condition it holds. -/
theorem transformed_dependent : transformed.Dependent
  | 0, .fox, _ => fun _ depends => Eq.subst (motive := fun y => 1 ≤ transformed.level 0 y)
      depends.2.symm (Nat.le_refl 1)
  | 1, .fox, _ => fun _ depends => Eq.subst (motive := fun y => 1 ≤ transformed.level 1 y)
      depends.2.symm (Nat.le_succ 1)
  | 2, .fox, _ => fun _ depends => Eq.subst (motive := fun y => 1 ≤ transformed.level 2 y)
      depends.2.symm (Nat.le_refl 1)
  | _ + 3, .fox, active => absurd active (Nat.not_lt_of_le (Nat.le_add_left 3 _))
  | _, .hare, _ => fun _ depends => nomatch depends.1
  | _, .fat, _ => fun _ depends => nomatch depends.1

instance decActive (t : Nat) : Decidable (web.active t .fox) := Nat.decLt t 3

/-- Lagged coextinction: the fox depends on the embodied hare, which ends after step zero.
The fox is not `Dependent`; its fat carries it, and it outlives the hare by exactly the
two units of its fat. Read with its dependence moved onto the fat, the same unfolding is
`Dependent`. -/
theorem famine : ¬ web.Dependent ∧ web.Carries (fun t x => web.level t (hold x)) ∧
    web.Embodied .hare ∧ (∀ t, 1 ≤ t → ¬ web.active t .hare) ∧
    (∀ t, 1 ≤ t → web.requires t .fox .hare ∧ 0 < web.need t .fox .hare) ∧
    web.active 2 .fox ∧ (∀ t, 3 ≤ t → ¬ web.active t .fox) ∧
    total (steps 1 2) (fun t => mark (web.active t .fox)) = web.level 1 (hold .fox) ∧
    transformed.Dependent :=
  ⟨fun dependent => Nat.not_succ_le_zero 0
      (dependent 1 .fox (Nat.le_succ 2) .hare ⟨rfl, rfl⟩),
   carries, hare_embodied,
   fun t later => match t, later with
     | 0, later => absurd later (Nat.not_succ_le_zero 0)
     | _ + 1, _ => Nat.lt_irrefl 0,
   fun _ _ => ⟨⟨rfl, rfl⟩, Nat.zero_lt_one⟩,
   Nat.lt_succ_self 2,
   fun _ later => Nat.not_lt_of_le later, rfl, transformed_dependent⟩

end Famine

namespace Sleeper

/-- One relatum standing at one throughout, awake at odd steps. -/
def web : Web Unit Unit where
  level _ _ := 1
  active t _ := 0 < Handing.stands false t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- Nothing takes part. -/
def flow : Flow Unit Unit := ⟨fun _ => [], fun _ _ _ => 0, fun _ _ _ => 0⟩

/-- Waking from dormancy is arising without coming to stand: the relatum stands as a
condition throughout and while active, the flow, in which nothing takes part, balances
and is dissipative, activity needs support, and generation is unceasing with nothing
given. The relatum is not embodied, since it stands while dormant, and never comes to
stand. -/
theorem sleeper : flow.Balances web ∧ flow.Dissipative ∧ web.Dependent ∧ web.Unceasing ∧
    (∀ t, web.active t () → 0 < web.level t ()) ∧ ¬ web.Embodied () ∧
    ∀ t, ¬ web.ComesToStand t () :=
  ⟨fun _ _ => rfl, fun _ _ _ _ _ present => (nomatch present),
   fun _ _ _ _ depends => (nomatch depends),
   fun N => match Handing.recurs false N with
    | ⟨t, later, arises⟩ => ⟨t, (), later, arises⟩,
   fun _ _ => Nat.zero_lt_one,
   fun embodied => Nat.lt_irrefl 0 ((embodied 0).mpr Nat.zero_lt_one),
   fun _ comes => comes.1 Nat.zero_lt_one⟩

end Sleeper

namespace Provisioned

/-- A parent and a seed. -/
inductive Relatum where
  | parent
  | seed

/-- Active from step two on. -/
def late : Nat → Nat
  | 0 => 0
  | 1 => 0
  | _ => 1

/-- The seed stands from step one and is active from step two; the parent is always
active. Nothing depends on or draws on anything. -/
def web : Web Relatum Relatum where
  level t x := match x with
    | .parent => 0
    | .seed => SunSeed.sprout t
  active t x := match x with
    | .parent => True
    | .seed => 0 < late t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- One unit at step zero. -/
def gift : Nat → Nat
  | 0 => 1
  | _ => 0

/-- The parent gives the seed one unit across step zero. -/
def flow : Flow Relatum Relatum where
  present _ := [.parent]
  take _ _ _ := 0
  give t g y := match g, y with
    | .parent, .seed => gift t
    | .parent, .parent => 0
    | .seed, _ => 0

theorem balances : flow.Balances web
  | 0, .parent | 0, .seed => rfl
  | _ + 1, .parent | _ + 1, .seed => rfl

/-- Only the parent gives, and it is always active. -/
theorem acting : flow.Acting web
  | _, .parent, _, _, _ => trivial
  | _, .seed, _, _, gives => absurd gives (Nat.lt_irrefl 0)

/-- Provisioning: the seed comes to stand across step zero, given its standing by the
parent while it is dormant, and arises across step one with nothing given to it. It
stands while active, and is not embodied. -/
theorem provisioned : flow.Balances web ∧ flow.Acting web ∧
    web.ComesToStand 0 .seed ∧ web.level 1 .seed ≤ flow.given 0 .seed ∧
    web.Arises 1 .seed ∧ flow.given 1 .seed = 0 ∧
    (∀ t, web.active t .seed → 0 < web.level t .seed) ∧ ¬ web.Embodied .seed :=
  ⟨balances, acting, ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩, Nat.le_refl 1,
   ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩, rfl,
   fun t active => match t, active with
     | 0, active => absurd active (Nat.lt_irrefl 0)
     | 1, active => absurd active (Nat.lt_irrefl 0)
     | _ + 2, _ => Nat.zero_lt_one,
   fun embodied => Nat.lt_irrefl 0 ((embodied 1).mpr Nat.zero_lt_one)⟩

end Provisioned

end Becoming
