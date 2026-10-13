import Becoming.Response

/-!
# Response through exchanges in their order

Two courses of one native Flow/Web description, with common initial levels and
the same present formations. A declared source may differ at specified steps;
the rest responds through its past registration. Spread is a potential route,
not an assertion of actual influence or reliable control. A response exchange
at t can first affect levels at t+1. No physical duration is assigned to a step.
-/
namespace Becoming
namespace TimedResponse

open Generative

variable {F C : Type}

/-- An exchange at the named step in either course, on their common present list.
Equality of those lists is a separate hypothesis of the application theorem. -/
def TouchesAt (L L' : Flow F C) (t : Nat) (h : F) (c : C) : Prop :=
  h ∈ L.present t ∧
    (0 < L.take t h c ∨ 0 < L.give t h c ∨
      0 < L'.take t h c ∨ 0 < L'.give t h c)

/-- Potential propagation, retaining the order of exchanges and past registration.
There is no initial source: differences already present must be handled separately. -/
inductive Spread (L L' : Flow F C) (W : Web F C)
    (obs : F → C → Prop) (source : Nat → F → Prop) : Nat → C → Prop
  | hold {t c} : Spread L L' W obs source t c → Spread L L' W obs source (t+1) c
  | input {t h c} : source t h → TouchesAt L L' t h c →
      Spread L L' W obs source (t+1) c
  | response {s t h c d} : Spread L L' W obs source s d → s ≤ t →
      W.Registers obs h d → TouchesAt L L' t h c →
      Spread L L' W obs source (t+1) c

/-- A potential source route has entered something the reader registers by T. -/
def ReachedBy (L L' : Flow F C) (W : Web F C) (obs : F → C → Prop)
    (source : Nat → F → Prop) (g : F) (T : Nat) : Prop :=
  ∃ s c, s ≤ T ∧ W.Registers obs g c ∧ Spread L L' W obs source s c

variable {L L' : Flow F C} {W W' : Web F C}
    {obs : F → C → Prop} {source : Nat → F → Prop}

theorem not_spread_zero (c : C) : ¬ Spread L L' W obs source 0 c :=
  fun spread => nomatch spread

/-- A route by T includes an actual source step strictly before T. -/
theorem Spread.has_earlier_source {t : Nat} {c : C}
    (spread : Spread L L' W obs source t c) : ∃ s h, s < t ∧ source s h := by
  induction spread with
  | hold _ ih =>
      rcases ih with ⟨s, h, before, src⟩
      exact ⟨s, h, Nat.lt_trans before (Nat.lt_succ_self _), src⟩
  | input src _ => exact ⟨_, _, Nat.lt_succ_self _, src⟩
  | response _ earlier _ _ ih =>
      rcases ih with ⟨s, h, before, src⟩
      exact ⟨s, h, Nat.lt_succ_of_lt (Nat.lt_of_lt_of_le before earlier), src⟩

theorem not_reached_before_source {g : F} {T : Nat}
    (later : ∀ s h, s < T → ¬ source s h) : ¬ ReachedBy L L' W obs source g T :=
  fun ⟨_, _, within, _, spread⟩ =>
    match spread.has_earlier_source with
    | ⟨r, h, before, src⟩ => later r h (Nat.lt_of_lt_of_le before within) src

theorem reachedBy_mono {g : F} {T U : Nat} (le : T ≤ U)
    (reached : ReachedBy L L' W obs source g T) : ReachedBy L L' W obs source g U :=
  match reached with
  | ⟨s, c, before, reg, spread⟩ => ⟨s, c, Nat.le_trans before le, reg, spread⟩

/-- Equality of registered levels suffices for the native registration, including support. -/
theorem registration_of_levels {h : F} {l l' : Nat → C → Nat} {t : Nat}
    (same : ∀ c, W.Registers obs h c → l t c = l' t c) :
    W.RegistersAlike obs h l l' t :=
  ⟨⟨fun admits c requires => Nat.le_trans (admits c requires)
      (Nat.le_of_eq (same c (.inl ⟨t, requires⟩))),
    fun admits c requires => Nat.le_trans (admits c requires)
      (Nat.le_of_eq (same c (.inl ⟨t, requires⟩)).symm)⟩,
   fun c observed => same c (.inr observed)⟩

/-- Deadline-local blindness. Only balances, presence and response before D are
required; arbitrary later changes are admitted. The initial levels agree globally. -/
theorem levels_alike_before {D : Nat}
    (balanced : ∀ t, t < D → ∀ c,
      W.level (t+1) c + L.taken t c = W.level t c + L.given t c)
    (balanced' : ∀ t, t < D → ∀ c,
      W'.level (t+1) c + L'.taken t c = W'.level t c + L'.given t c)
    (present : ∀ t, t < D → L.present t = L'.present t)
    (start : ∀ c, W.level 0 c = W'.level 0 c)
    (responds : ∀ t, t < D → ∀ h, ¬ source t h →
      W.RegistersAlikeUpTo obs h W.level W'.level t →
      ∀ c, L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c) :
    ∀ t, t ≤ D → ∀ c, ¬ Spread L L' W obs source t c →
      W.level t c = W'.level t c := by
  intro t
  induction t using Nat.strongRecOn with
  | ind t ih =>
    intro within c outside
    cases t with
    | zero => exact start c
    | succ t =>
      have before : t < D := Nat.lt_of_lt_of_le (Nat.lt_succ_self t) within
      have earlier : ∀ s, s ≤ t → ∀ d,
          ¬ Spread L L' W obs source s d → W.level s d = W'.level s d :=
        fun s le => ih s (Nat.lt_succ_of_le le) (Nat.le_trans le (Nat.le_of_lt before))
      have each : ∀ h, h ∈ L.present t →
          L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c := by
        intro h mem
        have response : TouchesAt L L' t h c →
            L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c := by
          intro touch
          apply responds t before h (fun src => outside (.input src touch))
          intro s le
          apply registration_of_levels
          intro d reg
          exact earlier s le d (fun spread => outside (.response spread le reg touch))
        exact match Nat.decLt 0 (L.take t h c), Nat.decLt 0 (L.give t h c),
            Nat.decLt 0 (L'.take t h c), Nat.decLt 0 (L'.give t h c) with
          | isTrue pos, _, _, _ => response ⟨mem, .inl pos⟩
          | _, isTrue pos, _, _ => response ⟨mem, .inr (.inl pos)⟩
          | _, _, isTrue pos, _ => response ⟨mem, .inr (.inr (.inl pos))⟩
          | _, _, _, isTrue pos => response ⟨mem, .inr (.inr (.inr pos))⟩
          | isFalse a, isFalse b, isFalse a', isFalse b' =>
            ⟨(eq_zero_of_not_pos a).trans (eq_zero_of_not_pos a').symm,
             (eq_zero_of_not_pos b).trans (eq_zero_of_not_pos b').symm⟩
      have taken : L.taken t c = L'.taken t c :=
        (total_congr_on fun h mem => (each h mem).1).trans
          (congrArg (fun fs => total fs fun h => L'.take t h c) (present t before))
      have given : L.given t c = L'.given t c :=
        (total_congr_on fun h mem => (each h mem).2).trans
          (congrArg (fun fs => total fs fun h => L'.give t h c) (present t before))
      have now := earlier t (Nat.le_refl t) c (fun spread => outside (.hold spread))
      exact add_right_cancel (L.taken t c)
        ((balanced t before c).trans
          ((congrArg (· + L.given t c) now).trans
            ((congrArg (W'.level t c + ·) given).trans
              ((balanced' t before c).symm.trans
                (congrArg (W'.level (t+1) c + ·) taken.symm)))))

section Deadline
variable {D : Nat}
    (balanced : ∀ t, t < D → ∀ c,
      W.level (t+1) c + L.taken t c = W.level t c + L.given t c)
    (balanced' : ∀ t, t < D → ∀ c,
      W'.level (t+1) c + L'.taken t c = W'.level t c + L'.given t c)
    (present : ∀ t, t < D → L.present t = L'.present t)
    (start : ∀ c, W.level 0 c = W'.level 0 c)
    (responds : ∀ t, t < D → ∀ h, ¬ source t h →
      W.RegistersAlikeUpTo obs h W.level W'.level t →
      ∀ c, L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c)

include balanced balanced' present start responds

theorem registration_alike_before {g : F}
    (unreached : ¬ ReachedBy L L' W obs source g D) :
    W.RegistersAlikeUpTo obs g W.level W'.level D :=
  fun s le => registration_of_levels fun c reg =>
    levels_alike_before balanced balanced' present start responds s le c
      (fun spread => unreached ⟨s, c, le, reg, spread⟩)

/-- Any output type is admitted. Factoring through complete registration is supplied. -/
theorem answer_alike_before {A : Type} {g : F}
    (read : (Nat → C → Nat) → A)
    (through : ∀ l l', W.RegistersAlikeUpTo obs g l l' D → read l = read l')
    (unreached : ¬ ReachedBy L L' W obs source g D) : read W.level = read W'.level :=
  through _ _ (registration_alike_before balanced balanced' present start responds unreached)

/-- Constructive necessity: different outputs rule out absence of a timely route. -/
theorem different_answers_not_unreached {A : Type} {g : F}
    (read : (Nat → C → Nat) → A)
    (through : ∀ l l', W.RegistersAlikeUpTo obs g l l' D → read l = read l')
    (different : read W.level ≠ read W'.level) : ¬ ¬ ReachedBy L L' W obs source g D :=
  fun unreached => different
    (answer_alike_before balanced balanced' present start responds read through unreached)

/-- With an explicit decision of the potential route, necessity gives membership. -/
theorem different_answers_require_reached {A : Type} {g : F}
    [decided : Decidable (ReachedBy L L' W obs source g D)]
    (read : (Nat → C → Nat) → A)
    (through : ∀ l l', W.RegistersAlikeUpTo obs g l l' D → read l = read l')
    (different : read W.level ≠ read W'.level) : ReachedBy L L' W obs source g D :=
  match decided with
  | isTrue reached => reached
  | isFalse unreached => False.elim
      (different_answers_not_unreached balanced balanced' present start responds read through
        different unreached)
end Deadline

theorem touches_registered_edge {g h : F} {t : Nat} {c : C}
    (present : L.present t = L'.present t) (reg : W.Registers obs g c)
    (touch : TouchesAt L L' t h c) : L.RegisteredFromEither W L' obs g h :=
  match touch.2 with
  | .inl pos => .inl ⟨c, reg, t, touch.1, .inl pos⟩
  | .inr (.inl pos) => .inl ⟨c, reg, t, touch.1, .inr pos⟩
  | .inr (.inr (.inl pos)) => .inr ⟨c, reg, t, present ▸ touch.1, .inl pos⟩
  | .inr (.inr (.inr pos)) => .inr ⟨c, reg, t, present ▸ touch.1, .inr pos⟩

/-- The new timed relation refines, rather than replaces, the existing responsive reach. -/
theorem Spread.within_response {part : F → Bool}
    (present : ∀ t, L.present t = L'.present t)
    (inside : ∀ t h, source t h → part h = true) {t : Nat} {c : C}
    (spread : Spread L L' W obs source t c) {g : F} (reg : W.Registers obs g c) :
    L.WithinResponse L' W obs part g := by
  induction spread generalizing g with
  | hold _ ih => exact ih reg
  | input src touch =>
      exact ⟨_, inside _ _ src,
        WithinClosure.of_rel (touches_registered_edge (present _) reg touch)⟩
  | response _ _ previous touch ih =>
      rcases ih previous with ⟨h, member, within⟩
      exact ⟨h, member, within.trans
        (WithinClosure.of_rel (touches_registered_edge (present _) reg touch))⟩

theorem reachedBy_within_response {part : F → Bool}
    (present : ∀ t, L.present t = L'.present t)
    (inside : ∀ t h, source t h → part h = true) {g : F} {T : Nat}
    (reached : ReachedBy L L' W obs source g T) : L.WithinResponse L' W obs part g :=
  match reached with
  | ⟨_, _, _, reg, spread⟩ => spread.within_response present inside reg

/-! A delayed native exchange. The source is true, the distinct reader is false.
Both are formations in the same web, sharing one condition. -/
namespace Delayed

def web (signal : Bool) : Web Bool Unit where
  level := fun t _ => match t with
    | 0 => 0
    | 1 => 0
    | _ + 2 => if signal then 1 else 0
  active := fun _ _ => True
  requires := fun _ _ _ => False
  need := fun _ _ _ => 0
  draws := fun _ _ _ => False

def flow (signal : Bool) : Flow Bool Unit where
  present := fun _ => [true, false]
  take := fun _ _ _ => 0
  give := fun t h _ => match t with
    | 1 => if h && signal then 1 else 0
    | _ => 0

def commandAt (t : Nat) (h : Bool) : Prop := t = 1 ∧ h = true

def readAt (t : Nat) (l : Nat → Unit → Nat) : Bool := decide (0 < l t ())

theorem balanced (b : Bool) : (flow b).Balances (web b) := by
  intro t c
  cases b <;> cases t with
  | zero => rfl
  | succ t => cases t with
    | zero => rfl
    | succ t => rfl

theorem responds : ∀ t, ∀ h, ¬ commandAt t h →
    (web false).RegistersAlikeUpTo (fun _ _ => True) h
      (web false).level (web true).level t →
    ∀ c, (flow false).take t h c = (flow true).take t h c ∧
      (flow false).give t h c = (flow true).give t h c := by
  intro t h out _ c
  cases t with
  | zero => exact ⟨rfl, rfl⟩
  | succ t => cases t with
    | zero => cases h with
      | false => exact ⟨rfl, rfl⟩
      | true => exact False.elim (out ⟨rfl, rfl⟩)
    | succ t => exact ⟨rfl, rfl⟩

theorem read_through (t : Nat) : ∀ l l', (web false).RegistersAlikeUpTo
    (fun _ _ => True) false l l' t → readAt t l = readAt t l' :=
  fun _ _ alike => congrArg (fun n => decide (0 < n)) ((alike t (Nat.le_refl t)).2 () trivial)

theorem structurally_connected :
    (flow false).WithinResponse (flow true) (web false) (fun _ _ => True) (fun h => h) false :=
  ⟨true, rfl, WithinClosure.of_rel (.inr ⟨(), .inr trivial, 1, .head _, .inr Nat.zero_lt_one⟩)⟩

theorem not_reached_at_one :
    ¬ ReachedBy (flow false) (flow true) (web false) (fun _ _ => True) commandAt false 1 :=
  not_reached_before_source fun _ _ before src =>
    Nat.lt_irrefl 1 (src.1 ▸ before)

theorem reached_at_two :
    ReachedBy (flow false) (flow true) (web false) (fun _ _ => True) commandAt false 2 :=
  ⟨2, (), Nat.le_refl 2, .inr trivial,
    .input (h := true) ⟨rfl, rfl⟩ ⟨.head _, .inr (.inr (.inr Nat.zero_lt_one))⟩⟩

/-- Static reach overestimates what can distinguish at step one; step two can distinguish. -/
theorem answers_before_and_after :
    readAt 1 (web false).level = readAt 1 (web true).level ∧
    readAt 2 (web false).level ≠ readAt 2 (web true).level :=
  ⟨rfl, Bool.noConfusion⟩

/-- A reached signal may be ignored: passing through registration does not ensure use. -/
theorem constant_read_ignores :
    (∀ l l', (web false).RegistersAlikeUpTo (fun _ _ => True) false l l' 2 →
      (fun _ : Nat → Unit → Nat => false) l = (fun _ => false) l') ∧
    (fun _ : Nat → Unit → Nat => false) (web true).level ≠ true :=
  ⟨fun _ _ _ => rfl, Bool.noConfusion⟩

end Delayed
end TimedResponse
end Becoming

