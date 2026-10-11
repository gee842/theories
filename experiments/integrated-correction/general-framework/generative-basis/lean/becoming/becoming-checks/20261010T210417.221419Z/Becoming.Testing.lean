import Becoming.Feedback

/-!
# Testing: what registers in a formation, and what it can test

On 11 October 2026 Ren asked whether becoming can provide "wisdoms to avoid run away feedbacks
and the identification of knowledge, learning, and scientific principles like falsifiability",
and wrote: "I think all the wisdoms about wisdoms, how to think, learn, update, are all explained
within what we have, if not not proved yet". This module states, with no premise beyond the
representation, what a formation can register and what a claim needs in order to be tested by it.
No significance, ranking or axiom occurs.

* **Registration.** A formation registers its support and the levels of the conditions it
  observes (`obs`). Under two level histories it registers alike at a step when the levels admit
  it alike and its observed conditions stand alike (`Web.RegistersAlike`), and alike up to a step
  when it does so at every step up to it (`Web.AlikeUpTo`). Two observations are named:
  registering support only (`supportOnly`), and, in the one-kind reading, a formation's own
  standing as well (`ownStanding`). Observing more distinguishes more
  (`Web.AlikeUpTo.of_obs`). Webs that agree on what a formation requires and needs register its
  support through admission by their levels (`Web.admits_iff_supported`).
* **Refutation.** A claim about level histories is refuted by a formation at a step when no
  history meeting the claim is registered alike up to that step (`Web.Refutes`). A claim is
  refuted only through a difference in what registers (`Web.Refutes.not_of_alike`); what holds is
  never refuted (`Web.Refutes.not_meets`); a refutation stands at every later step
  (`Web.Refutes.later`); observing more refutes more (`Web.Refutes.widen`).
* **Reach blindness.** A formation registers a condition when it depends on it or observes it
  (`Web.Registers`). The registration closure is the closure under exchanging with a condition
  registered (`Flow.WithinRegistration`). It holds the influence closure of `Becoming.Feedback`
  (`Flow.withinRegistration_of_withinInfluence`) and, registering support only, is it
  (`Flow.withinRegistration_supportOnly`). Nothing beyond it exchanges with a condition
  registered within it (`Flow.beyond_registration`). With the rest of the exchange fixed, a part
  whose members all lie beyond a formation's registration closure is registered alike with and
  without it by every formation within the closure (`Flow.Balances.unregistered_beyond_registration`),
  so no claim met by the levels without the part is refuted there
  (`Flow.Balances.unrefuted_beyond_registration`). Registering one's own standing registers being
  taken from: in `Prey` a predator lies beyond the prey's influence closure and within its
  registration closure under `ownStanding`, its taking registers in the prey's standing and not
  in its support (`Prey.registers_taking`).
* **Testing is relational.** In `Clearing` the clearer registers alike at every step whether or
  not its clearing ends the dweller (`Clearing.alike_for_clearer`). The claim that the dweller
  is ended is refuted by the dweller in the spared world at the third step, and by the clearer at
  no step (`Clearing.tested_by_dweller`).
* **Threshold blindness.** Let two balanced flows, on webs agreeing on what `g` requires and
  needs, differ at the start only in a stock `c` that `g` depends on and does not observe, which
  stands `d` higher in the second; and let them respond to `g` only through what it registers
  (`Flow.RespondsThrough`). Then at every step before which the first web supported `g` at every
  step, the stock stands exactly `d` higher in the second, every other condition `g` registers
  stands alike, and `g` has registered alike (`Flow.Balances.threshold_blind`). Where the poorer
  web supports `g` throughout, the surplus is never drawn on and `g` registers alike throughout
  (`Flow.Balances.surplus_untouched`). The surplus is drawn on only after the poorer web has
  failed to support `g`, and, where activity needs support, after `g` has failed to be active
  there (`Flow.Balances.surplus_after_break`). Observing one's own standing does not change this
  for a stock other than oneself (`ownStanding_other`). Observing the stock does: in `Gauged` a
  formation that observes its stock draws all of it above its need in both webs, stays supported
  in both and draws on the surplus, while no response through support alone can
  (`Gauged.draws_surplus`).
* **Horizon.** A reading decided by the first `h` steps of a run that credits no run consuming
  withholds credit from a run renewing (`Renewable.finite_reading_withholds_renewal`), the dual of
  `Renewable.finite_reading_credits_consumption`: every finite test of renewal errs on one side.

**Readings (the AI's, which Ren accepted on 11 October 2026).**
- Feedback through support has three blindnesses: below a threshold (`threshold_blind`), beyond
  the horizon (`Becoming.Horizon`), and beyond the registration closure
  (`unregistered_beyond_registration`).
- A runaway is a loop that runs inside one of them: its gains register in it and its losses do
  not, or not until the break.
- Measurement registers a level below the threshold (`Gauged`); a model of where the run goes
  crosses the horizon; another formation's registration and new exchanges widen the closure
  (`Clearing.tested_by_dweller`, `Refutes.widen`).
- Falsifiability is the condition of being corrected by the unfolding: a claim and its rivals
  must differ in what can register. It is relational, it moves with what is registered, and
  claims about the whole run are not tested by any finite record.

What is not derived:
- that a formation observes anything beyond its support, forms a model, or wants to avoid a
  runaway;
- what a registration is about: registering alike bounds what can be told apart, and says
  nothing of what a difference signifies;
- which laws hold of the actual unfolding;
- how others respond: the threshold result takes the responses through registration as a
  hypothesis (`Flow.RespondsThrough`), and the comparison with a part withheld holds the rest of
  the exchange fixed.

Activity is supplied by the representation, not produced by the exchange, so it is not counted
as registered; under `Web.Dependent` it cannot outrun support. The representation commits to
discrete steps and natural quantities.
-/

namespace Becoming

open Generative

variable {F C : Type}

/-! ## Registration and refutation -/

/-- No level is observed: a formation registers its support only. -/
def supportOnly : F → C → Prop := fun _ _ => False

/-- In the one-kind reading, a formation observes its own standing. -/
def ownStanding {X : Type} : X → X → Prop := fun g c => c = g

/-- A stock other than oneself is not one's own standing. -/
theorem ownStanding_other {X : Type} {g c : X} (other : c ≠ g) : ¬ ownStanding g c :=
  other

namespace Web

variable (W : Web F C)

/-- Under two level histories, `g` registers alike at `t`: the levels admit it alike, and the
conditions it observes stand alike. -/
def RegistersAlike (obs : F → C → Prop) (g : F) (l l' : Nat → C → Nat) (t : Nat) : Prop :=
  (W.Admits (l t) t g ↔ W.Admits (l' t) t g) ∧ ∀ c, obs g c → l t c = l' t c

/-- `g` registers alike at every step up to `t`. -/
def AlikeUpTo (obs : F → C → Prop) (g : F) (l l' : Nat → C → Nat) (t : Nat) : Prop :=
  ∀ s, s ≤ t → W.RegistersAlike obs g l l' s

/-- A claim about level histories is refuted by `g` at `t` under `l` when no history meeting the
claim is registered alike by `g` up to `t`. -/
def Refutes (obs : F → C → Prop) (claim : (Nat → C → Nat) → Prop) (g : F)
    (l : Nat → C → Nat) (t : Nat) : Prop :=
  ∀ l', claim l' → ¬ W.AlikeUpTo obs g l l' t

/-- `g` registers a condition: it depends on it or observes it. -/
def Registers (obs : F → C → Prop) (g : F) (c : C) : Prop :=
  W.DependsOn g c ∨ obs g c

variable {W} {obs obs' : F → C → Prop} {g : F} {l l' : Nat → C → Nat}

/-- Every history registers alike with itself. -/
theorem RegistersAlike.refl (t : Nat) : W.RegistersAlike obs g l l t :=
  ⟨Iff.rfl, fun _ _ => rfl⟩

/-- Registering alike is symmetric. -/
theorem RegistersAlike.symm {t : Nat} (alike : W.RegistersAlike obs g l l' t) :
    W.RegistersAlike obs g l' l t :=
  ⟨alike.1.symm, fun c observed => (alike.2 c observed).symm⟩

/-- Registering alike up to a step is symmetric. -/
theorem AlikeUpTo.symm {t : Nat} (alike : W.AlikeUpTo obs g l l' t) : W.AlikeUpTo obs g l' l t :=
  fun s le => (alike s le).symm

/-- Alike up to a step, alike up to every earlier step. -/
theorem AlikeUpTo.earlier {s t : Nat} (alike : W.AlikeUpTo obs g l l' t) (le : s ≤ t) :
    W.AlikeUpTo obs g l l' s :=
  fun r le' => alike r (Nat.le_trans le' le)

/-- Observing more distinguishes more: histories alike under a larger observation are alike
under a smaller one. -/
theorem AlikeUpTo.of_obs (larger : ∀ g c, obs g c → obs' g c) {t : Nat}
    (alike : W.AlikeUpTo obs' g l l' t) : W.AlikeUpTo obs g l l' t :=
  fun s le => ⟨(alike s le).1, fun c observed => (alike s le).2 c (larger g c observed)⟩

/-- A claim is refuted only through a difference in what registers: where a history meeting it
is registered alike up to a step, it is not refuted there. -/
theorem Refutes.not_of_alike {claim : (Nat → C → Nat) → Prop} {t : Nat} (meets : claim l')
    (alike : W.AlikeUpTo obs g l l' t) : ¬ W.Refutes obs claim g l t :=
  fun refutes => refutes l' meets alike

/-- What holds is never refuted. -/
theorem Refutes.not_meets {claim : (Nat → C → Nat) → Prop} {t : Nat}
    (refutes : W.Refutes obs claim g l t) : ¬ claim l :=
  fun meets => refutes l meets fun s _ => RegistersAlike.refl s

/-- A refutation stands: refuted at a step, refuted at every later step. -/
theorem Refutes.later {claim : (Nat → C → Nat) → Prop} {s t : Nat}
    (refutes : W.Refutes obs claim g l s) (le : s ≤ t) : W.Refutes obs claim g l t :=
  fun l' meets alike => refutes l' meets (alike.earlier le)

/-- Observing more refutes more. -/
theorem Refutes.widen (larger : ∀ g c, obs g c → obs' g c) {claim : (Nat → C → Nat) → Prop}
    {t : Nat} (refutes : W.Refutes obs claim g l t) : W.Refutes obs' claim g l t :=
  fun l' meets alike => refutes l' meets (alike.of_obs larger)

/-- Webs agreeing on what `g` requires and needs register its support through admission by their
levels. -/
theorem admits_iff_supported {W' : Web F C} (requires : ∀ t c, W.requires t g c ↔ W'.requires t g c)
    (need : ∀ t c, W.need t g c = W'.need t g c) (t : Nat) :
    W.Admits (W'.level t) t g ↔ W'.Supported t g :=
  ⟨fun admits c requires' =>
     Nat.le_trans (Nat.le_of_eq (need t c).symm) (admits c ((requires t c).mpr requires')),
   fun supported c requires'' =>
     Nat.le_trans (Nat.le_of_eq (need t c)) (supported c ((requires t c).mp requires''))⟩

end Web

/-! ## Reach blindness: nothing beyond the registration closure registers -/

namespace Flow

variable (L : Flow F C) (W : Web F C)

/-- `g` is affected through what it registers by `h`: `h` exchanges with a condition `g`
registers. -/
def RegisteredFrom (obs : F → C → Prop) (g h : F) : Prop :=
  ∃ c, W.Registers obs g c ∧ L.Exchanges h c

/-- `g` lies within `f`'s registration closure: the closure under being affected through what is
registered. -/
def WithinRegistration (obs : F → C → Prop) (f g : F) : Prop :=
  WithinClosure (L.RegisteredFrom W obs) f g

/-- Two flows respond to `g` only through what it registers: wherever `g` registers alike at
every step up to `t`, they take from and give to every condition `g` registers alike across the
step from `t`. -/
def RespondsThrough (L' : Flow F C) (W' : Web F C) (obs : F → C → Prop) (g : F) : Prop :=
  ∀ t, W.AlikeUpTo obs g W.level W'.level t → ∀ c, W.Registers obs g c →
    L.taken t c = L'.taken t c ∧ L.given t c = L'.given t c

variable {L W} {obs : F → C → Prop} {part : F → Bool}

/-- The registration closure holds the influence closure. -/
theorem withinRegistration_of_withinInfluence {f g : F} (within : L.WithinInfluence W f g) :
    L.WithinRegistration W obs f g :=
  WithinClosure.mono (fun _ _ ⟨c, depends, exchanges⟩ => ⟨c, .inl depends, exchanges⟩) within

/-- Registering support only, the registration closure is the influence closure. -/
theorem withinRegistration_supportOnly {f g : F} :
    L.WithinRegistration W supportOnly f g ↔ L.WithinInfluence W f g :=
  ⟨WithinClosure.mono fun _ _ ⟨c, registers, exchanges⟩ => match registers with
     | .inl depends => ⟨c, depends, exchanges⟩
     | .inr no => False.elim no,
   withinRegistration_of_withinInfluence⟩

/-- Nothing beyond a formation's registration closure exchanges with a condition registered
within it. -/
theorem beyond_registration {f g h : F} (within : L.WithinRegistration W obs f g)
    (beyond : ¬ L.WithinRegistration W obs f h) {c : C} (registers : W.Registers obs g c) :
    ¬ L.Exchanges h c :=
  fun exchanges => WithinClosure.not_rel within beyond ⟨c, registers, exchanges⟩

/-- **Reach blindness.** With the rest of the exchange fixed, where every member of a part lies
beyond `f`'s registration closure, each formation within the closure registers alike with and
without the part at every step: its support is admitted alike, and its observed conditions stand
alike. -/
theorem Balances.unregistered_beyond_registration (balances : L.Balances W)
    {l : Nat → C → Nat} (without : L.WithheldLevels part W l) {f : F}
    (beyond : ∀ h, part h = true → ¬ L.WithinRegistration W obs f h) :
    ∀ t g, L.WithinRegistration W obs f g → W.RegistersAlike obs g W.level l t :=
  fun t _ within =>
    ⟨balances.admits_unreached without (fun ⟨h, member, _, depends, exchanges⟩ =>
        beyond_registration within (beyond h member) (.inl depends) exchanges) t,
     fun _ observed => balances.agrees_of_quiet without (fun h member exchanges =>
        beyond_registration within (beyond h member) (.inr observed) exchanges) t⟩

/-- What a part beyond the registration closure does cannot be tested within it: no claim met by
the levels without the part is refuted, at any step, by a formation within the closure. -/
theorem Balances.unrefuted_beyond_registration (balances : L.Balances W)
    {l : Nat → C → Nat} (without : L.WithheldLevels part W l) {f : F}
    (beyond : ∀ h, part h = true → ¬ L.WithinRegistration W obs f h)
    {claim : (Nat → C → Nat) → Prop} (meets : claim l) :
    ∀ t g, L.WithinRegistration W obs f g → ¬ W.Refutes obs claim g W.level t :=
  fun _ g within => Web.Refutes.not_of_alike meets fun s _ =>
    balances.unregistered_beyond_registration without beyond s g within

/-! ## Threshold blindness: support registers a stock only at the break -/

variable [DecidableEq C] {L' : Flow F C} {W' : Web F C} {g : F} {c : C} {d : Nat}

/-- **Threshold blindness.** Let two balanced flows, on webs agreeing on what `g` requires and
needs, start alike on every condition `g` registers except a stock `c` that `g` depends on and
does not observe, which stands `d` higher in the second; and let them respond to `g` only through
what it registers. Then at every step before which the first web supported `g` at every step, the
stock stands exactly `d` higher in the second, every other condition `g` registers stands alike,
and `g` has registered alike at every earlier step. -/
theorem Balances.threshold_blind (balances : L.Balances W) (balances' : L'.Balances W')
    (requires : ∀ t e, W.requires t g e ↔ W'.requires t g e)
    (need : ∀ t e, W.need t g e = W'.need t g e)
    (depends : W.DependsOn g c) (unobserved : ¬ obs g c)
    (stock : W'.level 0 c = W.level 0 c + d)
    (start : ∀ e, W.Registers obs g e → e ≠ c → W.level 0 e = W'.level 0 e)
    (responds : L.RespondsThrough W L' W' obs g) :
    ∀ t, (∀ s, s < t → W.Supported s g) →
      W'.level t c = W.level t c + d ∧ (∀ e, W.Registers obs g e → e ≠ c →
        W.level t e = W'.level t e) ∧ ∀ s, s < t → W.RegistersAlike obs g W.level W'.level s
  | 0, _ => ⟨stock, start, fun s before => absurd before (Nat.not_lt_zero s)⟩
  | t + 1, supported =>
    match balances.threshold_blind balances' requires need depends unobserved stock start
      responds t (fun s before => supported s (Nat.lt_succ_of_lt before)) with
    | ⟨high, others, past⟩ =>
      have now : W.Supported t g := supported t (Nat.lt_succ_self t)
      have admitted : W.Admits (W'.level t) t g := fun e requires' =>
        match decEq e c with
        | isTrue same => match e, same, requires' with
          | _, rfl, requires' => Nat.le_trans (now c requires')
              (Nat.le_trans (Nat.le_add_right (W.level t c) d) (Nat.le_of_eq high.symm))
        | isFalse other => Nat.le_trans (now e requires')
            (Nat.le_of_eq (others e (.inl ⟨t, requires'⟩) other))
      have alike : W.RegistersAlike obs g W.level W'.level t :=
        ⟨⟨fun _ => admitted, fun _ => now⟩, fun e observed =>
          others e (.inr observed) fun same => unobserved (same ▸ observed)⟩
      have upTo : W.AlikeUpTo obs g W.level W'.level t := fun s le =>
        match Nat.lt_or_eq_of_le le with
        | .inl before => past s before
        | .inr same => same ▸ alike
      have exchange := responds t upTo
      ⟨match exchange c (.inl depends) with
       | ⟨taken, given⟩ => add_right_cancel (L.taken t c)
          (calc W'.level (t + 1) c + L.taken t c
              = W'.level (t + 1) c + L'.taken t c := congrArg (W'.level (t + 1) c + ·) taken
            _ = W'.level t c + L'.given t c := balances' t c
            _ = W.level t c + d + L.given t c := by rw [high, given]
            _ = W.level t c + L.given t c + d := Nat.add_right_comm _ _ _
            _ = W.level (t + 1) c + L.taken t c + d := by rw [balances t c]
            _ = W.level (t + 1) c + d + L.taken t c := Nat.add_right_comm _ _ _),
       fun e registers other => match exchange e registers with
       | ⟨taken, given⟩ => add_right_cancel (L.taken t e)
          (calc W.level (t + 1) e + L.taken t e
              = W.level t e + L.given t e := balances t e
            _ = W'.level t e + L'.given t e := by rw [others e registers other, given]
            _ = W'.level (t + 1) e + L'.taken t e := (balances' t e).symm
            _ = W'.level (t + 1) e + L.taken t e := by rw [taken]),
       fun s before => match Nat.lt_or_eq_of_le (Nat.le_of_lt_succ before) with
       | .inl earlier => past s earlier
       | .inr same => same ▸ alike⟩

/-- The surplus is never drawn on while the poorer web supports `g`: where it supports `g` at
every step, the stock stands `d` higher at every step and `g` registers alike at every step. -/
theorem Balances.surplus_untouched (balances : L.Balances W) (balances' : L'.Balances W')
    (requires : ∀ t e, W.requires t g e ↔ W'.requires t g e)
    (need : ∀ t e, W.need t g e = W'.need t g e)
    (depends : W.DependsOn g c) (unobserved : ¬ obs g c)
    (stock : W'.level 0 c = W.level 0 c + d)
    (start : ∀ e, W.Registers obs g e → e ≠ c → W.level 0 e = W'.level 0 e)
    (responds : L.RespondsThrough W L' W' obs g) (supported : ∀ t, W.Supported t g) :
    ∀ t, W'.level t c = W.level t c + d ∧ W.RegistersAlike obs g W.level W'.level t :=
  fun t =>
    ⟨(balances.threshold_blind balances' requires need depends unobserved stock start responds t
        fun s _ => supported s).1,
     (balances.threshold_blind balances' requires need depends unobserved stock start responds
        (t + 1) fun s _ => supported s).2.2 t (Nat.lt_succ_self t)⟩

/-- The surplus is drawn on only after a break. Where the stock no longer stands `d` higher in the
second web at a step, the first web did not support `g` at every earlier step, and, where activity
needs support, `g` was not active there at every earlier step. -/
theorem Balances.surplus_after_break (balances : L.Balances W) (balances' : L'.Balances W')
    (requires : ∀ t e, W.requires t g e ↔ W'.requires t g e)
    (need : ∀ t e, W.need t g e = W'.need t g e)
    (depends : W.DependsOn g c) (unobserved : ¬ obs g c)
    (stock : W'.level 0 c = W.level 0 c + d)
    (start : ∀ e, W.Registers obs g e → e ≠ c → W.level 0 e = W'.level 0 e)
    (responds : L.RespondsThrough W L' W' obs g) {t : Nat}
    (drawn : W'.level t c ≠ W.level t c + d) :
    ¬ (∀ s, s < t → W.Supported s g) ∧ (W.Dependent → ¬ ∀ s, s < t → W.active s g) :=
  have broke : ¬ ∀ s, s < t → W.Supported s g := fun supported =>
    drawn (balances.threshold_blind balances' requires need depends unobserved stock start
      responds t supported).1
  ⟨broke, fun dependent active => broke fun s before => dependent s g (active s before)⟩

end Flow

/-! ## Witnesses -/

/-- One is not two. -/
theorem one_ne_two : (1 : Nat) ≠ 2 :=
  fun same => Nat.lt_irrefl 1 (Nat.lt_of_lt_of_le (Nat.lt_succ_self 1) (Nat.le_of_eq same.symm))

/-- Two is not three. -/
theorem two_ne_three : (2 : Nat) ≠ 3 :=
  fun same => Nat.lt_irrefl 2 (Nat.lt_of_lt_of_le (Nat.lt_succ_self 2) (Nat.le_of_eq same.symm))

/-! ### A formation that observes its stock

It needs one unit of the stock, draws all of the stock above its need at the first step and
nothing after. In the poorer web the stock stands at two, in the richer at three. -/

namespace Gauged

/-- What the formation takes at each step under each start. -/
def draw (above : Nat) : Nat → Nat
  | 0 => above
  | _ + 1 => 0

/-- The flow drawing `above` units at the first step. -/
def flow (above : Nat) : Flow Unit Unit where
  present _ := [()]
  take t _ _ := draw above t
  give _ _ _ := 0

/-- The level of the stock: `1 + above` at the start, one after. -/
def level (above : Nat) : Nat → Nat
  | 0 => 1 + above
  | _ + 1 => 1

/-- The web whose stock starts at `1 + above`. -/
def web (above : Nat) : Web Unit Unit where
  level t _ := level above t
  active _ _ := True
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ _ _ := True

/-- Observing the stock. -/
def stock : Unit → Unit → Prop := fun _ _ => True

theorem balances (above : Nat) : (flow above).Balances (web above)
  | 0, () => show 1 + (above + 0) = 1 + above + 0 from rfl
  | _ + 1, () => rfl

theorem supported (above : Nat) : ∀ t, (web above).Supported t ()
  | 0, (), _ => Nat.le_add_right 1 above
  | _ + 1, (), _ => Nat.le_refl 1

theorem dependent (above : Nat) : (web above).Dependent :=
  fun t _ _ => supported above t

/-- **Observing the stock draws the surplus.** In the poorer web (one unit above the need) and
the richer (two), the formation drawing all of the stock above its need is supported at every
step in both, and in the richer it draws on its surplus: the stock no longer stands one higher.
Observing the stock, the two flows respond to it only through what it registers. Through its
support only they do not: it registers alike at the first step, where they take differently. -/
theorem draws_surplus :
    (flow 1).Balances (web 1) ∧ (flow 2).Balances (web 2) ∧ (web 1).Dependent ∧
      (web 2).Dependent ∧ (∀ t, (web 1).Supported t () ∧ (web 2).Supported t ()) ∧
      (web 2).level 0 () = (web 1).level 0 () + 1 ∧
      (web 2).level 1 () ≠ (web 1).level 1 () + 1 ∧
      (flow 1).RespondsThrough (web 1) (flow 2) (web 2) stock () ∧
      ¬ (flow 1).RespondsThrough (web 1) (flow 2) (web 2) supportOnly () :=
  ⟨balances 1, balances 2, dependent 1, dependent 2,
   fun t => ⟨supported 1 t, supported 2 t⟩, rfl, fun same => one_ne_two same,
   fun _ alike => absurd ((alike 0 (Nat.zero_le _)).2 () trivial) two_ne_three,
   fun responds => one_ne_two
     ((responds 0 (fun s le => match s, le with
        | 0, _ => ⟨⟨fun _ => supported 2 0, fun _ => supported 1 0⟩, fun _ no => False.elim no⟩
        | _ + 1, le => absurd le (Nat.not_succ_le_zero _))
       () (.inl ⟨0, trivial⟩)).1)⟩

end Gauged

/-! ### A formation that draws one unit while supported

It needs one unit of the stock and responds through its support only: it draws one unit at each
step at which it is supported, and is active exactly then. In the poorer web the stock stands at
two, in the richer at three. -/

namespace Gated

/-- The poorer stock: two, one, then nothing. -/
def poorLevel : Nat → Nat
  | 0 => 2
  | 1 => 1
  | _ + 2 => 0

/-- The richer stock: three, two, one, then nothing. -/
def richLevel : Nat → Nat
  | 0 => 3
  | 1 => 2
  | 2 => 1
  | _ + 3 => 0

/-- One unit at each supported step of the poorer web. -/
def poorDraw : Nat → Nat
  | 0 => 1
  | 1 => 1
  | _ + 2 => 0

/-- One unit at each supported step of the richer web. -/
def richDraw : Nat → Nat
  | 0 => 1
  | 1 => 1
  | 2 => 1
  | _ + 3 => 0

def flow (draw : Nat → Nat) : Flow Unit Unit where
  present _ := [()]
  take t _ _ := draw t
  give _ _ _ := 0

/-- The web of a stock: the formation needs one unit and is active exactly while it stands. -/
def web (level : Nat → Nat) : Web Unit Unit where
  level t _ := level t
  active t _ := 1 ≤ level t
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ _ _ := True

theorem poor_balances : (flow poorDraw).Balances (web poorLevel)
  | 0, () => rfl
  | 1, () => rfl
  | _ + 2, () => rfl

theorem rich_balances : (flow richDraw).Balances (web richLevel)
  | 0, () => rfl
  | 1, () => rfl
  | 2, () => rfl
  | _ + 3, () => rfl

theorem dependent (level : Nat → Nat) : (web level).Dependent :=
  fun _ _ active _ _ => active

/-- The two flows respond to the formation through its support only. Up to the second step
they draw alike; from the third, the support registers differently. -/
theorem responds : (flow poorDraw).RespondsThrough (web poorLevel) (flow richDraw) (web richLevel)
    supportOnly ()
  | 0, _, (), _ => ⟨rfl, rfl⟩
  | 1, _, (), _ => ⟨rfl, rfl⟩
  | t + 2, alike, (), _ => absurd ((alike 2 (Nat.le_add_left 2 t)).1.mpr
      (fun _ _ => Nat.le_refl 1) () trivial) (Nat.not_succ_le_zero 0)

/-- **The surplus waits for the break.** Through its support only, the formation registers the
richer stock as the poorer up to the third step, where the poorer web breaks: the surplus of one
unit stands untouched through that step, as `Flow.Balances.threshold_blind` gives, and is drawn on
only after it. -/
theorem surplus_waits :
    (flow poorDraw).Balances (web poorLevel) ∧ (flow richDraw).Balances (web richLevel) ∧
      (web poorLevel).Dependent ∧ (web richLevel).Dependent ∧
      (flow poorDraw).RespondsThrough (web poorLevel) (flow richDraw) (web richLevel)
        supportOnly () ∧
      (∀ t, t ≤ 2 → (web richLevel).level t () = (web poorLevel).level t () + 1) ∧
      ¬ (web poorLevel).Supported 2 () ∧ (web richLevel).Supported 2 () ∧
      (web richLevel).level 3 () ≠ (web poorLevel).level 3 () + 1 :=
  ⟨poor_balances, rich_balances, dependent poorLevel, dependent richLevel, responds,
   fun t le => (poor_balances.threshold_blind rich_balances (fun _ _ => Iff.rfl) (fun _ _ => rfl)
      ⟨0, trivial⟩ (fun no => no) rfl (fun () _ other => absurd rfl other) responds t
      (fun s before => match s, before with
        | 0, _ => fun _ _ => Nat.le_succ 1
        | 1, _ => fun _ _ => Nat.le_refl 1
        | s + 2, before => absurd (Nat.lt_of_lt_of_le before le)
            (Nat.not_lt_of_le (Nat.le_add_left 2 s)))).1,
   fun supported => Nat.not_succ_le_zero 0 (supported () trivial),
   fun _ _ => Nat.le_refl 1,
   fun same => Nat.not_succ_le_zero 0 (Nat.le_of_eq same.symm)⟩

end Gated

/-! ### A predator takes from the prey's standing

The prey depends on food that nothing exchanges with. -/

namespace Prey

inductive Relatum where
  | food
  | prey
  | predator

open Relatum

/-- The predator takes one unit of the prey's standing at the first step. -/
def bite : Nat → Nat
  | 0 => 1
  | _ + 1 => 0

def flow : Flow Relatum Relatum where
  present _ := [predator]
  take t f c := match f, c with
    | predator, prey => bite t
    | predator, food => 0
    | predator, predator => 0
    | food, _ => 0
    | prey, _ => 0
  give _ _ _ := 0

/-- The prey's standing: two at the start, one after the bite. -/
def standing : Nat → Nat
  | 0 => 2
  | _ + 1 => 1

def web : Web Relatum Relatum where
  level t c := match c with
    | food => 1
    | prey => standing t
    | predator => 0
  active _ _ := True
  requires _ f c := match f, c with
    | prey, food => True
    | prey, prey => False
    | prey, predator => False
    | food, _ => False
    | predator, _ => False
  need _ _ _ := 1
  draws _ f c := match f, c with
    | predator, prey => True
    | predator, food => False
    | predator, predator => False
    | food, _ => False
    | prey, _ => False

/-- The predator's part. -/
def predatorPart : Relatum → Bool
  | predator => true
  | food => false
  | prey => false

/-- The levels without the predator: the prey stays at two. -/
def spared (_ : Nat) : Relatum → Nat
  | food => 1
  | prey => 2
  | predator => 0

theorem balances : flow.Balances web
  | 0, food => rfl
  | 0, prey => rfl
  | 0, predator => rfl
  | _ + 1, food => rfl
  | _ + 1, prey => rfl
  | _ + 1, predator => rfl

theorem dependent : web.Dependent
  | _, prey, _, food, _ => Nat.le_refl 1
  | _, prey, _, prey, no => nomatch no
  | _, prey, _, predator, no => nomatch no
  | _, food, _, _, no => nomatch no
  | _, predator, _, _, no => nomatch no

theorem withheld : flow.WithheldLevels predatorPart web spared :=
  ⟨fun _ c => match c with
    | food => rfl
    | prey => rfl
    | predator => rfl,
   fun c => match c with
    | food => rfl
    | prey => rfl
    | predator => rfl⟩

/-- The region holding the prey alone is closed under being affected: nothing exchanges with the
food it depends on. -/
theorem preyAlone_closed : ClosedUnder (flow.AffectedBy web) (fun x => x = prey)
  | g, h, same, ⟨c, ⟨_, depends⟩, ⟨_, _, exchanges⟩⟩ =>
    match g, same, c, depends, h, exchanges with
    | _, rfl, food, _, predator, .inl taken => absurd taken (Nat.lt_irrefl 0)
    | _, rfl, food, _, food, .inl taken => absurd taken (Nat.lt_irrefl 0)
    | _, rfl, food, _, prey, .inl taken => absurd taken (Nat.lt_irrefl 0)
    | _, rfl, food, _, _, .inr given => absurd given (Nat.lt_irrefl 0)
    | _, rfl, prey, no, _, _ => nomatch no
    | _, rfl, predator, no, _, _ => nomatch no

/-- **Registering one's own standing registers being taken from.** The predator lies beyond the
prey's influence closure and within its registration closure observing its own standing. With
the rest of the exchange fixed, the prey registers the predator's part alike through its support
at every step, and not through its own standing after the bite. -/
theorem registers_taking :
    ¬ flow.WithinInfluence web prey predator ∧
      flow.WithinRegistration web ownStanding prey predator ∧
      (∀ t, web.RegistersAlike supportOnly prey web.level spared t) ∧
      ¬ web.RegistersAlike ownStanding prey web.level spared 1 :=
  have beyond : ¬ flow.WithinInfluence web prey predator := fun within =>
    Relatum.noConfusion (within (fun x => x = prey) preyAlone_closed rfl)
  ⟨beyond,
   WithinClosure.of_rel ⟨prey, .inr rfl, ⟨0, .head _, .inl Nat.zero_lt_one⟩⟩,
   fun t => balances.unregistered_beyond_registration withheld
     (fun h member => match h, member with
       | predator, _ => fun within => beyond (Flow.withinRegistration_supportOnly.mp within)
       | food, no => nomatch no
       | prey, no => nomatch no)
     t prey (WithinClosure.refl _),
   fun alike => one_ne_two (alike.2 prey rfl)⟩

end Prey

namespace Clearing

/-- The clearer registers alike at every step whether or not it clears the habitat. -/
theorem alike_for_clearer :
    ∀ t, web.AlikeUpTo supportOnly .clearer web.level sparedWeb.level t :=
  fun _ s _ => ⟨(unregistered.2.2.1 s).trans
      (Web.admits_iff_supported (W := web) (W' := sparedWeb) (fun _ _ => Iff.rfl)
        (fun _ _ => rfl) s).symm, fun _ no => False.elim no⟩

/-- The dweller is ended: from the third step on the levels do not admit it. -/
def Ended (l : Nat → Place → Nat) : Prop :=
  ∀ n, ¬ web.Admits (l (n + 2)) (n + 2) .dweller

/-- **Testing is relational.** In the world with the habitat spared, the claim that the dweller
is ended is refuted by the clearer at no step, and by the dweller at the third step. -/
theorem tested_by_dweller :
    Ended web.level ∧ (∀ t, ¬ web.Refutes supportOnly Ended .clearer sparedWeb.level t) ∧
      web.Refutes supportOnly Ended .dweller sparedWeb.level 2 :=
  ⟨unsupported_with,
   fun t => Web.Refutes.not_of_alike (claim := Ended) (l' := web.level) unsupported_with
     (alike_for_clearer t).symm,
   fun _ ended alike => ended 0 ((alike 2 (Nat.le_refl 2)).1.mp
     ((Web.admits_iff_supported (W := web) (W' := sparedWeb) (fun _ _ => Iff.rfl)
        (fun _ _ => rfl) 2).mpr (spared_dependent 2 .dweller trivial)))⟩

end Clearing

namespace Renewable

/-- Every finite test of renewal errs on one side. A reading decided by the first `h` steps of a
run, crediting no run in which the focal formation consumes, withholds credit from a run in which
it renews. -/
theorem finite_reading_withholds_renewal (h : Nat) (reading : Run process → Prop)
    (decided : ∀ r r', r.AgreeUpTo h r' → reading r → reading r')
    (sound : ∀ r, reading r → ¬ (conditions.dependence.along r).ConsumingIn .focal) :
    ∃ r, (conditions.dependence.along r).RenewingIn .focal ∧ ¬ reading r :=
  match prefix_does_not_decide h with
  | ⟨renewing, consuming, agree, _, _, renews, consumes⟩ =>
    ⟨renewing, renews, fun reads => sound consuming (decided renewing consuming agree reads)
      consumes⟩

end Renewable

end Becoming
