import Becoming.Feedback

/-!
# Testing: what registers in a formation, and what it can test

On 11 October 2026 Ren asked whether becoming can provide "wisdoms to avoid run away feedbacks
and the identification of knowledge, learning, and scientific principles like falsifiability",
and wrote: "I think all the wisdoms about wisdoms, how to think, learn, update, are all explained
within what we have, if not not proved yet". To the AI's answer Ren replied: "agree with you,
great job, start now. for 4, you can explore which option is better, then make decision". This
module states, with no premise beyond balance on the conditions registered and the
representation, what a formation can register, what a claim needs in order to be tested by it,
and where a difference stays unregistered. No significance, ranking or axiom occurs. The responsive form of reach blindness,
the exact threshold laws, refutation relative to a model, pooled testing, the bridge to
`Becoming.Inquiry` and the self-bearing witness were proposed and checked by the stage's
independent review.

* **Registration.** A formation registers its support, whether the levels admit it, and the
  levels of the conditions it observes (`obs`). Under two level histories it registers alike at a
  step when the levels admit it alike and its observed conditions stand alike
  (`Web.RegistersAlike`), and alike up to a step when it does so at every step up to it
  (`Web.RegistersAlikeUpTo`). A condition it depends on and does not observe registers only
  whether it meets the need (`Web.alike_of_threshold`); an observed one registers its level
  (`Web.observed_level_registers`). Observing more distinguishes more
  (`Web.RegistersAlikeUpTo.of_obs`). The base observation is support only (`supportOnly`). In the
  one-kind reading a formation's own standing then registers through support where it bears on
  itself (`Web.SelfBearing`); a gauge of its own standing (`ownStanding`) is an observation
  premise, as a gauge of a stock is.
* **Refutation.** A claim about level histories is refuted by a formation at a step when no
  history meeting it is registered alike up to that step (`Web.Refutes`), and relative to a model,
  a class of admissible histories, when no admissible history meeting it is (`Web.RefutesWithin`):
  the refutation of the model and the claim together (`Web.refutesWithin_iff_conjunction`). A
  claim is refuted only through a difference in what registers (`Web.Refutes.not_of_alike`); what
  holds is never refuted, and within a model only where the model admits what holds
  (`Web.Refutes.not_meets`, `Web.RefutesWithin.not_meets`); a refutation stands at every later
  step (`Web.Refutes.later`); observing more refutes more (`Web.Refutes.widen`). Without a model,
  no finite record refutes a claim about what follows it (`Web.tail_unrefuted`). With a model of
  the exchange, a formation observing a stock refutes at the first step every false claim that it
  comes to nothing (`Flow.refutes_tail_within`); a wrong model refutes what holds
  (`Stationary.model_error`), and registration refutes the model (`Stationary.model_refuted`). A
  formation's belief is the histories it registers alike with the actual one
  (`Web.Belief`, `Web.belief_refutes_iff`); a judgment from it is a common response of
  `Becoming.Inquiry`, kept as later steps and more observation narrow the belief
  (`Web.belief_judge_iff`, `Web.belief_judge_later`, `Web.belief_judge_widen`).
* **Reach blindness.** A formation registers a condition when it depends on it or observes it
  (`Web.Registers`). The registration closure is the closure under exchanging with a condition
  registered (`Flow.WithinRegistration`). It holds the influence closure of `Becoming.Feedback`,
  is that closure where the formation registers support only, and grows with observation and
  with exchange (`Flow.withinRegistration_of_withinInfluence`,
  `Flow.withinRegistration_supportOnly`, `Flow.withinRegistration_mono_obs`,
  `Flow.withinRegistration_mono_flow`). Let two flows with the same formations present balance on
  each condition the members of a region register (`Flow.BalancesOn`), let the region be closed
  in both under being affected through what is registered, let the levels start alike on what its
  members register, and let each member's exchange on what members register follow its own
  registration. Then every member registers alike at every step, whatever is done beyond the
  region or on what no member registers (`Flow.alike_within_closed`,
  `Flow.alike_within_registration`). With the rest of the exchange fixed this is P42's form for
  every observation (`Flow.unregistered_beyond_registration`): no claim met by the levels without
  a part beyond the closure is refuted within it, a refutation there rests on a model of the
  part's exchange, and a judgment there holds with and without the part
  (`Flow.unrefuted_beyond_registration`, `Flow.beyond_needs_model`, `Flow.belief_judge_beyond`).
* **Testing is relational.** In `Clearing` the clearer registers alike at every step whether or
  not its clearing ends the dweller (`Clearing.alike_for_clearer`, an instance of
  `alike_within_closed`). In the spared world the claim that the dweller is ended is refuted by
  the dweller at the third step and by the clearer at no step (`Clearing.tested_by_dweller`); a
  claim neither refutes, the two together refute (`Clearing.pooled`); with a model fixing the
  start and the exchange, the clearer refutes what it does not register, and its registration
  does no work (`Clearing.model_idles_registration`).
* **Threshold blindness.** Let two flows balance on each condition `g` registers, the exchange
  there following `g`'s registration (`Flow.ExchangeFollows`). While `g` registers alike, every
  difference on a condition it registers stays as it was at the start (`Flow.difference_kept`).
  Where the second web starts at least as high on what `g` registers and alike on what it
  observes, `g` registers alike at every step before which the first web supported it
  (`Flow.alike_while_supported`), and a difference changes only after a step at which the second
  web admitted `g` and the first did not support it (`Flow.difference_changes_after_divergence`).
  For one stock `d` higher that `g` depends on and does not observe: it stands `d` higher, and
  `g` registers alike, at every step before which the first web supported `g` at every step
  (`Flow.subthreshold_alike`, `Flow.subthreshold_alike_always`). Both webs failing together, the difference can stay
  for ever (`JointFailure.difference_kept`). `SupportDrawn` is a witness in which the difference
  changes (`SupportDrawn.difference_waits`). Observing the stock lifts this: the formation of
  `Gauged` registers the two webs apart at the first step and draws on the higher stock while
  supported in both (`Gauged.gauge_changes_difference`). Where others respond to the stock itself
  the hypothesis fails, and the higher stock can end `g` first (`Attracting.higher_breaks_first`).
  On a prey that bears on itself, a bite registers through support only where it brings the prey
  below its need, and a gauge of itself registers every bite (`SelfPrey.threshold_on_oneself`).
* **Horizon.** Where the continuation is open, as in `Renewable`, no reading decided by the first
  `h` steps of a run is the whole-run classification (`Renewable.no_exact_finite_reading`); one
  that credits no consuming run withholds credit from a renewing one
  (`Renewable.finite_reading_withholds_renewal`). Both are corollaries of
  `Renewable.prefix_does_not_decide`, beside `Renewable.finite_reading_credits_consumption`.

**Readings (the AI's; Ren accepted their earlier wording on 11 October 2026, and the review
narrowed them).**
- Feedback through support has three blindnesses, each in its scope: below a threshold, where the
  exchange follows registration (`subthreshold_alike`); beyond the horizon, where the continuation
  is open (`Becoming.Horizon`); and beyond the registration closure (`alike_within_closed`). They
  are not the only ones: support registers only net exchange (`Flow.Balances.agrees_iff_even`),
  and one joint bit across the conditions required.
- A runaway is a loop that runs inside one of them. This is a heuristic, not a statement: no loop
  or gain is defined, and where others respond to a stock its loss can register sooner
  (`Attracting`).
- Measurement registers a level below the threshold (`Web.observed_level_registers`); a model of
  the exchange crosses the horizon relative to itself and answers to registration
  (`Flow.refutes_tail_within`, `Stationary`); new observation and new exchange widen the closure
  (`Flow.withinRegistration_mono_obs`, `Flow.withinRegistration_mono_flow`); others' registration
  tests what one cannot (`Clearing.tested_by_dweller`, `Clearing.pooled`), and reaches one only
  through a relation that is itself an exchange or an observation.
- Falsifiability is the condition of being corrected by the unfolding: a claim and its rivals
  must differ in what can register (`Web.Refutes.not_of_alike`). It is relational and moves with
  what is registered. Without a model no finite record tests a claim about what follows it; with
  one, the test is of the model and the claim together.
- Read with Ren's 心 and 理, 理 is a model answerable to registration: it narrows the histories
  admitted, so that the same registration decides more; it can mislead, and registration corrects
  it.

What is not derived:
- that a formation observes anything beyond its support, gauges its own standing, forms a model,
  or wants to avoid a runaway;
- what a registration is about: registering alike bounds what can be told apart, and says nothing
  of what a difference signifies;
- what an act does: a claim about it compares two histories, and is tested only relative to a
  model of the history without the act (`Flow.beyond_needs_model`,
  `Clearing.model_idles_registration`); varying one's own act and registering the difference is
  open;
- which laws hold of the actual unfolding;
- how others respond: `Flow.ExchangeFollows`, and the response hypothesis of
  `alike_within_closed`, are supplied, and the comparison with a part withheld holds the rest of
  the exchange fixed.

Activity is supplied by the representation, not produced by the exchange, so it is not counted
as registered; under `Web.Dependent` it cannot outrun support. Balance is assumed only on the
conditions registered, at each step (`Flow.BalancesOn`); global balance gives it
(`Flow.Balances.on`). The representation commits to discrete steps and natural quantities.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

variable {F C : Type}

/-! ## Registration and refutation -/

/-- No level is observed: a formation registers its support only. In the one-kind reading its own
standing then registers through support where it bears on itself (`Web.SelfBearing`). -/
def supportOnly : F → C → Prop := fun _ _ => False

/-- In the one-kind reading, a gauge of one's own standing: an observation premise, as a gauge of
a stock is, not given by the identification of the two roles. -/
def ownStanding {X : Type} : X → X → Prop := fun g c => c = g

/-- A stock other than oneself is not one's own standing. -/
theorem ownStanding_other {X : Type} {g c : X} (other : c ≠ g) : ¬ ownStanding g c :=
  other

/-- Belief narrows where the believed histories do. -/
theorem sees_narrow {X : Type} {B B' : X → Prop} (narrower : ∀ x, B' x → B x) :
    ∀ s, sees B' s → sees B s
  | _, ⟨x, believed, same⟩ => ⟨x, narrower x believed, same⟩

/-- `a + x = b + y` and `x ≤ y` give `b ≤ a`. -/
theorem le_of_add_eq_of_le {a b x y : Nat} (same : a + x = b + y) (le : x ≤ y) : b ≤ a :=
  le_of_add_le_add_right x (Nat.le_trans (Nat.add_le_add_left le b) (Nat.le_of_eq same.symm))

/-- `a + x = b + y` and `x = y` give `b = a`. -/
theorem eq_of_add_eq_of_eq {a b x y : Nat} (same : a + x = b + y) (eq : x = y) : b = a :=
  (add_right_cancel x (same.trans (congrArg (b + ·) eq.symm))).symm

/-- The record `l` up to `t`, then the level `k` on `c`. -/
def recordThen [DecidableEq C] (l : Nat → C → Nat) (t : Nat) (c : C) (k : Nat) :
    Nat → C → Nat :=
  fun s e => if s ≤ t then l s e else if e = c then k else l s e

namespace Web

variable (W : Web F C)

/-- Under two level histories, `g` registers alike at `t`: the levels admit it alike, and the
conditions it observes stand alike. -/
def RegistersAlike (obs : F → C → Prop) (g : F) (l l' : Nat → C → Nat) (t : Nat) : Prop :=
  (W.Admits (l t) t g ↔ W.Admits (l' t) t g) ∧ ∀ c, obs g c → l t c = l' t c

/-- `g` registers alike at every step up to `t`. -/
def RegistersAlikeUpTo (obs : F → C → Prop) (g : F) (l l' : Nat → C → Nat) (t : Nat) : Prop :=
  ∀ s, s ≤ t → W.RegistersAlike obs g l l' s

/-- A claim about level histories is refuted by `g` at `t` under `l` when no history meeting the
claim is registered alike by `g` up to `t`. For a formation without inquiry, read: its
registration excludes the claim. -/
def Refutes (obs : F → C → Prop) (claim : (Nat → C → Nat) → Prop) (g : F)
    (l : Nat → C → Nat) (t : Nat) : Prop :=
  ∀ l', claim l' → ¬ W.RegistersAlikeUpTo obs g l l' t

/-- Refuted relative to a model, the histories it admits: no admitted history meeting the claim
is registered alike by `g` up to `t`. -/
def RefutesWithin (admitted : (Nat → C → Nat) → Prop) (obs : F → C → Prop)
    (claim : (Nat → C → Nat) → Prop) (g : F) (l : Nat → C → Nat) (t : Nat) : Prop :=
  ∀ l', admitted l' → claim l' → ¬ W.RegistersAlikeUpTo obs g l l' t

/-- A condition enters what registers in `g` when `g` depends on it, through the threshold of
its support, or observes it, through its level. -/
def Registers (obs : F → C → Prop) (g : F) (c : C) : Prop :=
  W.DependsOn g c ∨ obs g c

/-- `g`'s belief at `t` under `l`: the histories it registers alike with `l` up to `t`. -/
def Belief (obs : F → C → Prop) (g : F) (l : Nat → C → Nat) (t : Nat) :
    (Nat → C → Nat) → Prop :=
  fun l' => W.RegistersAlikeUpTo obs g l l' t

/-- Every member of a group registers alike up to `t`. -/
def RegistersAlikeAll (obs : F → C → Prop) (group : F → Prop) (l l' : Nat → C → Nat)
    (t : Nat) : Prop :=
  ∀ g, group g → W.RegistersAlikeUpTo obs g l l' t

/-- A group refutes a claim when no history meeting it is registered alike by all its members. -/
def RefutesBy (obs : F → C → Prop) (claim : (Nat → C → Nat) → Prop) (group : F → Prop)
    (l : Nat → C → Nat) (t : Nat) : Prop :=
  ∀ l', claim l' → ¬ W.RegistersAlikeAll obs group l l' t

/-- At `t`, `W'` stands at least as high as `W` on every condition `g` registers, and alike on
every condition it observes. -/
def LevelsAtLeast (W' : Web F C) (obs : F → C → Prop) (g : F) (t : Nat) : Prop :=
  (∀ e, W.Registers obs g e → W.level t e ≤ W'.level t e) ∧
    ∀ e, obs g e → W.level t e = W'.level t e

variable {W} {obs obs' : F → C → Prop} {g : F} {l l' : Nat → C → Nat}

/-- Every history registers alike with itself. -/
theorem RegistersAlike.refl (t : Nat) : W.RegistersAlike obs g l l t :=
  ⟨Iff.rfl, fun _ _ => rfl⟩

/-- Registering alike is symmetric. -/
theorem RegistersAlike.symm {t : Nat} (alike : W.RegistersAlike obs g l l' t) :
    W.RegistersAlike obs g l' l t :=
  ⟨alike.1.symm, fun c observed => (alike.2 c observed).symm⟩

/-- Registering alike up to a step is symmetric. -/
theorem RegistersAlikeUpTo.symm {t : Nat} (alike : W.RegistersAlikeUpTo obs g l l' t) :
    W.RegistersAlikeUpTo obs g l' l t :=
  fun s le => (alike s le).symm

/-- Alike up to a step, alike up to every earlier step. -/
theorem RegistersAlikeUpTo.earlier {s t : Nat} (alike : W.RegistersAlikeUpTo obs g l l' t)
    (le : s ≤ t) : W.RegistersAlikeUpTo obs g l l' s :=
  fun r le' => alike r (Nat.le_trans le' le)

/-- Observing more distinguishes more: histories alike under a larger observation are alike
under a smaller one. -/
theorem RegistersAlikeUpTo.of_obs (larger : ∀ g c, obs g c → obs' g c) {t : Nat}
    (alike : W.RegistersAlikeUpTo obs' g l l' t) : W.RegistersAlikeUpTo obs g l l' t :=
  fun s le => ⟨(alike s le).1, fun c observed => (alike s le).2 c (larger g c observed)⟩

/-- Histories agreeing up to `t` are registered alike up to `t`. -/
theorem registersAlikeUpTo_of_agree {t : Nat} (agree : ∀ s, s ≤ t → ∀ e, l' s e = l s e) :
    W.RegistersAlikeUpTo obs g l l' t :=
  fun s le => ⟨⟨fun admits c requires => Nat.le_trans (admits c requires)
      (Nat.le_of_eq (agree s le c).symm),
    fun admits c requires => Nat.le_trans (admits c requires) (Nat.le_of_eq (agree s le c))⟩,
   fun c _ => (agree s le c).symm⟩

/-- **What registers of one condition: its threshold.** With every other condition `g` registers
alike at `s`, a condition `g` depends on and does not observe registers only whether it meets the
need: meeting it under both histories or under neither, `g` registers alike, whatever the two
levels are. -/
theorem alike_of_threshold [DecidableEq C] {c : C} {s : Nat} (unobserved : ¬ obs g c)
    (others : ∀ e, W.Registers obs g e → e ≠ c → l s e = l' s e)
    (threshold : W.requires s g c → (W.need s g c ≤ l s c ↔ W.need s g c ≤ l' s c)) :
    W.RegistersAlike obs g l l' s :=
  ⟨⟨fun admits e requires => match decEq e c with
      | isTrue same => match e, same, requires with
        | _, rfl, requires => (threshold requires).mp (admits _ requires)
      | isFalse other => Nat.le_trans (admits e requires)
          (Nat.le_of_eq (others e (.inl ⟨s, requires⟩) other)),
    fun admits e requires => match decEq e c with
      | isTrue same => match e, same, requires with
        | _, rfl, requires => (threshold requires).mpr (admits _ requires)
      | isFalse other => Nat.le_trans (admits e requires)
          (Nat.le_of_eq (others e (.inl ⟨s, requires⟩) other).symm)⟩,
   fun e observed => others e (.inr observed) fun same => unobserved (same ▸ observed)⟩

/-- **What registers of one condition: its level, where observed.** Any difference in an observed
condition at `s` is registered. -/
theorem observed_level_registers {c : C} {s : Nat} (observed : obs g c)
    (differ : l s c ≠ l' s c) : ¬ W.RegistersAlike obs g l l' s :=
  fun alike => differ (alike.2 c observed)

/-- A claim is refuted only through a difference in what registers: where a history meeting it
is registered alike up to a step, it is not refuted there. -/
theorem Refutes.not_of_alike {claim : (Nat → C → Nat) → Prop} {t : Nat} (meets : claim l')
    (alike : W.RegistersAlikeUpTo obs g l l' t) : ¬ W.Refutes obs claim g l t :=
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

/-- A claim met by a history that agrees with the record up to `t` is not refuted at `t`. -/
theorem Refutes.not_of_extension {claim : (Nat → C → Nat) → Prop} {t : Nat}
    (extension : ∃ m, claim m ∧ ∀ s, s ≤ t → ∀ e, m s e = l s e) :
    ¬ W.Refutes obs claim g l t :=
  match extension with
  | ⟨_, meets, agree⟩ => Refutes.not_of_alike meets (registersAlikeUpTo_of_agree agree)

/-- **Without a model, a finite record leaves what follows open.** For every record up to `t`,
neither the claim that a condition comes to nothing nor the claim that it stays above nothing
after `t` is refuted at `t`, by any formation under any observation. -/
theorem tail_unrefuted [DecidableEq C] {t : Nat} (c : C) :
    ¬ W.Refutes obs (fun m => ∃ T, m T c = 0) g l t ∧
      ¬ W.Refutes obs (fun m => ∀ T, t < T → 0 < m T c) g l t :=
  have agree : ∀ k, ∀ s, s ≤ t → ∀ e, recordThen l t c k s e = l s e := fun _ _ le _ =>
    if_pos le
  have after : ∀ k T, t < T → recordThen l t c k T c = k := fun _ _ later =>
    (if_neg (Nat.not_le_of_lt later)).trans (if_pos rfl)
  ⟨Refutes.not_of_extension ⟨recordThen l t c 0,
      ⟨t + 1, after 0 (t + 1) (Nat.lt_succ_self t)⟩, agree 0⟩,
   Refutes.not_of_extension ⟨recordThen l t c 1, fun T later =>
      Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq (after 1 T later).symm), agree 1⟩⟩

/-- Refutation is refutation relative to the model admitting every history. -/
theorem refutes_iff_refutesWithin_all {claim : (Nat → C → Nat) → Prop} {t : Nat} :
    W.Refutes obs claim g l t ↔ W.RefutesWithin (fun _ => True) obs claim g l t :=
  ⟨fun refutes l' _ meets => refutes l' meets, fun refutes l' meets => refutes l' trivial meets⟩

/-- Refutation within a model is refutation of the model and the claim together. -/
theorem refutesWithin_iff_conjunction {admitted : (Nat → C → Nat) → Prop}
    {claim : (Nat → C → Nat) → Prop} {t : Nat} :
    W.RefutesWithin admitted obs claim g l t ↔
      W.Refutes obs (fun l' => admitted l' ∧ claim l') g l t :=
  ⟨fun refutes l' ⟨inside, meets⟩ => refutes l' inside meets,
   fun refutes l' inside meets => refutes l' ⟨inside, meets⟩⟩

/-- A narrower model refutes more. -/
theorem RefutesWithin.narrow {admitted admitted' : (Nat → C → Nat) → Prop}
    (narrower : ∀ l, admitted' l → admitted l) {claim : (Nat → C → Nat) → Prop} {t : Nat}
    (refutes : W.RefutesWithin admitted obs claim g l t) :
    W.RefutesWithin admitted' obs claim g l t :=
  fun l' inside meets => refutes l' (narrower l' inside) meets

/-- Within a model admitting what holds, what holds is never refuted. -/
theorem RefutesWithin.not_meets {admitted : (Nat → C → Nat) → Prop}
    {claim : (Nat → C → Nat) → Prop} {t : Nat} (actual : admitted l)
    (refutes : W.RefutesWithin admitted obs claim g l t) : ¬ claim l :=
  fun meets => refutes l actual meets fun _ _ => RegistersAlike.refl _

/-- A group refutes what any member refutes. -/
theorem RefutesBy.of_member {claim : (Nat → C → Nat) → Prop} {group : F → Prop} {t : Nat}
    (member : group g) (refutes : W.Refutes obs claim g l t) : W.RefutesBy obs claim group l t :=
  fun l' meets all => refutes l' meets (all g member)

/-- Refutation is a claim disjoint from the belief. -/
theorem belief_refutes_iff {claim : (Nat → C → Nat) → Prop} {t : Nat} :
    W.Refutes obs claim g l t ↔ ∀ l', W.Belief obs g l t l' → ¬ claim l' :=
  ⟨fun refutes l' believed meets => refutes l' meets believed,
   fun disjoint l' meets believed => disjoint l' believed meets⟩

variable {H : Type} {admissible : (Nat → C → Nat) → H → Prop} {a : H}

/-- **The bridge to `Becoming.Inquiry`.** A judgment from a formation's registration is a common
response over its belief: admissible at every history it registers alike with the actual. -/
theorem belief_judge_iff {t : Nat} :
    CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True) (fun a => [a])
        (sees (W.Belief obs g l t)) a ↔ ∀ l', W.RegistersAlikeUpTo obs g l l' t → admissible l' a :=
  commonResponse_judge_iff

/-- Later steps narrow the belief and keep every common response. -/
theorem belief_judge_later {t t' : Nat} (le : t ≤ t')
    (common : CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True)
      (fun a => [a]) (sees (W.Belief obs g l t)) a) :
    CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True) (fun a => [a])
      (sees (W.Belief obs g l t')) a :=
  commonResponse_antitone (sees_narrow fun _ alike => alike.earlier le) common

/-- More observation narrows the belief and keeps every common response. -/
theorem belief_judge_widen (larger : ∀ g c, obs g c → obs' g c) {t : Nat}
    (common : CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True)
      (fun a => [a]) (sees (W.Belief obs g l t)) a) :
    CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True) (fun a => [a])
      (sees (W.Belief obs' g l t)) a :=
  commonResponse_antitone (sees_narrow fun _ alike => alike.of_obs larger) common

/-- Webs agreeing on what `g` requires and needs register its support through admission by their
levels. -/
theorem admits_iff_supported_of_agree {W' : Web F C}
    (requires : ∀ t c, W.requires t g c ↔ W'.requires t g c)
    (need : ∀ t c, W.need t g c = W'.need t g c) (t : Nat) :
    W.Admits (W'.level t) t g ↔ W'.Supported t g :=
  ⟨fun admits c requires' =>
     Nat.le_trans (Nat.le_of_eq (need t c).symm) (admits c ((requires t c).mpr requires')),
   fun supported c requires'' =>
     Nat.le_trans (Nat.le_of_eq (need t c)) (supported c ((requires t c).mp requires''))⟩

/-- Where `W'` stands at least as high on what `g` registers and alike on what it observes,
registering alike at a step is exactly: wherever the levels of `W'` admit `g`, `W` supports it. -/
theorem registersAlike_iff_of_levelsAtLeast {W' : Web F C} {t : Nat}
    (above : W.LevelsAtLeast W' obs g t) :
    W.RegistersAlike obs g W.level W'.level t ↔ (W.Admits (W'.level t) t g → W.Supported t g) :=
  ⟨fun alike => alike.1.mpr,
   fun back => ⟨⟨fun supported e requires =>
       Nat.le_trans (supported e requires) (above.1 e (.inl ⟨t, requires⟩)), back⟩,
     above.2⟩⟩

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

/-- Affected through what is registered, in either of two flows. -/
def RegisteredFromEither (L' : Flow F C) (obs : F → C → Prop) (g h : F) : Prop :=
  L.RegisteredFrom W obs g h ∨ L'.RegisteredFrom W obs g h

/-- The exchange on what `g` registers follows `g`'s registration: wherever `g` registers alike
up to `t`, the two flows take from and give to every condition `g` registers alike across the
step from `t`, in total over every formation present. A hypothesis on the whole exchange around
`g`: it excludes others responding to what `g` does not register. -/
def ExchangeFollows (L' : Flow F C) (W' : Web F C) (obs : F → C → Prop) (g : F) : Prop :=
  ∀ t, W.RegistersAlikeUpTo obs g W.level W'.level t → ∀ c, W.Registers obs g c →
    L.taken t c = L'.taken t c ∧ L.given t c = L'.given t c

/-- `l` is a level history of the flow: across every step each condition gains what is given to
it and loses what is taken from it. A model of the exchange. -/
def BalancedHistory (l : Nat → C → Nat) : Prop :=
  ∀ s e, l (s + 1) e + L.taken s e = l s e + L.given s e

variable {L W} {L' : Flow F C} {W' : Web F C} {obs obs' : F → C → Prop} {part : F → Bool}
  {g : F}

/-- A balanced flow's levels are a level history of it. -/
theorem balancedHistory_iff : L.BalancedHistory W.level ↔ L.Balances W :=
  Iff.rfl

/-- Two level histories of one flow that start alike on a condition stay alike on it. -/
theorem BalancedHistory.agree {l l' : Nat → C → Nat} {c : C} (history : L.BalancedHistory l)
    (history' : L.BalancedHistory l') (start : l 0 c = l' 0 c) : ∀ s, l s c = l' s c
  | 0 => start
  | s + 1 => add_right_cancel (L.taken s c)
      ((history s c).trans ((congrArg (· + L.given s c) (BalancedHistory.agree history history'
        start s)).trans (history' s c).symm))

/-- **A model of the exchange crosses the horizon.** Relative to the level histories of a flow, a
formation observing a stock refutes at the first step every false claim that the stock comes to
nothing. -/
theorem refutes_tail_within {l : Nat → C → Nat} {c : C} (observed : obs g c)
    (history : L.BalancedHistory l) (never : ∀ T, ¬ l T c = 0) :
    W.RefutesWithin L.BalancedHistory obs (fun l' => ∃ T, l' T c = 0) g l 0 :=
  fun _ history' ⟨T, zero⟩ alike =>
    never T ((BalancedHistory.agree history history' ((alike 0 (Nat.le_refl 0)).2 c observed)
      T).trans zero)

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

/-- The registration closure grows with observation. -/
theorem withinRegistration_mono_obs (larger : ∀ g c, obs g c → obs' g c) {f g : F}
    (within : L.WithinRegistration W obs f g) : L.WithinRegistration W obs' f g :=
  WithinClosure.mono (fun _ _ ⟨c, registers, exchanges⟩ =>
    ⟨c, registers.imp id (larger _ c), exchanges⟩) within

/-- The registration closure grows with exchange. -/
theorem withinRegistration_mono_flow (more : ∀ h c, L.Exchanges h c → L'.Exchanges h c)
    {f g : F} (within : L.WithinRegistration W obs f g) : L'.WithinRegistration W obs f g :=
  WithinClosure.mono (fun _ _ ⟨c, registers, exchanges⟩ =>
    ⟨c, registers, more _ c exchanges⟩) within

/-- Nothing beyond a formation's registration closure exchanges with a condition registered
within it. -/
theorem beyond_registration {f g h : F} (within : L.WithinRegistration W obs f g)
    (beyond : ¬ L.WithinRegistration W obs f h) {c : C} (registers : W.Registers obs g c) :
    ¬ L.Exchanges h c :=
  fun exchanges => WithinClosure.not_rel within beyond ⟨c, registers, exchanges⟩

/-- Within a region closed in both flows under being affected through what is registered, each
formation's exchange on a condition a member registers agrees in the two flows wherever the
members' does: a formation exchanging there is a member. -/
theorem exchange_agrees_within {region : F → Prop} {h : F} {c : C} {t : Nat}
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

/-- **Reach blindness where the members respond.** Take two flows with the same formations
present, balancing on each condition a member registers, and a region closed in both under being
affected through what is registered.
Let the levels start alike on everything a member registers, and let each member take from and
give to what the members register alike in the two flows wherever it has registered alike. Then
every member registers alike at every step, whatever differs beyond the region, in what members
do with conditions no member registers, or in levels no member registers. -/
theorem alike_within_closed {region : F → Prop}
    (balanced : ∀ t g c, region g → W.Registers obs g c → L.BalancesOn W [c] t)
    (balanced' : ∀ t g c, region g → W.Registers obs g c → L'.BalancesOn W' [c] t)
    (closed : ClosedUnder (L.RegisteredFrom W obs) region)
    (closed' : ClosedUnder (L'.RegisteredFrom W obs) region)
    (present : ∀ t, L.present t = L'.present t)
    (start : ∀ g, region g → ∀ c, W.Registers obs g c → W.level 0 c = W'.level 0 c)
    (responds : ∀ h, region h → ∀ t, W.RegistersAlikeUpTo obs h W.level W'.level t →
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
          have upTo : ∀ h, region h → W.RegistersAlikeUpTo obs h W.level W'.level t :=
            fun h inside r le' => alikeOf r (ih r le') h inside
          have each : ∀ h, h ∈ L.present t →
              L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c := fun h mem =>
            exchange_agrees_within closed closed' (present t) member registers mem
              fun inside => responds h inside t (upTo h inside) g c member registers
          have taken : L.taken t c = L'.taken t c :=
            (total_congr_on fun h mem => (each h mem).1).trans
              (congrArg (fun as => total as fun h => L'.take t h c) (present t))
          have given : L.given t c = L'.given t c :=
            (total_congr_on fun h mem => (each h mem).2).trans
              (congrArg (fun as => total as fun h => L'.give t h c) (present t))
          have now := ih t (Nat.le_refl t) g member c registers
          add_right_cancel (L.taken t c)
            ((balanced t g c member registers c (.head _)).trans
              ((congrArg (· + L.given t c) now).trans
                ((congrArg (W'.level t c + ·) given).trans
                  ((balanced' t g c member registers c (.head _)).symm.trans
                    (congrArg (W'.level (t + 1) c + ·) taken.symm))))))
      t
  fun t g member => alikeOf t (levels t t (Nat.le_refl t)) g member

/-- Reach blindness where the members respond, for `f`'s registration closure drawn through both
flows. -/
theorem alike_within_registration {f : F}
    (balanced : ∀ t g c, WithinClosure (L.RegisteredFromEither W L' obs) f g →
      W.Registers obs g c → L.BalancesOn W [c] t)
    (balanced' : ∀ t g c, WithinClosure (L.RegisteredFromEither W L' obs) f g →
      W.Registers obs g c → L'.BalancesOn W' [c] t)
    (present : ∀ t, L.present t = L'.present t)
    (start : ∀ g, WithinClosure (L.RegisteredFromEither W L' obs) f g →
      ∀ c, W.Registers obs g c → W.level 0 c = W'.level 0 c)
    (responds : ∀ h, WithinClosure (L.RegisteredFromEither W L' obs) f h →
      ∀ t, W.RegistersAlikeUpTo obs h W.level W'.level t →
      ∀ g c, WithinClosure (L.RegisteredFromEither W L' obs) f g → W.Registers obs g c →
        L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c) :
    ∀ t g, WithinClosure (L.RegisteredFromEither W L' obs) f g →
      W.RegistersAlike obs g W.level W'.level t :=
  alike_within_closed balanced balanced'
    (fun _ _ within related => within.trans (WithinClosure.of_rel (.inl related)))
    (fun _ _ within related => within.trans (WithinClosure.of_rel (.inr related)))
    present start responds

/-- A positive amount withheld is a positive amount of the flow. -/
theorem pos_of_withheld_pos {b : Bool} {q : Nat} (pos : 0 < (if b then 0 else q)) : 0 < q :=
  match b, pos with
  | false, pos => pos
  | true, pos => absurd pos (Nat.lt_irrefl 0)

/-- Outside the part, withholding leaves an amount as it is. -/
theorem withheld_eq_of_false {b : Bool} (no : b = false) (q : Nat) :
    (if b then 0 else q) = q :=
  match b, no with
  | false, _ => rfl

/-- The flow with a part withheld exchanges only where the flow does. -/
theorem withhold_exchanges {h : F} {c : C} : (L.withhold part).Exchanges h c → L.Exchanges h c
  | ⟨t, mem, .inl pos⟩ => ⟨t, mem, .inl (pos_of_withheld_pos (b := part h) (q := L.take t h c) pos)⟩
  | ⟨t, mem, .inr pos⟩ => ⟨t, mem, .inr (pos_of_withheld_pos (b := part h) (q := L.give t h c) pos)⟩

/-- **Reach blindness with the rest of the exchange fixed.** Where every member of a part lies
beyond `f`'s registration closure, each formation within the closure registers alike with and
without the part at every step: an instance of `alike_within_closed`, whose second flow is the
flow with the part withheld. Registering support only, this is P42's
`unregistered_beyond_influence`. -/
theorem unregistered_beyond_registration {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {f : F}
    (balanced : ∀ t g c, L.WithinRegistration W obs f g → W.Registers obs g c →
      L.BalancesOn W [c] t)
    (beyond : ∀ h, part h = true → ¬ L.WithinRegistration W obs f h) :
    ∀ t g, L.WithinRegistration W obs f g → W.RegistersAlike obs g W.level l t :=
  have closed : ClosedUnder (L.RegisteredFrom W obs) (L.WithinRegistration W obs f) :=
    closedUnder_withinClosure f
  have closed' : ClosedUnder ((L.withhold part).RegisteredFrom W obs)
      (L.WithinRegistration W obs f) :=
    fun g h within ⟨c, registers, exchanges⟩ =>
      closed g h within ⟨c, registers, withhold_exchanges exchanges⟩
  fun t g within =>
    alike_within_closed (W' := { W with level := l }) balanced
      (fun t _ _ _ _ c' _ => without.1 t c') closed closed' (fun _ => rfl)
      (fun _ _ c _ => (without.2 c).symm)
      (fun h inside _ _ _ _ _ _ =>
        have notPart : part h = false := match part h, beyond h with
          | false, _ => rfl
          | true, no => absurd inside (no rfl)
        ⟨(withheld_eq_of_false notPart _).symm, (withheld_eq_of_false notPart _).symm⟩)
      t g within

/-- What a part beyond the registration closure does cannot be tested within it: no claim met by
the levels without the part is refuted, at any step, by a formation within the closure. -/
theorem unrefuted_beyond_registration {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {f : F}
    (balanced : ∀ t g c, L.WithinRegistration W obs f g → W.Registers obs g c →
      L.BalancesOn W [c] t)
    (beyond : ∀ h, part h = true → ¬ L.WithinRegistration W obs f h)
    {claim : (Nat → C → Nat) → Prop} (meets : claim l) :
    ∀ t g, L.WithinRegistration W obs f g → ¬ W.Refutes obs claim g W.level t :=
  fun _ g within => Web.Refutes.not_of_alike meets fun s _ =>
    unregistered_beyond_registration without balanced beyond s g within

/-- **Beyond the registration closure, only a model can judge.** Where a formation within the
closure refutes a claim relative to a model, the model and the claim together exclude the levels
without a part beyond it: the refutation rests on a model of the part's exchange. -/
theorem beyond_needs_model {l₀ : Nat → C → Nat}
    (without : L.WithheldLevels part W l₀) {f : F}
    (balanced : ∀ t g c, L.WithinRegistration W obs f g → W.Registers obs g c →
      L.BalancesOn W [c] t)
    (beyond : ∀ h, part h = true → ¬ L.WithinRegistration W obs f h)
    (within : L.WithinRegistration W obs f g) {admitted : (Nat → C → Nat) → Prop}
    {claim : (Nat → C → Nat) → Prop} {t : Nat}
    (refutes : W.RefutesWithin admitted obs claim g W.level t) : ¬ (admitted l₀ ∧ claim l₀) :=
  fun ⟨inside, meets⟩ => refutes l₀ inside meets fun s _ =>
    unregistered_beyond_registration without balanced beyond s g within

/-- A judgment from within the registration closure holds with and without a part beyond it:
every response common to the belief is admissible under both levels. -/
theorem belief_judge_beyond {H : Type} {admissible : (Nat → C → Nat) → H → Prop} {a : H}
    {l₀ : Nat → C → Nat} (without : L.WithheldLevels part W l₀) {f : F}
    (balanced : ∀ t g c, L.WithinRegistration W obs f g → W.Registers obs g c →
      L.BalancesOn W [c] t)
    (beyond : ∀ h, part h = true → ¬ L.WithinRegistration W obs f h)
    (within : L.WithinRegistration W obs f g) {t : Nat}
    (common : CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True)
      (fun a => [a]) (sees (W.Belief obs g W.level t)) a) :
    admissible W.level a ∧ admissible l₀ a :=
  ⟨Web.belief_judge_iff.mp common W.level fun s _ => Web.RegistersAlike.refl s,
   Web.belief_judge_iff.mp common l₀ fun s _ =>
     unregistered_beyond_registration without balanced beyond s g within⟩

/-! ## Threshold blindness: a difference persists until support diverges -/

/-- **Differences kept.** While `g` registers alike, exchange following its registration keeps
every difference on a condition it registers as it was at the start. -/
theorem difference_kept
    (balanced : ∀ t e, W.Registers obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.Registers obs g e → L'.BalancesOn W' [e] t)
    (follows : L.ExchangeFollows W L' W' obs g) :
    ∀ t, (∀ s, s < t → W.RegistersAlike obs g W.level W'.level s) →
      ∀ e, W.Registers obs g e → W'.level t e + W.level 0 e = W.level t e + W'.level 0 e
  | 0, _, _, _ => Nat.add_comm _ _
  | t + 1, alike, e, registers =>
    have ih := difference_kept balanced balanced' follows t
      (fun s before => alike s (Nat.lt_succ_of_lt before)) e registers
    match follows t (fun s le => alike s (Nat.lt_succ_of_le le)) e registers with
    | ⟨taken, given⟩ => add_right_cancel (L.taken t e)
        (calc W'.level (t + 1) e + W.level 0 e + L.taken t e
            = W'.level (t + 1) e + L.taken t e + W.level 0 e := Nat.add_right_comm _ _ _
          _ = W'.level (t + 1) e + L'.taken t e + W.level 0 e :=
              congrArg (fun x => W'.level (t + 1) e + x + W.level 0 e) taken
          _ = W'.level t e + L'.given t e + W.level 0 e :=
              congrArg (· + W.level 0 e) (balanced' t e registers e (.head _))
          _ = W'.level t e + W.level 0 e + L'.given t e := Nat.add_right_comm _ _ _
          _ = W.level t e + W'.level 0 e + L'.given t e := congrArg (· + L'.given t e) ih
          _ = W.level t e + W'.level 0 e + L.given t e := congrArg (_ + ·) given.symm
          _ = W.level t e + L.given t e + W'.level 0 e := Nat.add_right_comm _ _ _
          _ = W.level (t + 1) e + L.taken t e + W'.level 0 e :=
              congrArg (· + W'.level 0 e) (balanced t e registers e (.head _)).symm
          _ = W.level (t + 1) e + W'.level 0 e + L.taken t e := Nat.add_right_comm _ _ _)

/-- While `g` registers alike, a second web starting at least as high on what `g` registers and
alike on what it observes still stands so. -/
theorem levelsAtLeast_while_alike
    (balanced : ∀ t e, W.Registers obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.Registers obs g e → L'.BalancesOn W' [e] t)
    (higher : ∀ e, W.Registers obs g e → W.level 0 e ≤ W'.level 0 e)
    (observedAlike : ∀ e, obs g e → W.level 0 e = W'.level 0 e)
    (follows : L.ExchangeFollows W L' W' obs g) {t : Nat}
    (alike : ∀ s, s < t → W.RegistersAlike obs g W.level W'.level s) :
    W.LevelsAtLeast W' obs g t :=
  ⟨fun e registers => le_of_add_eq_of_le (difference_kept balanced balanced' follows t alike e
      registers) (higher e registers),
   fun e observed => eq_of_add_eq_of_eq (difference_kept balanced balanced' follows t alike e
      (.inr observed)) (observedAlike e observed)⟩

/-- **Alike while supported.** A second web starting at least as high on what `g` registers and
alike on what it observes: `g` registers alike at every step before which the first web supported
it. Any number of conditions may differ. -/
theorem alike_while_supported
    (balanced : ∀ t e, W.Registers obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.Registers obs g e → L'.BalancesOn W' [e] t)
    (higher : ∀ e, W.Registers obs g e → W.level 0 e ≤ W'.level 0 e)
    (observedAlike : ∀ e, obs g e → W.level 0 e = W'.level 0 e)
    (follows : L.ExchangeFollows W L' W' obs g) :
    ∀ t, (∀ s, s < t → W.Supported s g) → ∀ s, s < t → W.RegistersAlike obs g W.level W'.level s
  | 0, _, s, before => absurd before (Nat.not_lt_zero s)
  | t + 1, supported, s, before =>
    have past := alike_while_supported balanced balanced' higher observedAlike follows t
      (fun s before => supported s (Nat.lt_succ_of_lt before))
    match Nat.lt_or_eq_of_le (Nat.le_of_lt_succ before) with
    | .inl earlier => past s earlier
    | .inr same => same ▸
        (Web.registersAlike_iff_of_levelsAtLeast (levelsAtLeast_while_alike balanced balanced'
          higher observedAlike follows past)).mpr fun _ => supported t (Nat.lt_succ_self t)

/-- **A difference changes only after a divergence.** Where a difference on a condition `g`
registers has changed by a step, the second web's levels admitted `g` and the first web did not
support it at some earlier step (not every earlier step is otherwise); where activity needs
support, `g` was not active in the first web at every earlier step. A failure of both webs
together is not a divergence. -/
theorem difference_changes_after_divergence
    (balanced : ∀ t e, W.Registers obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.Registers obs g e → L'.BalancesOn W' [e] t)
    (higher : ∀ e, W.Registers obs g e → W.level 0 e ≤ W'.level 0 e)
    (observedAlike : ∀ e, obs g e → W.level 0 e = W'.level 0 e)
    (follows : L.ExchangeFollows W L' W' obs g) {t : Nat} {e : C}
    (registers : W.Registers obs g e)
    (changed : W'.level t e + W.level 0 e ≠ W.level t e + W'.level 0 e) :
    ¬ (∀ s, s < t → (W.Admits (W'.level s) s g → W.Supported s g)) ∧
      (W.Dependent → ¬ ∀ s, s < t → W.active s g) :=
  have diverged : ¬ ∀ s, s < t → (W.Admits (W'.level s) s g → W.Supported s g) := fun never =>
    have alike : ∀ t', t' ≤ t → ∀ s, s < t' → W.RegistersAlike obs g W.level W'.level s :=
      fun t' => Nat.rec (motive := fun t' => t' ≤ t → ∀ s, s < t' →
          W.RegistersAlike obs g W.level W'.level s)
        (fun _ s before => absurd before (Nat.not_lt_zero s))
        (fun k ih le s before =>
          have past := ih (Nat.le_of_succ_le le)
          match Nat.lt_or_eq_of_le (Nat.le_of_lt_succ before) with
          | .inl earlier => past s earlier
          | .inr same => same ▸ (Web.registersAlike_iff_of_levelsAtLeast
              (levelsAtLeast_while_alike balanced balanced' higher observedAlike follows
                past)).mpr (never k (Nat.lt_of_lt_of_le (Nat.lt_succ_self k) le)))
        t'
    changed (difference_kept balanced balanced' follows t (alike t (Nat.le_refl t)) e registers)
  ⟨diverged, fun dependent active => diverged fun s before _ => dependent s g (active s before)⟩

/-- **Threshold blindness.** Let two flows balance on each condition `g` registers, the exchange
there following its registration, and start alike on every condition `g` registers except a
stock `c` that `g` depends on and does not observe, which stands `d` higher in the second. Then at every step
before which the first web supported `g` at every step, the stock stands exactly `d` higher in
the second, every other condition `g` registers stands alike, and `g` has registered alike at
every earlier step. Where the webs agree on what `g` requires and needs, registering alike is
the same support in both (`Web.admits_iff_supported_of_agree`). -/
theorem subthreshold_alike [DecidableEq C] {c : C} {d : Nat}
    (balanced : ∀ t e, W.Registers obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.Registers obs g e → L'.BalancesOn W' [e] t)
    (depends : W.DependsOn g c) (unobserved : ¬ obs g c)
    (stock : W'.level 0 c = W.level 0 c + d)
    (start : ∀ e, W.Registers obs g e → e ≠ c → W.level 0 e = W'.level 0 e)
    (follows : L.ExchangeFollows W L' W' obs g) :
    ∀ t, (∀ s, s < t → W.Supported s g) →
      W'.level t c = W.level t c + d ∧ (∀ e, W.Registers obs g e → e ≠ c →
        W.level t e = W'.level t e) ∧ ∀ s, s < t → W.RegistersAlike obs g W.level W'.level s :=
  have higher : ∀ e, W.Registers obs g e → W.level 0 e ≤ W'.level 0 e := fun e registers =>
    match decEq e c with
    | isTrue same => same ▸ Nat.le_trans (Nat.le_add_right _ d) (Nat.le_of_eq stock.symm)
    | isFalse other => Nat.le_of_eq (start e registers other)
  have observedAlike : ∀ e, obs g e → W.level 0 e = W'.level 0 e := fun e observed =>
    start e (.inr observed) fun same => unobserved (same ▸ observed)
  fun t supported =>
    have alike := alike_while_supported balanced balanced' higher observedAlike follows t
      supported
    have keep := difference_kept balanced balanced' follows t alike
    ⟨add_right_cancel (W.level 0 c) ((keep c (.inl depends)).trans
        ((congrArg (W.level t c + ·) stock).trans
          ((Nat.add_assoc _ _ _).symm.trans (Nat.add_right_comm _ _ _)))),
     fun e registers other => eq_of_add_eq_of_eq (keep e registers) (start e registers other),
     alike⟩

/-- Where the first web supports `g` at every step, the stock stands `d` higher at every step and
`g` registers alike at every step. -/
theorem subthreshold_alike_always [DecidableEq C] {c : C} {d : Nat}
    (balanced : ∀ t e, W.Registers obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.Registers obs g e → L'.BalancesOn W' [e] t)
    (depends : W.DependsOn g c) (unobserved : ¬ obs g c)
    (stock : W'.level 0 c = W.level 0 c + d)
    (start : ∀ e, W.Registers obs g e → e ≠ c → W.level 0 e = W'.level 0 e)
    (follows : L.ExchangeFollows W L' W' obs g) (supported : ∀ t, W.Supported t g) :
    ∀ t, W'.level t c = W.level t c + d ∧ W.RegistersAlike obs g W.level W'.level t :=
  fun t =>
    ⟨(subthreshold_alike balanced balanced' depends unobserved stock start follows t
        fun s _ => supported s).1,
     (subthreshold_alike balanced balanced' depends unobserved stock start follows (t + 1)
        fun s _ => supported s).2.2 t (Nat.lt_succ_self t)⟩

end Flow

/-! ## Witnesses -/

/-! ### A formation that observes its stock

It needs one unit of the stock, draws all of the stock above its need at the first step and
nothing after. In the lower web the stock stands at two, in the higher at three. -/

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

/-- **A gauge changes the difference while supported.** In the lower web (one unit above the
need) and the higher (two), the formation drawing all of the stock above its need is supported at
every step in both, and in the higher it draws on the difference: the stock no longer stands one
higher. Observing the stock, the formation registers the two webs apart at the first step, so
exchange following its registration constrains nothing there; registering its support only, the
exchange does not follow its registration. -/
theorem gauge_changes_difference :
    (flow 1).Balances (web 1) ∧ (flow 2).Balances (web 2) ∧ (web 1).Dependent ∧
      (web 2).Dependent ∧ (∀ t, (web 1).Supported t () ∧ (web 2).Supported t ()) ∧
      (web 2).level 0 () = (web 1).level 0 () + 1 ∧
      (web 2).level 1 () ≠ (web 1).level 1 () + 1 ∧
      ¬ (web 1).RegistersAlike stock () (web 1).level (web 2).level 0 ∧
      (flow 1).ExchangeFollows (web 1) (flow 2) (web 2) stock () ∧
      ¬ (flow 1).ExchangeFollows (web 1) (flow 2) (web 2) supportOnly () :=
  ⟨balances 1, balances 2, dependent 1, dependent 2,
   fun t => ⟨supported 1 t, supported 2 t⟩, rfl, fun same => absurd same (by decide),
   fun alike => absurd (alike.2 () trivial) (by decide),
   fun _ alike => absurd ((alike 0 (Nat.zero_le _)).2 () trivial) (by decide),
   fun follows => absurd
     ((follows 0 (fun s le => match s, le with
        | 0, _ => ⟨⟨fun _ => supported 2 0, fun _ => supported 1 0⟩, fun _ no => False.elim no⟩
        | _ + 1, le => absurd le (Nat.not_succ_le_zero _))
       () (.inl ⟨0, trivial⟩)).1) (by decide)⟩

/-- In `Gauged` the stock is the formation's own standing, and a gauge of its own standing is the
gauge of the stock: under `ownStanding` the formation registers the two webs apart at the first
step. A formation carved so that its reserve is its own standing is never blind below its
threshold there. -/
theorem own_is_stock :
    (∀ g c, stock g c ↔ ownStanding g c) ∧
      ¬ (web 1).RegistersAlike ownStanding () (web 1).level (web 2).level 0 :=
  ⟨fun () () => ⟨fun _ => rfl, fun _ => trivial⟩,
   fun alike => absurd (alike.2 () rfl) (by decide)⟩

end Gauged

/-! ### A formation that draws one unit while supported

It needs one unit of the stock and its exchange follows its support only: it draws one unit at
each step at which it is supported, and is active exactly then. In the lower web the stock stands
at two, in the higher at three. -/

namespace SupportDrawn

/-- The lower stock: two, one, then nothing. -/
def lowerLevel : Nat → Nat
  | 0 => 2
  | 1 => 1
  | _ + 2 => 0

/-- The higher stock: three, two, one, then nothing. -/
def higherLevel : Nat → Nat
  | 0 => 3
  | 1 => 2
  | 2 => 1
  | _ + 3 => 0

/-- One unit at each supported step of the lower web. -/
def lowerDraw : Nat → Nat
  | 0 => 1
  | 1 => 1
  | _ + 2 => 0

/-- One unit at each supported step of the higher web. -/
def higherDraw : Nat → Nat
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

theorem lower_balances : (flow lowerDraw).Balances (web lowerLevel)
  | 0, () => rfl
  | 1, () => rfl
  | _ + 2, () => rfl

theorem higher_balances : (flow higherDraw).Balances (web higherLevel)
  | 0, () => rfl
  | 1, () => rfl
  | 2, () => rfl
  | _ + 3, () => rfl

theorem dependent (level : Nat → Nat) : (web level).Dependent :=
  fun _ _ active _ _ => active

/-- The exchange follows the formation's support only. Up to the second step the two flows draw
alike; from the third, the support registers differently. -/
theorem follows : (flow lowerDraw).ExchangeFollows (web lowerLevel) (flow higherDraw)
    (web higherLevel) supportOnly ()
  | 0, _, (), _ => ⟨rfl, rfl⟩
  | 1, _, (), _ => ⟨rfl, rfl⟩
  | t + 2, alike, (), _ => absurd ((alike 2 (Nat.le_add_left 2 t)).1.mpr
      (fun _ _ => Nat.le_refl 1) () trivial) (Nat.not_succ_le_zero 0)

/-- **The difference waits for the divergence.** Through its support only, the formation
registers the higher stock as the lower before the third step, where the lower web fails to
support it and the higher does: the difference of one unit stands through the third step, as
`Flow.subthreshold_alike` gives, and has changed by the fourth. -/
theorem difference_waits :
    (flow lowerDraw).Balances (web lowerLevel) ∧ (flow higherDraw).Balances (web higherLevel) ∧
      (web lowerLevel).Dependent ∧ (web higherLevel).Dependent ∧
      (flow lowerDraw).ExchangeFollows (web lowerLevel) (flow higherDraw) (web higherLevel)
        supportOnly () ∧
      (∀ t, t ≤ 2 → (web higherLevel).level t () = (web lowerLevel).level t () + 1) ∧
      ¬ (web lowerLevel).Supported 2 () ∧ (web higherLevel).Supported 2 () ∧
      (web higherLevel).level 3 () ≠ (web lowerLevel).level 3 () + 1 :=
  ⟨lower_balances, higher_balances, dependent lowerLevel, dependent higherLevel, follows,
   fun t le => (Flow.subthreshold_alike (fun t e _ => lower_balances.on [e] t)
      (fun t e _ => higher_balances.on [e] t) ⟨0, trivial⟩ (fun no => no) rfl
      (fun () _ other => absurd rfl other) follows t
      (fun s before => match s, before with
        | 0, _ => fun _ _ => Nat.le_succ 1
        | 1, _ => fun _ _ => Nat.le_refl 1
        | s + 2, before => absurd (Nat.lt_of_lt_of_le before le)
            (Nat.not_lt_of_le (Nat.le_add_left 2 s)))).1,
   fun supported => Nat.not_succ_le_zero 0 (supported () trivial),
   fun _ _ => Nat.le_refl 1,
   fun same => Nat.not_succ_le_zero 0 (Nat.le_of_eq same.symm)⟩

end SupportDrawn

/-! ### Both webs fail together: the difference stays

Two conditions, the stock (`true`) and a second requirement (`false`), which is gone after the
first step. -/

namespace JointFailure

def flow (draw : Nat → Nat) : Flow Unit Bool where
  present _ := [()]
  take t _ _ := draw t
  give _ _ _ := 0

/-- One unit at the first step only. -/
def draw : Nat → Nat
  | 0 => 1
  | _ + 1 => 0

/-- The stock starts at `s`; the second requirement stands at one at the first step and at
nothing after. -/
def web (s : Nat) : Web Unit Bool where
  level t c := match c, t with
    | true, 0 => s
    | true, _ + 1 => s - 1
    | false, 0 => 1
    | false, _ + 1 => 0
  active _ _ := True
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ _ _ := True

theorem balances_two : (flow draw).Balances (web 2)
  | 0, true => rfl
  | 0, false => rfl
  | _ + 1, true => rfl
  | _ + 1, false => rfl

theorem balances_three : (flow draw).Balances (web 3)
  | 0, true => rfl
  | 0, false => rfl
  | _ + 1, true => rfl
  | _ + 1, false => rfl

/-- **A joint failure keeps the difference.** Both webs fail the formation from the second step
on, the second requirement being gone, and the exchange follows its support only; the stock
stands one higher at every step: the lower web's failure is not a divergence. -/
theorem difference_kept :
    (flow draw).Balances (web 2) ∧ (flow draw).Balances (web 3) ∧
      (flow draw).ExchangeFollows (web 2) (flow draw) (web 3) supportOnly () ∧
      ¬ (web 2).Supported 1 () ∧ ¬ (web 3).Supported 1 () ∧
      ∀ t, (web 3).level t true = (web 2).level t true + 1 :=
  ⟨balances_two, balances_three, fun _ _ _ _ => ⟨rfl, rfl⟩,
   fun supported => Nat.not_succ_le_zero 0 (supported false trivial),
   fun supported => Nat.not_succ_le_zero 0 (supported false trivial),
   fun t => match t with
    | 0 => rfl
    | _ + 1 => rfl⟩

end JointFailure

/-! ### A stock that draws a taker ends the dependent sooner

A dependent needs one unit of the stock; a taker, which requires nothing, takes two units at the
first step where the stock stands at three. -/

namespace Attracting

inductive Formation where
  | dependent
  | taker

open Formation

/-- Lower: the dependent draws one unit at the first two steps. -/
def lowerFlow : Flow Formation Unit where
  present _ := [dependent, taker]
  take t f _ := match f, t with
    | dependent, 0 => 1
    | dependent, 1 => 1
    | dependent, _ + 2 => 0
    | taker, _ => 0
  give _ _ _ := 0

/-- Higher: the taker, drawn by a stock of three, takes two units at the first step, and the
dependent one. -/
def higherFlow : Flow Formation Unit where
  present _ := [dependent, taker]
  take t f _ := match f, t with
    | dependent, 0 => 1
    | dependent, _ + 1 => 0
    | taker, 0 => 2
    | taker, _ + 1 => 0
  give _ _ _ := 0

def lowerLevel : Nat → Nat
  | 0 => 2
  | 1 => 1
  | _ + 2 => 0

def higherLevel : Nat → Nat
  | 0 => 3
  | _ + 1 => 0

def web (level : Nat → Nat) : Web Formation Unit where
  level t _ := level t
  active t f := match f with
    | dependent => 1 ≤ level t
    | taker => True
  requires _ f _ := match f with
    | dependent => True
    | taker => False
  need _ _ _ := 1
  draws _ _ _ := True

theorem lower_balances : lowerFlow.Balances (web lowerLevel)
  | 0, () => rfl
  | 1, () => rfl
  | _ + 2, () => rfl

theorem higher_balances : higherFlow.Balances (web higherLevel)
  | 0, () => rfl
  | _ + 1, () => rfl

theorem dependent_web (level : Nat → Nat) : (web level).Dependent
  | _, Formation.dependent, active, _, _ => active
  | _, Formation.taker, _, _, no => nomatch no

/-- **Where others respond to the stock, the higher stock can end the dependent first.** The
higher web, one unit higher at the start, fails the dependent at the second step, where the lower
still supports it. The dependent registers alike at the first step and the totals taken differ
there: the exchange does not follow its registration. -/
theorem higher_breaks_first :
    lowerFlow.Balances (web lowerLevel) ∧ higherFlow.Balances (web higherLevel) ∧
      (web lowerLevel).Dependent ∧ (web higherLevel).Dependent ∧
      (web higherLevel).level 0 () = (web lowerLevel).level 0 () + 1 ∧
      (web lowerLevel).RegistersAlike supportOnly dependent (web lowerLevel).level
        (web higherLevel).level 0 ∧
      (web lowerLevel).Supported 1 dependent ∧ ¬ (web higherLevel).Supported 1 dependent ∧
      ¬ (web lowerLevel).RegistersAlike supportOnly dependent (web lowerLevel).level
        (web higherLevel).level 1 ∧
      ¬ lowerFlow.ExchangeFollows (web lowerLevel) higherFlow (web higherLevel) supportOnly
        dependent :=
  have alike0 : (web lowerLevel).RegistersAlike supportOnly dependent (web lowerLevel).level
      (web higherLevel).level 0 :=
    ⟨⟨fun _ _ _ => Nat.le_succ_of_le (Nat.le_succ 1), fun _ _ _ => Nat.le_succ 1⟩,
     fun _ no => False.elim no⟩
  ⟨lower_balances, higher_balances, dependent_web _, dependent_web _, rfl, alike0,
   fun _ _ => Nat.le_refl 1,
   fun supported => Nat.not_succ_le_zero 0 (supported () trivial),
   fun alike => Nat.not_succ_le_zero 0 ((alike.1.mp fun _ _ => Nat.le_refl 1) () trivial),
   fun follows => absurd (follows 0 (fun s le => match s, le with
       | 0, _ => alike0
       | _ + 1, le => absurd le (Nat.not_succ_le_zero _)) () (.inl ⟨0, trivial⟩)).1
     (by decide)⟩

end Attracting

/-! ### A predator takes from the prey's standing

The prey depends on food that nothing exchanges with, and not on its own standing. -/

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

/-- **A gauge of one's own standing registers being taken from.** The predator lies beyond the
prey's influence closure and within its registration closure under `ownStanding`. With the rest
of the exchange fixed, the prey registers the predator's part alike through its support at every
step, and not through a gauge of its own standing after the bite. -/
theorem registers_taking :
    ¬ flow.WithinInfluence web prey predator ∧
      flow.WithinRegistration web ownStanding prey predator ∧
      (∀ t, web.RegistersAlike supportOnly prey web.level spared t) ∧
      ¬ web.RegistersAlike ownStanding prey web.level spared 1 :=
  have beyond : ¬ flow.WithinInfluence web prey predator := fun within =>
    Relatum.noConfusion (within (fun x => x = prey) preyAlone_closed rfl)
  ⟨beyond,
   WithinClosure.of_rel ⟨prey, .inr rfl, ⟨0, .head _, .inl Nat.zero_lt_one⟩⟩,
   fun t => Flow.unregistered_beyond_registration withheld (fun t _ c _ _ => balances.on [c] t)
     (fun h member => match h, member with
       | predator, _ => fun within => beyond (Flow.withinRegistration_supportOnly.mp within)
       | food, no => nomatch no
       | prey, no => nomatch no)
     t prey (WithinClosure.refl _),
   fun alike => absurd (alike.2 prey rfl) (by decide)⟩

/-- **What `Prey` omits.** The registered difference makes no difference to the prey: it is
supported, active and admitted by the spared levels at every step. The prey does not bear on
itself, and the predator is active with no standing: the first part of `registers_taking` rests on
these omitted relations. -/
theorem omits :
    (∀ t, web.Supported t prey ∧ web.active t prey ∧ web.Admits (spared t) t prey) ∧
      ¬ web.SelfBearing prey ∧ ¬ web.Embodied predator :=
  ⟨fun _ => ⟨fun c requires => (match c, requires with
      | food, _ => Nat.le_refl 1
      | prey, no => nomatch no
      | predator, no => nomatch no),
    trivial,
    fun c requires => (match c, requires with
      | food, _ => Nat.le_refl 1
      | prey, no => nomatch no
      | predator, no => nomatch no)⟩,
   fun bearing => (nomatch (bearing 0 trivial).1),
   fun embodied => Nat.lt_irrefl 0 ((embodied 0).mp trivial)⟩

end Prey

/-! ### A prey that bears on itself

As `Prey`, except that the prey depends on its own standing at need one; the predator takes `b`
units at the first step. -/

namespace SelfPrey

open Prey.Relatum

def flow (b : Nat) : Flow Prey.Relatum Prey.Relatum where
  present _ := [predator]
  take t f c := match f, c with
    | predator, prey => (match t with
      | 0 => b
      | _ + 1 => 0)
    | predator, food => 0
    | predator, predator => 0
    | food, _ => 0
    | prey, _ => 0
  give _ _ _ := 0

/-- The prey's standing: two at the start, `2 - b` after the bite. -/
def standing (b : Nat) : Nat → Nat
  | 0 => 2
  | _ + 1 => 2 - b

def web (b : Nat) : Web Prey.Relatum Prey.Relatum where
  level t c := match c with
    | food => 1
    | prey => standing b t
    | predator => 0
  active _ _ := True
  requires _ f c := match f, c with
    | prey, food => True
    | prey, prey => True
    | prey, predator => False
    | food, _ => False
    | predator, _ => False
  need _ _ _ := 1
  draws _ _ _ := True

theorem balances_one : (flow 1).Balances (web 1)
  | 0, food => rfl
  | 0, prey => rfl
  | 0, predator => rfl
  | _ + 1, food => rfl
  | _ + 1, prey => rfl
  | _ + 1, predator => rfl

theorem balances_two : (flow 2).Balances (web 2)
  | 0, food => rfl
  | 0, prey => rfl
  | 0, predator => rfl
  | _ + 1, food => rfl
  | _ + 1, prey => rfl
  | _ + 1, predator => rfl

theorem selfBearing (b : Nat) : (web b).SelfBearing prey :=
  fun _ _ => ⟨trivial, Nat.zero_lt_one⟩

/-- Bearing on itself, the prey has the predator within its influence closure. -/
theorem within_influence (b : Nat) (pos : 0 < b) : (flow b).WithinInfluence (web b) prey predator :=
  WithinClosure.of_rel ⟨prey, ⟨0, trivial⟩, 0, .head _, .inl pos⟩

theorem admits_spared (b t : Nat) : (web b).Admits (Prey.spared t) t prey :=
  fun c requires => match c, requires with
  | food, _ => Nat.le_refl 1
  | prey, _ => Nat.le_succ 1
  | predator, no => nomatch no

/-- **The threshold on oneself.** A bite of one is above the prey's need on itself: through
support the prey registers it alike with the spared levels at every step, while a gauge of its
own standing registers it at the second step. A bite of two registers through support at the
second step. -/
theorem threshold_on_oneself :
    (∀ t, (web 1).RegistersAlike supportOnly prey (web 1).level Prey.spared t) ∧
      ¬ (web 1).RegistersAlike ownStanding prey (web 1).level Prey.spared 1 ∧
      ¬ (web 2).RegistersAlike supportOnly prey (web 2).level Prey.spared 1 :=
  ⟨fun t => ⟨⟨fun _ => admits_spared 1 t, fun _ c requires => match c, requires, t with
      | food, _, _ => Nat.le_refl 1
      | prey, _, 0 => Nat.le_succ 1
      | prey, _, _ + 1 => Nat.le_refl 1
      | predator, no, _ => nomatch no⟩, fun _ no => False.elim no⟩,
   fun alike => absurd (alike.2 prey rfl) (by decide),
   fun alike => Nat.not_succ_le_zero 0 ((alike.1.mpr (admits_spared 2 1)) prey trivial)⟩

end SelfPrey

/-! ### A wrong model

The model is that nothing takes or gives; the stock stands at two, then something the model omits
takes it. -/

namespace Stationary

/-- The model: nothing takes or gives. -/
def still : Flow Unit Unit := ⟨fun _ => [()], fun _ _ _ => 0, fun _ _ _ => 0⟩

/-- The actual history. -/
def actual : Nat → Unit → Nat
  | 0, _ => 2
  | _ + 1, _ => 0

def web : Web Unit Unit := ⟨actual, fun _ _ => True, fun _ _ _ => True, fun _ _ _ => 1,
  fun _ _ _ => True⟩

/-- Observing the stock. -/
def gauge : Unit → Unit → Prop := fun _ _ => True

/-- **A wrong model refutes what holds.** Relative to the model, a formation gauging the stock
refutes at the first step the claim that the stock comes to nothing, which holds of the actual
history. -/
theorem model_error :
    (∃ T, actual T () = 0) ∧ ¬ still.BalancedHistory actual ∧
      web.RefutesWithin still.BalancedHistory gauge (fun l' => ∃ T, l' T () = 0) () actual 0 :=
  ⟨⟨1, rfl⟩, fun history => Nat.noConfusion (history 0 ()),
   fun l' history' ⟨T, zero⟩ alike =>
     have same : ∀ s, l' s () = l' 0 () := fun s =>
       Nat.rec (motive := fun s => l' s () = l' 0 ()) rfl
         (fun s ih => (history' s ()).trans ih) s
     have two : l' 0 () = 2 := ((alike 0 (Nat.le_refl 0)).2 () trivial).symm
     Nat.noConfusion ((zero.symm.trans (same T)).trans two)⟩

/-- **Registration refutes the model.** At the second step no history the model admits is
registered alike by the gauging formation: within the model its belief is empty. -/
theorem model_refuted :
    web.RefutesWithin still.BalancedHistory gauge (fun _ => True) () actual 1 :=
  fun l' history' _ alike =>
    have zero : l' 1 () = 0 := ((alike 1 (Nat.le_refl 1)).2 () trivial).symm
    have two : l' 0 () = 2 := ((alike 0 (Nat.zero_le 1)).2 () trivial).symm
    Nat.noConfusion (zero.symm.trans ((history' 0 ()).trans two))

end Stationary

namespace Clearing

/-- The source and the clearer: the region of the clearer's registration. -/
def clearerSide : Formation → Prop
  | .source => True
  | .clearer => True
  | .dweller => False

/-- What a member of the clearer's side registers, registering support only, is the resource. -/
theorem registers_resource {g : Formation} {c : Place} (member : clearerSide g)
    (registers : web.Registers supportOnly g c) : c = .resource :=
  match registers with
  | .inr no => False.elim no
  | .inl ⟨_, depends⟩ => match g, c, member, depends with
    | .clearer, .resource, _, _ => rfl
    | .source, _, _, no => nomatch no
    | .clearer, .habitat, _, no => nomatch no
    | .clearer, .fuel _, _, no => nomatch no

/-- In a flow in which the dweller does not exchange with the resource, the clearer's side is
closed under being affected through what it registers. -/
theorem clearerSide_closed (L : Flow Formation Place)
    (dwellerQuiet : ∀ t, L.take t .dweller .resource = 0 ∧ L.give t .dweller .resource = 0) :
    ClosedUnder (L.RegisteredFrom web supportOnly) clearerSide :=
  fun _ h member ⟨c, registers, t, _, exchanges⟩ =>
    match c, registers_resource member registers, h, exchanges with
    | _, rfl, .source, _ => trivial
    | _, rfl, .clearer, _ => trivial
    | _, rfl, .dweller, .inl pos =>
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (dwellerQuiet t).1))
    | _, rfl, .dweller, .inr pos =>
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (dwellerQuiet t).2))

/-- The clearer registers alike at every step whether or not it clears the habitat: an instance
of `Flow.alike_within_closed`, the clearing being an act on a condition no member of its
side registers. -/
theorem alike_for_clearer :
    ∀ t, web.RegistersAlikeUpTo supportOnly .clearer web.level sparedWeb.level t :=
  fun _ s _ => Flow.alike_within_closed (region := clearerSide)
    (fun t _ c _ _ => balances.on [c] t) (fun t _ c _ _ => spared_balances.on [c] t)
    (clearerSide_closed flow fun _ => ⟨rfl, rfl⟩)
    (clearerSide_closed sparedFlow fun _ => ⟨rfl, rfl⟩)
    (fun _ => rfl)
    (fun _ member c registers => match c, registers_resource member registers with
      | _, rfl => rfl)
    (fun h _ _ _ _ c member registers => match c, registers_resource member registers with
      | _, rfl => match h with
        | .source => ⟨rfl, rfl⟩
        | .clearer => ⟨rfl, rfl⟩
        | .dweller => ⟨rfl, rfl⟩)
    s .clearer trivial

/-- The dweller is ended: from the third step on the levels do not admit it. -/
def DwellerEnded (l : Nat → Place → Nat) : Prop :=
  ∀ n, ¬ web.Admits (l (n + 2)) (n + 2) .dweller

/-- **Testing is relational.** In the world with the habitat spared, the claim that the dweller
is ended is refuted by the clearer at no step, and by the dweller at the third step. -/
theorem tested_by_dweller :
    DwellerEnded web.level ∧
      (∀ t, ¬ web.Refutes supportOnly DwellerEnded .clearer sparedWeb.level t) ∧
      web.Refutes supportOnly DwellerEnded .dweller sparedWeb.level 2 :=
  ⟨unsupported_with,
   fun t => Web.Refutes.not_of_alike (claim := DwellerEnded) (l' := web.level) unsupported_with
     (alike_for_clearer t).symm,
   fun _ ended alike => ended 0 ((alike 2 (Nat.le_refl 2)).1.mp
     ((Web.admits_iff_supported_of_agree (W := web) (W' := sparedWeb) (fun _ _ => Iff.rfl)
        (fun _ _ => rfl) 2).mpr (spared_dependent 2 .dweller trivial)))⟩

/-- The resource gone at the third step, all else as spared. -/
def resourceGone (t : Nat) : Place → Nat
  | .resource => match t with
    | 2 => 0
    | _ => 1
  | .habitat => 2
  | .fuel n => sparedWeb.level t (.fuel n)

/-- At the third step the dweller is not admitted, or the clearer is not. -/
def EitherEnded (l : Nat → Place → Nat) : Prop :=
  ¬ web.Admits (l 2) 2 .dweller ∨ ¬ web.Admits (l 2) 2 .clearer

/-- The clearer and the dweller. -/
def clearerAndDweller : Formation → Prop
  | .clearer => True
  | .dweller => True
  | .source => False

/-- **Pooled testing.** In the spared world, neither the clearer nor the dweller refutes, at the
third step, that one of them is not admitted there; the two together do. -/
theorem pooled :
    ¬ web.Refutes supportOnly EitherEnded .clearer sparedWeb.level 2 ∧
      ¬ web.Refutes supportOnly EitherEnded .dweller sparedWeb.level 2 ∧
      web.RefutesBy supportOnly EitherEnded clearerAndDweller sparedWeb.level 2 :=
  ⟨fun refutes => refutes web.level (.inl fun admits =>
      Nat.not_succ_le_zero 0 (admits .habitat trivial))
     (alike_for_clearer 2).symm,
   fun refutes => refutes resourceGone (.inr fun admits =>
      Nat.not_succ_le_zero 0 (admits .resource trivial))
     (fun _ _ => ⟨⟨fun admits c requires => (match c, requires with
          | .habitat, _ => admits .habitat trivial
          | .resource, no => nomatch no
          | .fuel _, no => nomatch no),
         fun admits c requires => (match c, requires with
          | .habitat, _ => admits .habitat trivial
          | .resource, no => nomatch no
          | .fuel _, no => nomatch no)⟩, fun _ no => False.elim no⟩),
   fun _ meets all => match meets with
    | .inl dweller => dweller (((all .dweller trivial) 2 (Nat.le_refl 2)).1.mp
        fun c requires => match c, requires with
          | .habitat, _ => Nat.le_succ 1
          | .resource, no => nomatch no
          | .fuel _, no => nomatch no)
    | .inr clearer => clearer (((all .clearer trivial) 2 (Nat.le_refl 2)).1.mp
        fun c requires => match c, requires with
          | .resource, _ => Nat.le_refl 1
          | .habitat, no => nomatch no
          | .fuel _, no => nomatch no)⟩

/-- A model fixing the start and the exchange of the clearing flow. -/
def FixedStartAndExchange (l' : Nat → Place → Nat) : Prop :=
  flow.BalancedHistory l' ∧ ∀ c, l' 0 c = web.level 0 c

/-- **A complete model idles registration.** With a model fixing the start and the exchange, the
clearer refutes at the first step, registering nothing about the habitat, that the dweller is
admitted at the third. -/
theorem model_idles_registration :
    web.RefutesWithin FixedStartAndExchange supportOnly (fun l' => web.Admits (l' 2) 2 .dweller)
      .clearer web.level 0 :=
  fun l' ⟨history', start⟩ admits _ =>
    have same : l' 2 .habitat = web.level 2 .habitat :=
      Flow.BalancedHistory.agree history' balances (start .habitat) 2
    Nat.not_succ_le_zero 0 (Nat.le_trans (admits .habitat trivial) (Nat.le_of_eq same))

end Clearing

namespace Renewable

/-- A reading decided by the first `h` steps of a run, crediting no run in which the focal
formation consumes, withholds credit from a run in which it renews. -/
theorem finite_reading_withholds_renewal (h : Nat) (reading : Run process → Prop)
    (decided : ∀ r r', r.AgreeUpTo h r' → reading r → reading r')
    (sound : ∀ r, reading r → ¬ (conditions.dependence.along r).ConsumingIn .focal) :
    ∃ r, (conditions.dependence.along r).RenewingIn .focal ∧ ¬ reading r :=
  match prefix_does_not_decide h with
  | ⟨renewing, consuming, agree, _, _, renews, consumes⟩ =>
    ⟨renewing, renews, fun reads => sound consuming (decided renewing consuming agree reads)
      consumes⟩

/-- **No finite reading is exact.** Where the continuation is open, no reading decided by the
first `h` steps of a run is the whole-run classification. -/
theorem no_exact_finite_reading (h : Nat) (reading : Run process → Prop)
    (decided : ∀ r r', r.AgreeUpTo h r' → reading r → reading r') :
    ¬ ∀ r, reading r ↔ (conditions.dependence.along r).RenewingIn .focal :=
  fun exact => match finite_reading_withholds_renewal h reading decided
      (fun r reads => Web.renewing_not_consuming ((exact r).mp reads)) with
    | ⟨r, renews, unread⟩ => unread ((exact r).mpr renews)

end Renewable

end Becoming
