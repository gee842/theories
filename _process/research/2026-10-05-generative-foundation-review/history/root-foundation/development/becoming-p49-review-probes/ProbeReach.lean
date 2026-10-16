import Becoming.Testing

/-!
# Probe B: reach blindness where the others respond

Sixteenth review of P47. P47's `Flow.Balances.unregistered_beyond_registration` holds the rest
of the exchange fixed (withheld levels), so the transitive links of the registration closure do
no work in it: only direct exchange with what a formation registers matters
(`Flow.Balances.admits_unreached`). The closure earns its transitivity only in a comparison in
which the formations inside it respond. This probe checks that comparison.

* B1 `Flow.Balances.alike_within_closed`: take two balanced flows with the same formations
  taking part, and a region closed, in both flows, under being affected through what is
  registered. Let the levels start alike on everything any member registers, and let each member
  take from and give to what the members register only through its own registration. Then
  every member registers alike at every step, whatever else differs: other formations' acts,
  members' acts on conditions no member registers, and every unregistered level.
* B2 `Flow.Balances.alike_within_registration`: the same for `f`'s registration closure drawn
  through both flows.
* B3 `withheld_instance`: P47's fixed-rest theorem is the instance in which the second flow is the
  flow with the part withheld (the response hypothesis holds trivially).
* B4 `Clearing.alike_for_clearer_responsive`: `Clearing.alike_for_clearer` is an instance: the
  clearer's own clearing is an act on a condition nothing in its closure registers.
* B5 `Flow.withinRegistration_mono_obs`, `Flow.withinRegistration_mono_flow`: the registration
  closure grows with observation and with exchange (the "new exchanges widen" reading).
-/

namespace Becoming.Review47

open Becoming Generative

variable {F C : Type}

theorem total_congr_mem {α : Type} {p q : α → Nat} :
    ∀ {as : List α}, (∀ a, a ∈ as → p a = q a) → total as p = total as q
  | [], _ => rfl
  | a :: _, same => (congrArg (· + _) (same a (.head _))).trans
      (congrArg (q a + ·) (total_congr_mem fun b mem => same b (.tail a mem)))

namespace Flow

variable {L L' : Flow F C} {W W' : Web F C} {obs : F → C → Prop}

/-- Per formation: where a positive take or give on `c` by a member makes it a member, the two
flows' exchange of `h` on `c` agree whenever members' responses do. -/
theorem exchange_agrees {region : F → Prop} {g h : F} {c : C} {t : Nat}
    (closed : ClosedUnder (L.RegisteredFrom W obs) region)
    (closed' : ClosedUnder (L'.RegisteredFrom W obs) region)
    (present : L.present t = L'.present t) (member : region g) (registers : W.Registers obs g c)
    (mem : h ∈ L.present t)
    (respond : region h → L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c) :
    L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c :=
  have inside : (0 < L.take t h c ∨ 0 < L.give t h c ∨ 0 < L'.take t h c ∨ 0 < L'.give t h c) →
      region h := fun
    | .inl pos => closed g h member ⟨c, registers, t, mem, .inl pos⟩
    | .inr (.inl pos) => closed g h member ⟨c, registers, t, mem, .inr pos⟩
    | .inr (.inr (.inl pos)) => closed' g h member ⟨c, registers, t, present ▸ mem, .inl pos⟩
    | .inr (.inr (.inr pos)) => closed' g h member ⟨c, registers, t, present ▸ mem, .inr pos⟩
  match Nat.decLt 0 (L.take t h c), Nat.decLt 0 (L.give t h c),
      Nat.decLt 0 (L'.take t h c), Nat.decLt 0 (L'.give t h c) with
  | isTrue pos, _, _, _ => respond (inside (.inl pos))
  | _, isTrue pos, _, _ => respond (inside (.inr (.inl pos)))
  | _, _, isTrue pos, _ => respond (inside (.inr (.inr (.inl pos))))
  | _, _, _, isTrue pos => respond (inside (.inr (.inr (.inr pos))))
  | isFalse a, isFalse b, isFalse a', isFalse b' =>
    ⟨(eq_zero_of_not_pos a).trans (eq_zero_of_not_pos a').symm,
     (eq_zero_of_not_pos b).trans (eq_zero_of_not_pos b').symm⟩

/-- B1. **Reach blindness where the members respond.** -/
theorem Balances.alike_within_closed (balances : L.Balances W) (balances' : L'.Balances W')
    {region : F → Prop}
    (closed : ClosedUnder (L.RegisteredFrom W obs) region)
    (closed' : ClosedUnder (L'.RegisteredFrom W obs) region)
    (present : ∀ t, L.present t = L'.present t)
    (start : ∀ g, region g → ∀ c, W.Registers obs g c → W.level 0 c = W'.level 0 c)
    (responds : ∀ h, region h → ∀ t, W.AlikeUpTo obs h W.level W'.level t →
      ∀ g c, region g → W.Registers obs g c →
        L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c) :
    ∀ t g, region g → W.RegistersAlike obs g W.level W'.level t :=
  have alikeOf : ∀ t, (∀ g, region g → ∀ c, W.Registers obs g c → W.level t c = W'.level t c) →
      ∀ g, region g → W.RegistersAlike obs g W.level W'.level t := fun t same g member =>
    ⟨⟨fun admits c requires => Nat.le_trans (admits c requires)
        (Nat.le_of_eq (same g member c (.inl ⟨t, requires⟩))),
      fun admits c requires => Nat.le_trans (admits c requires)
        (Nat.le_of_eq (same g member c (.inl ⟨t, requires⟩)).symm)⟩,
     fun c observed => same g member c (.inr observed)⟩
  have levels : ∀ t, ∀ s, s ≤ t →
      ∀ g, region g → ∀ c, W.Registers obs g c → W.level s c = W'.level s c := fun t =>
    Nat.rec (motive := fun t => ∀ s, s ≤ t →
        ∀ g, region g → ∀ c, W.Registers obs g c → W.level s c = W'.level s c)
      (fun s le => match s, le with
        | 0, _ => start
        | _ + 1, le => absurd le (Nat.not_succ_le_zero _))
      (fun t ih s le g member c registers =>
        match Nat.lt_or_eq_of_le le with
        | .inl before => ih s (Nat.le_of_lt_succ before) g member c registers
        | .inr same => same ▸
          have upTo : ∀ h, region h → W.AlikeUpTo obs h W.level W'.level t :=
            fun h inside r le' => alikeOf r (ih r le') h inside
          have each : ∀ h, h ∈ L.present t →
              L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c := fun h mem =>
            exchange_agrees closed closed' (present t) member registers mem
              fun inside => responds h inside t (upTo h inside) g c member registers
          have taken : L.taken t c = L'.taken t c :=
            (total_congr_mem fun h mem => (each h mem).1).trans
              (congrArg (fun as => total as fun h => L'.take t h c) (present t))
          have given : L.given t c = L'.given t c :=
            (total_congr_mem fun h mem => (each h mem).2).trans
              (congrArg (fun as => total as fun h => L'.give t h c) (present t))
          have now := ih t (Nat.le_refl t) g member c registers
          add_right_cancel (L.taken t c)
            ((balances t c).trans
              ((congrArg (· + L.given t c) now).trans
                ((congrArg (W'.level t c + ·) given).trans
                  ((balances' t c).symm.trans
                    (congrArg (W'.level (t + 1) c + ·) taken.symm))))))
      t
  fun t g member => alikeOf t (levels t t (Nat.le_refl t)) g member

/-- Being affected through what is registered, in either flow. -/
def RegisteredFromEither (L L' : Flow F C) (W : Web F C) (obs : F → C → Prop) (g h : F) : Prop :=
  L.RegisteredFrom W obs g h ∨ L'.RegisteredFrom W obs g h

/-- B2. `f`'s registration closure drawn through both flows. -/
theorem Balances.alike_within_registration (balances : L.Balances W)
    (balances' : L'.Balances W') {f : F}
    (present : ∀ t, L.present t = L'.present t)
    (start : ∀ g, WithinClosure (RegisteredFromEither L L' W obs) f g →
      ∀ c, W.Registers obs g c → W.level 0 c = W'.level 0 c)
    (responds : ∀ h, WithinClosure (RegisteredFromEither L L' W obs) f h →
      ∀ t, W.AlikeUpTo obs h W.level W'.level t →
      ∀ g c, WithinClosure (RegisteredFromEither L L' W obs) f g → W.Registers obs g c →
        L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c) :
    ∀ t g, WithinClosure (RegisteredFromEither L L' W obs) f g →
      W.RegistersAlike obs g W.level W'.level t :=
  Becoming.Review47.Flow.Balances.alike_within_closed balances balances'
    (fun g h within related => within.trans (WithinClosure.of_rel (.inl related)))
    (fun g h within related => within.trans (WithinClosure.of_rel (.inr related)))
    present start responds

/-- B5. The registration closure grows with observation. -/
theorem withinRegistration_mono_obs {obs' : F → C → Prop} (larger : ∀ g c, obs g c → obs' g c)
    {f g : F} (within : L.WithinRegistration W obs f g) : L.WithinRegistration W obs' f g :=
  WithinClosure.mono (fun _ _ ⟨c, registers, exchanges⟩ =>
    ⟨c, registers.imp id (larger _ c), exchanges⟩) within

/-- B5. The registration closure grows with exchange. -/
theorem withinRegistration_mono_flow
    (more : ∀ h c, L.Exchanges h c → L'.Exchanges h c) {f g : F}
    (within : L.WithinRegistration W obs f g) : L'.WithinRegistration W obs f g :=
  WithinClosure.mono (fun _ _ ⟨c, registers, exchanges⟩ =>
    ⟨c, registers, more _ c exchanges⟩) within

end Flow

/-! ### B4. The clearer, as an instance -/

namespace ClearingResponsive

open Becoming.Clearing

/-- The clearer and the source. -/
def region : Formation → Prop
  | .source => True
  | .clearer => True
  | .dweller => False

/-- What a member registers under `supportOnly` is the resource. -/
theorem registers_resource {g : Formation} {c : Place} (member : region g)
    (registers : web.Registers supportOnly g c) : c = .resource :=
  match registers with
  | .inr no => False.elim no
  | .inl ⟨_, depends⟩ => match g, c, member, depends with
    | .clearer, .resource, _, _ => rfl
    | .source, _, _, no => nomatch no
    | .clearer, .habitat, _, no => nomatch no
    | .clearer, .fuel _, _, no => nomatch no

theorem closed_in (L : Flow Formation Place)
    (dwellerQuiet : ∀ t, L.take t .dweller .resource = 0 ∧ L.give t .dweller .resource = 0) :
    ClosedUnder (L.RegisteredFrom web supportOnly) region :=
  fun g h member ⟨c, registers, t, _, exchanges⟩ =>
    match c, registers_resource member registers, h, exchanges with
    | _, rfl, .source, _ => trivial
    | _, rfl, .clearer, _ => trivial
    | _, rfl, .dweller, .inl pos =>
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (dwellerQuiet t).1))
    | _, rfl, .dweller, .inr pos =>
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (dwellerQuiet t).2))

/-- B4. The clearer registers alike whether or not it clears, by B1: the clearing is an act on a
condition no member of its closure registers. -/
theorem alike_for_clearer_responsive :
    ∀ t, web.RegistersAlike supportOnly .clearer web.level sparedWeb.level t :=
  fun t => Becoming.Review47.Flow.Balances.alike_within_closed balances spared_balances
    (closed_in flow fun _ => ⟨rfl, rfl⟩) (closed_in sparedFlow fun _ => ⟨rfl, rfl⟩)
    (fun _ => rfl)
    (fun g member c registers => match c, registers_resource member registers with
      | _, rfl => rfl)
    (fun h _ t _ g c member registers => match c, registers_resource member registers with
      | _, rfl => match h with
        | .source => ⟨rfl, rfl⟩
        | .clearer => ⟨rfl, rfl⟩
        | .dweller => ⟨rfl, rfl⟩)
    t .clearer trivial

end ClearingResponsive

/-! ### B3. P47's fixed-rest theorem as an instance -/

namespace Flow

variable {L : Flow F C} {W : Web F C} {obs : F → C → Prop} {part : F → Bool}

theorem ite_pos_else {b : Bool} {q : Nat} (pos : 0 < (if b then 0 else q)) : 0 < q :=
  match b, pos with
  | false, pos => pos
  | true, pos => absurd pos (Nat.lt_irrefl 0)

theorem ite_false_eq {b : Bool} (no : b = false) (q : Nat) : (if b then 0 else q) = q :=
  match b, no with
  | false, _ => rfl

/-- The withheld flow exchanges only where the flow does. -/
theorem withhold_exchanges {h : F} {c : C} : (L.withhold part).Exchanges h c → L.Exchanges h c
  | ⟨t, mem, .inl pos⟩ => ⟨t, mem, .inl (ite_pos_else (b := part h) (q := L.take t h c) pos)⟩
  | ⟨t, mem, .inr pos⟩ => ⟨t, mem, .inr (ite_pos_else (b := part h) (q := L.give t h c) pos)⟩

/-- B3. The fixed-rest theorem from B1: the second flow is the flow with the part withheld, on
the web with the withheld levels. -/
theorem withheld_instance (balances : L.Balances W) {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {f : F}
    (beyond : ∀ h, part h = true → ¬ L.WithinRegistration W obs f h) :
    ∀ t g, L.WithinRegistration W obs f g → W.RegistersAlike obs g W.level l t :=
  have closed : ClosedUnder (L.RegisteredFrom W obs) (L.WithinRegistration W obs f) :=
    closedUnder_withinClosure f
  have closed' : ClosedUnder ((L.withhold part).RegisteredFrom W obs)
      (L.WithinRegistration W obs f) :=
    fun g h within ⟨c, registers, exchanges⟩ =>
      closed g h within ⟨c, registers, withhold_exchanges exchanges⟩
  fun t g within =>
    Becoming.Review47.Flow.Balances.alike_within_closed (W' := { W with level := l }) balances
      without.1
      closed closed' (fun _ => rfl)
      (fun _ _ c _ => (without.2 c).symm)
      (fun h inside _ _ _ _ _ _ =>
        have notPart : part h = false := match part h, beyond h with
          | false, _ => rfl
          | true, no => absurd inside (no rfl)
        ⟨(ite_false_eq notPart _).symm, (ite_false_eq notPart _).symm⟩)
      t g within

end Flow

end Becoming.Review47

open Becoming.Review47
#print axioms total_congr_mem
#print axioms Flow.exchange_agrees
#print axioms Flow.Balances.alike_within_closed
#print axioms Flow.Balances.alike_within_registration
#print axioms Flow.withinRegistration_mono_obs
#print axioms Flow.withinRegistration_mono_flow
#print axioms ClearingResponsive.alike_for_clearer_responsive
#print axioms Flow.withheld_instance
