import Becoming.Feedback

/-!
# Testing: what couples into a formation, and what it can test

On 11 October 2026 Ren asked whether becoming can provide "wisdoms to avoid run away feedbacks
and the identification of knowledge, learning, and scientific principles like falsifiability",
and wrote: "I think all the wisdoms about wisdoms, how to think, learn, update, are all explained
within what we have, if not not proved yet". To the AI's answer Ren replied: "agree with you,
great job, start now. for 4, you can explore which option is better, then make decision". This
module states, with no premise beyond balance on the conditions coupled into a formation and the
representation, what can couple into a formation, what a claim needs in order to be tested by it,
and where a difference does not pass. No significance, ranking or axiom occurs. The responsive
form of reach blindness, the exact threshold laws, exclusion relative to a model, pooled testing, the bridge to
`Becoming.Inquiry` and the self-bearing witness were proposed and checked by the stage's
independent review.

* **Coupling into a formation.** Into a formation couple its support, whether the levels admit
  it, and the levels of the conditions coupled into it by level (`obs`). Under two level
  histories they are alike through its couplings at a step when the levels admit it alike and the
  conditions coupled into it by level stand alike (`Web.AlikeThrough`), and alike up to a step
  when they are so at every step up to it (`Web.AlikeThroughUpTo`). A condition coupled into it
  by threshold only passes only whether it meets the need (`Web.alike_of_threshold`); one coupled
  by level passes its level (`Web.observed_level_couples`). More coupling by level distinguishes
  more (`Web.AlikeThroughUpTo.of_obs`). The base coupling is by threshold only
  (`thresholdOnly`). In the one-kind reading a formation's own standing then couples into it
  through support where it bears on itself (`Web.SelfBearing`); a gauge of its own standing
  (`ownStanding`) is a supplied coupling by level, as a gauge of a stock is.
* **Exclusion.** A claim about level histories is excluded at a formation at a step when no
  history meeting it is alike through the formation's couplings up to that step (`Web.Excludes`),
  and relative to a model, a class of admissible histories, when no admissible history meeting it
  is (`Web.ExcludesWithin`): the exclusion of the model and the claim together
  (`Web.excludesWithin_iff_conjunction`). A claim is excluded only through a difference that
  couples into the formation (`Web.Excludes.not_of_alike`); what holds is never excluded, and
  within a model only where the model admits what holds (`Web.Excludes.not_meets`,
  `Web.ExcludesWithin.not_meets`); an exclusion stands at every later step (`Web.Excludes.later`);
  more coupling by level excludes more (`Web.Excludes.widen`). Without a model, no finite prefix
  of levels excludes a claim about what follows it (`Web.tail_unexcluded`). With a model of the
  exchange, a formation into which a stock couples by level excludes at the first step every
  false claim that the stock comes to nothing (`Flow.excludes_tail_within`); a wrong model
  excludes what holds (`Stationary.model_error`), and what couples in excludes the model
  (`Stationary.model_excluded`). The class alike through a formation's couplings is the
  histories alike with the actual one through them (`Web.ClassThrough`,
  `Web.class_excludes_iff`); a judgment from it is a common response of `Becoming.Inquiry`,
  kept as later steps and more coupling by level narrow the class (`Web.class_judge_iff`,
  `Web.class_judge_later`, `Web.class_judge_widen`).
* **Reach blindness.** A condition couples into a formation when the formation depends on it or
  it is coupled into the formation by level (`Web.CoupledInto`). The coupling closure is the
  closure under exchanging with a condition coupled in (`Flow.WithinCoupling`). It holds the
  influence closure of `Becoming.Feedback`, is that closure where coupling is by threshold only,
  and grows with coupling by level and with exchange (`Flow.withinCoupling_of_withinInfluence`,
  `Flow.withinCoupling_thresholdOnly`, `Flow.withinCoupling_mono_obs`,
  `Flow.withinCoupling_mono_flow`). Let two flows with the same formations present balance on
  each condition coupled into a member of a region (`Flow.BalancesOn`), let the region be closed
  in both under being affected through what couples in, let the levels start alike on what couples
  into its members, and let each member's exchange on what couples into members follow what
  couples into it. Then every member is alike through its couplings at every step, whatever is
  done beyond the region or on what couples into no member (`Flow.alike_within_closed`,
  `Flow.alike_within_coupling`). With the rest of the exchange fixed this is P42's form for
  every coupling by level (`Flow.uncoupled_beyond_coupling`): no claim met by the levels without
  a part beyond the closure is excluded within it, an exclusion there rests on a model of the
  part's exchange, and a judgment there holds with and without the part
  (`Flow.unexcluded_beyond_coupling`, `Flow.beyond_needs_model`, `Flow.class_judge_beyond`).
* **Testing is relational.** In `Clearing` the clearer is alike through its couplings at every
  step whether or not its clearing ends the dweller (`Clearing.alike_for_clearer`, an instance of
  `alike_within_closed`). In the spared world the claim that the dweller is ended is excluded at
  the dweller at the third step and at the clearer at no step (`Clearing.tested_by_dweller`); a
  claim excluded at neither is excluded at the two together (`Clearing.pooled`); with a model
  fixing the start and the exchange, the clearer excludes what does not couple into it, and its
  couplings do no work (`Clearing.model_idles_coupling`).
* **Threshold blindness.** Let two flows balance on each condition coupled into `g`, the exchange
  there following what couples into `g` (`Flow.ExchangeFollows`). While the flows are alike
  through `g`'s couplings, every difference on a condition coupled into `g` stays as it was at the
  start (`Flow.difference_kept`). Where the second web starts at least as high on what couples
  into `g` and alike on what is coupled into it by level, the flows are alike through `g`'s
  couplings at every step before which the first web supported it (`Flow.alike_while_supported`),
  and a difference changes only after a step at which the second web admitted `g` and the first
  did not support it (`Flow.difference_changes_after_divergence`). For one stock `d` higher that
  couples into `g` by threshold only: it stands `d` higher, and the flows are alike through `g`'s
  couplings, at every step before which the first web supported `g` at every step
  (`Flow.subthreshold_alike`, `Flow.subthreshold_alike_always`). Both webs failing together, the
  difference can stay for ever (`JointFailure.difference_kept`). `SupportDrawn` is a witness in
  which the difference changes (`SupportDrawn.difference_waits`). Coupling the stock by level
  lifts this: the two webs are apart through the couplings of `Gauged`'s formation at the first
  step, and it draws on the higher stock while supported in both
  (`Gauged.gauge_changes_difference`). Where others respond to the stock itself the hypothesis
  fails, and the higher stock can end `g` first (`Attracting.higher_breaks_first`). On a prey that
  bears on itself, a bite passes through support only where it brings the prey below its need, and
  a gauge of itself passes every bite (`SelfPrey.threshold_on_oneself`).
* **Horizon.** Where the continuation is open, as in `Renewable`, no reading decided by the first
  `h` steps of a run is the whole-run classification (`Renewable.no_exact_finite_reading`); one
  that includes no consuming run excludes a renewing one
  (`Renewable.finite_reading_withholds_renewal`). Both are corollaries of
  `Renewable.prefix_does_not_decide`, beside `Renewable.finite_reading_includes_consumption`.

**Readings (the AI's; Ren accepted their earlier wording on 11 October 2026, and the review
narrowed them).**
- Feedback through support has three blindnesses, each in its scope: below a threshold, where the
  exchange follows what couples in (`subthreshold_alike`); beyond the horizon, where the
  continuation is open (`Becoming.Horizon`); and beyond the coupling closure
  (`alike_within_closed`). They are not the only ones: support passes only net exchange
  (`Flow.Balances.agrees_iff_even`), and one joint bit across the conditions required.
- A runaway is a loop that runs inside one of them. This is a heuristic, not a statement: no loop
  or gain is defined, and where others respond to a stock its loss can couple in sooner
  (`Attracting`).
- Measurement couples a level into a formation below the threshold
  (`Web.observed_level_couples`); a model of the exchange crosses the horizon relative to itself
  and answers to what couples in (`Flow.excludes_tail_within`, `Stationary`); new coupling by
  level and new exchange widen the closure (`Flow.withinCoupling_mono_obs`,
  `Flow.withinCoupling_mono_flow`); what couples into others tests what does not couple into one
  (`Clearing.tested_by_dweller`, `Clearing.pooled`), and reaches one only through a relation that
  is itself an exchange or a coupling by level.
- Falsifiability is the condition of being corrected by the unfolding: a claim and its rivals
  must differ in what can couple in (`Web.Excludes.not_of_alike`). It is relational and moves with
  what couples in. Without a model no finite prefix tests a claim about what follows it; with
  one, the test is of the model and the claim together.
- Read with Ren's 心 and 理, 理 is a model answerable to what couples in: it narrows the histories
  admitted, so that the same couplings decide more; it can mislead, and what couples in corrects
  it.

What is not derived:
- that anything couples into a formation by level beyond its support, that it gauges its own
  standing, forms a model, or wants to avoid a runaway;
- what a coupling is about: being alike through the couplings bounds what can be told apart, and
  says nothing of what a difference signifies;
- what an act does: a claim about it compares two histories, and is tested only relative to a
  model of the history without the act (`Flow.beyond_needs_model`,
  `Clearing.model_idles_coupling`); varying one's own act and the difference coupling back is
  open;
- which laws hold of the actual unfolding;
- how others respond: `Flow.ExchangeFollows`, and the response hypothesis of
  `alike_within_closed`, are supplied, and the comparison with a part withheld holds the rest of
  the exchange fixed.

Activity is supplied by the representation, not produced by the exchange, so it is not counted
among what couples in; under `Web.Dependent` it cannot outrun support. Balance is assumed only on
the conditions coupled in, at each step (`Flow.BalancesOn`); global balance gives it
(`Flow.Balances.on`). The representation commits to discrete steps and natural quantities.

Judging a class along runs (`Web.class_judge_iff`, `Web.class_judge_later`, `Web.class_judge_widen`,
`Flow.class_judge_beyond`) and the finite readings of renewal
(`Renewable.finite_reading_withholds_renewal`, `Renewable.no_exact_finite_reading`), with
`sees_narrow`, which only they use, are in `Becoming.LabelledRoles`, so this module does not import
the frame (board item W).
-/

namespace Becoming

variable {F C : Type}

/-! ## Coupling and exclusion -/

/-- No level is coupled by level: only support couples into a formation, by threshold. In the
one-kind reading its own standing then couples in through support where it bears on itself
(`Web.SelfBearing`). -/
def thresholdOnly : F → C → Prop := fun _ _ => False

/-- In the one-kind reading, a gauge of one's own standing: a supplied coupling by level, as a
gauge of a stock is, not given by the identification of the two roles. -/
def ownStanding {X : Type} : X → X → Prop := fun g c => c = g

/-- A stock other than oneself is not one's own standing. -/
theorem ownStanding_other {X : Type} {g c : X} (other : c ≠ g) : ¬ ownStanding g c :=
  other

/-- `a + x = b + y` and `x ≤ y` give `b ≤ a`. -/
theorem le_of_add_eq_of_le {a b x y : Nat} (same : a + x = b + y) (le : x ≤ y) : b ≤ a :=
  le_of_add_le_add_right x (Nat.le_trans (Nat.add_le_add_left le b) (Nat.le_of_eq same.symm))

/-- `a + x = b + y` and `x = y` give `b = a`. -/
theorem eq_of_add_eq_of_eq {a b x y : Nat} (same : a + x = b + y) (eq : x = y) : b = a :=
  (add_right_cancel x (same.trans (congrArg (b + ·) eq.symm))).symm

/-- The level history `l` up to `t`, then the level `k` on `c`. -/
def prefixThen [DecidableEq C] (l : Nat → C → Nat) (t : Nat) (c : C) (k : Nat) :
    Nat → C → Nat :=
  fun s e => if s ≤ t then l s e else if e = c then k else l s e

namespace Web

variable (W : Web F C)

/-- Under two level histories, alike through `g`'s couplings at `t`: the levels admit `g` alike,
and the conditions coupled into `g` by level stand alike. -/
def AlikeThrough (obs : F → C → Prop) (g : F) (l l' : Nat → C → Nat) (t : Nat) : Prop :=
  (W.Admits (l t) t g ↔ W.Admits (l' t) t g) ∧ ∀ c, obs g c → l t c = l' t c

/-- Alike through `g`'s couplings at every step up to `t`. -/
def AlikeThroughUpTo (obs : F → C → Prop) (g : F) (l l' : Nat → C → Nat) (t : Nat) : Prop :=
  ∀ s, s ≤ t → W.AlikeThrough obs g l l' s

/-- A claim about level histories is excluded at `g` at `t` under `l` when no history meeting
the claim is alike with `l` through `g`'s couplings up to `t`. No inquiry is presupposed: what
couples into `g` leaves no history meeting the claim. -/
def Excludes (obs : F → C → Prop) (claim : (Nat → C → Nat) → Prop) (g : F)
    (l : Nat → C → Nat) (t : Nat) : Prop :=
  ∀ l', claim l' → ¬ W.AlikeThroughUpTo obs g l l' t

/-- Excluded relative to a model, the histories it admits: no admitted history meeting the claim
is alike through `g`'s couplings up to `t`. -/
def ExcludesWithin (admitted : (Nat → C → Nat) → Prop) (obs : F → C → Prop)
    (claim : (Nat → C → Nat) → Prop) (g : F) (l : Nat → C → Nat) (t : Nat) : Prop :=
  ∀ l', admitted l' → claim l' → ¬ W.AlikeThroughUpTo obs g l l' t

/-- A condition couples into `g` when `g` depends on it, by the threshold of its support, or it
is coupled into `g` by level (`obs`). The coupling is directed: `c` into `g`.
(`Becoming.RespectsClaims` of `Becoming.Likeness` is a different relation, on descriptions under
which related descriptions realize the same claims.) -/
def CoupledInto (obs : F → C → Prop) (g : F) (c : C) : Prop :=
  W.DependsOn g c ∨ obs g c

/-- The class alike through `g` at `t` under `l`: the histories alike with `l` through `g`'s
couplings up to `t`. -/
def ClassThrough (obs : F → C → Prop) (g : F) (l : Nat → C → Nat) (t : Nat) :
    (Nat → C → Nat) → Prop :=
  fun l' => W.AlikeThroughUpTo obs g l l' t

/-- Alike through the couplings of every member of a group up to `t`. -/
def AlikeThroughAll (obs : F → C → Prop) (group : F → Prop) (l l' : Nat → C → Nat)
    (t : Nat) : Prop :=
  ∀ g, group g → W.AlikeThroughUpTo obs g l l' t

/-- A claim is excluded at a group when no history meeting it is alike through the couplings of
all its members. -/
def ExcludesBy (obs : F → C → Prop) (claim : (Nat → C → Nat) → Prop) (group : F → Prop)
    (l : Nat → C → Nat) (t : Nat) : Prop :=
  ∀ l', claim l' → ¬ W.AlikeThroughAll obs group l l' t

/-- At `t`, `W'` stands at least as high as `W` on every condition coupled into `g`, and alike on
every condition coupled into `g` by level. -/
def LevelsAtLeast (W' : Web F C) (obs : F → C → Prop) (g : F) (t : Nat) : Prop :=
  (∀ e, W.CoupledInto obs g e → W.level t e ≤ W'.level t e) ∧
    ∀ e, obs g e → W.level t e = W'.level t e

variable {W} {obs obs' : F → C → Prop} {g : F} {l l' : Nat → C → Nat}

/-- Every history is alike with itself through `g`'s couplings. -/
theorem AlikeThrough.refl (t : Nat) : W.AlikeThrough obs g l l t :=
  ⟨Iff.rfl, fun _ _ => rfl⟩

/-- Alike through the couplings is symmetric. -/
theorem AlikeThrough.symm {t : Nat} (alike : W.AlikeThrough obs g l l' t) :
    W.AlikeThrough obs g l' l t :=
  ⟨alike.1.symm, fun c observed => (alike.2 c observed).symm⟩

/-- Alike through the couplings up to a step is symmetric. -/
theorem AlikeThroughUpTo.symm {t : Nat} (alike : W.AlikeThroughUpTo obs g l l' t) :
    W.AlikeThroughUpTo obs g l' l t :=
  fun s le => (alike s le).symm

/-- Alike up to a step, alike up to every earlier step. -/
theorem AlikeThroughUpTo.earlier {s t : Nat} (alike : W.AlikeThroughUpTo obs g l l' t)
    (le : s ≤ t) : W.AlikeThroughUpTo obs g l l' s :=
  fun r le' => alike r (Nat.le_trans le' le)

/-- More coupling by level distinguishes more: histories alike through a larger coupling by
level are alike through a smaller one. -/
theorem AlikeThroughUpTo.of_obs (larger : ∀ g c, obs g c → obs' g c) {t : Nat}
    (alike : W.AlikeThroughUpTo obs' g l l' t) : W.AlikeThroughUpTo obs g l l' t :=
  fun s le => ⟨(alike s le).1, fun c observed => (alike s le).2 c (larger g c observed)⟩

/-- Histories agreeing up to `t` are alike through the couplings up to `t`. -/
theorem alikeThroughUpTo_of_agree {t : Nat} (agree : ∀ s, s ≤ t → ∀ e, l' s e = l s e) :
    W.AlikeThroughUpTo obs g l l' t :=
  fun s le => ⟨⟨fun admits c requires => Nat.le_trans (admits c requires)
      (Nat.le_of_eq (agree s le c).symm),
    fun admits c requires => Nat.le_trans (admits c requires) (Nat.le_of_eq (agree s le c))⟩,
   fun c _ => (agree s le c).symm⟩

/-- **What passes of one condition: its threshold.** With every other condition coupled into `g`
alike at `s`, a condition coupled into `g` by threshold only passes only whether it meets the
need: meeting it under both histories or under neither, they are alike through `g`'s couplings,
whatever the two levels are. -/
theorem alike_of_threshold [DecidableEq C] {c : C} {s : Nat} (unobserved : ¬ obs g c)
    (others : ∀ e, W.CoupledInto obs g e → e ≠ c → l s e = l' s e)
    (threshold : W.requires s g c → (W.need s g c ≤ l s c ↔ W.need s g c ≤ l' s c)) :
    W.AlikeThrough obs g l l' s :=
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

/-- **What passes of one condition: its level, where coupled by level.** Any difference at `s` in
a condition coupled into `g` by level makes the histories not alike through `g`'s couplings. -/
theorem observed_level_couples {c : C} {s : Nat} (observed : obs g c)
    (differ : l s c ≠ l' s c) : ¬ W.AlikeThrough obs g l l' s :=
  fun alike => differ (alike.2 c observed)

/-- A claim is excluded only through a difference that couples in: where a history meeting it
is alike through `g`'s couplings up to a step, it is not excluded there. -/
theorem Excludes.not_of_alike {claim : (Nat → C → Nat) → Prop} {t : Nat} (meets : claim l')
    (alike : W.AlikeThroughUpTo obs g l l' t) : ¬ W.Excludes obs claim g l t :=
  fun refutes => refutes l' meets alike

/-- What holds is never excluded. -/
theorem Excludes.not_meets {claim : (Nat → C → Nat) → Prop} {t : Nat}
    (refutes : W.Excludes obs claim g l t) : ¬ claim l :=
  fun meets => refutes l meets fun s _ => AlikeThrough.refl s

/-- An exclusion stands: excluded at a step, excluded at every later step. -/
theorem Excludes.later {claim : (Nat → C → Nat) → Prop} {s t : Nat}
    (refutes : W.Excludes obs claim g l s) (le : s ≤ t) : W.Excludes obs claim g l t :=
  fun l' meets alike => refutes l' meets (alike.earlier le)

/-- More coupling by level excludes more. -/
theorem Excludes.widen (larger : ∀ g c, obs g c → obs' g c) {claim : (Nat → C → Nat) → Prop}
    {t : Nat} (refutes : W.Excludes obs claim g l t) : W.Excludes obs' claim g l t :=
  fun l' meets alike => refutes l' meets (alike.of_obs larger)

/-- A claim met by a history that agrees with `l` up to `t` is not excluded at `t`. -/
theorem Excludes.not_of_extension {claim : (Nat → C → Nat) → Prop} {t : Nat}
    (extension : ∃ m, claim m ∧ ∀ s, s ≤ t → ∀ e, m s e = l s e) :
    ¬ W.Excludes obs claim g l t :=
  match extension with
  | ⟨_, meets, agree⟩ => Excludes.not_of_alike meets (alikeThroughUpTo_of_agree agree)

/-- **Without a model, a finite prefix leaves what follows open.** For every level history up to
`t`, neither the claim that a condition comes to nothing nor the claim that it stays above
nothing after `t` is excluded at `t`, at any formation under any coupling by level. -/
theorem tail_unexcluded [DecidableEq C] {t : Nat} (c : C) :
    ¬ W.Excludes obs (fun m => ∃ T, m T c = 0) g l t ∧
      ¬ W.Excludes obs (fun m => ∀ T, t < T → 0 < m T c) g l t :=
  have agree : ∀ k, ∀ s, s ≤ t → ∀ e, prefixThen l t c k s e = l s e := fun _ _ le _ =>
    if_pos le
  have after : ∀ k T, t < T → prefixThen l t c k T c = k := fun _ _ later =>
    (if_neg (Nat.not_le_of_lt later)).trans (if_pos rfl)
  ⟨Excludes.not_of_extension ⟨prefixThen l t c 0,
      ⟨t + 1, after 0 (t + 1) (Nat.lt_succ_self t)⟩, agree 0⟩,
   Excludes.not_of_extension ⟨prefixThen l t c 1, fun T later =>
      Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq (after 1 T later).symm), agree 1⟩⟩

/-- Exclusion is exclusion relative to the model admitting every history. -/
theorem excludes_iff_excludesWithin_all {claim : (Nat → C → Nat) → Prop} {t : Nat} :
    W.Excludes obs claim g l t ↔ W.ExcludesWithin (fun _ => True) obs claim g l t :=
  ⟨fun refutes l' _ meets => refutes l' meets, fun refutes l' meets => refutes l' trivial meets⟩

/-- Exclusion within a model is exclusion of the model and the claim together. -/
theorem excludesWithin_iff_conjunction {admitted : (Nat → C → Nat) → Prop}
    {claim : (Nat → C → Nat) → Prop} {t : Nat} :
    W.ExcludesWithin admitted obs claim g l t ↔
      W.Excludes obs (fun l' => admitted l' ∧ claim l') g l t :=
  ⟨fun refutes l' ⟨inside, meets⟩ => refutes l' inside meets,
   fun refutes l' inside meets => refutes l' ⟨inside, meets⟩⟩

/-- A narrower model excludes more. -/
theorem ExcludesWithin.narrow {admitted admitted' : (Nat → C → Nat) → Prop}
    (narrower : ∀ l, admitted' l → admitted l) {claim : (Nat → C → Nat) → Prop} {t : Nat}
    (refutes : W.ExcludesWithin admitted obs claim g l t) :
    W.ExcludesWithin admitted' obs claim g l t :=
  fun l' inside meets => refutes l' (narrower l' inside) meets

/-- Within a model admitting what holds, what holds is never excluded. -/
theorem ExcludesWithin.not_meets {admitted : (Nat → C → Nat) → Prop}
    {claim : (Nat → C → Nat) → Prop} {t : Nat} (actual : admitted l)
    (refutes : W.ExcludesWithin admitted obs claim g l t) : ¬ claim l :=
  fun meets => refutes l actual meets fun _ _ => AlikeThrough.refl _

/-- What is excluded at any member is excluded at the group. -/
theorem ExcludesBy.of_member {claim : (Nat → C → Nat) → Prop} {group : F → Prop} {t : Nat}
    (member : group g) (refutes : W.Excludes obs claim g l t) : W.ExcludesBy obs claim group l t :=
  fun l' meets all => refutes l' meets (all g member)

/-- A claim is excluded exactly where it is disjoint from the class alike through `g`. -/
theorem class_excludes_iff {claim : (Nat → C → Nat) → Prop} {t : Nat} :
    W.Excludes obs claim g l t ↔ ∀ l', W.ClassThrough obs g l t l' → ¬ claim l' :=
  ⟨fun refutes l' believed meets => refutes l' meets believed,
   fun disjoint l' meets believed => disjoint l' believed meets⟩

variable {H : Type} {admissible : (Nat → C → Nat) → H → Prop} {a : H}

/-- Webs agreeing on what `g` requires and needs pass its support through admission by their
levels. -/
theorem admits_iff_supported_of_agree {W' : Web F C}
    (requires : ∀ t c, W.requires t g c ↔ W'.requires t g c)
    (need : ∀ t c, W.need t g c = W'.need t g c) (t : Nat) :
    W.Admits (W'.level t) t g ↔ W'.Supported t g :=
  ⟨fun admits c requires' =>
     Nat.le_trans (Nat.le_of_eq (need t c).symm) (admits c ((requires t c).mpr requires')),
   fun supported c requires'' =>
     Nat.le_trans (Nat.le_of_eq (need t c)) (supported c ((requires t c).mp requires''))⟩

/-- Where `W'` stands at least as high on what couples into `g` and alike on what couples into it
by level, being alike through `g`'s couplings at a step is exactly: wherever the levels of `W'`
admit `g`, `W` supports it. -/
theorem alikeThrough_iff_of_levelsAtLeast {W' : Web F C} {t : Nat}
    (above : W.LevelsAtLeast W' obs g t) :
    W.AlikeThrough obs g W.level W'.level t ↔ (W.Admits (W'.level t) t g → W.Supported t g) :=
  ⟨fun alike => alike.1.mpr,
   fun back => ⟨⟨fun supported e requires =>
       Nat.le_trans (supported e requires) (above.1 e (.inl ⟨t, requires⟩)), back⟩,
     above.2⟩⟩

end Web

/-! ## Reach blindness: nothing beyond the coupling closure couples in -/

namespace Flow

variable (L : Flow F C) (W : Web F C)

/-- `g` is affected by `h` through what couples into `g`: `h` exchanges with a condition coupled
into `g`. -/
def CoupledFrom (obs : F → C → Prop) (g h : F) : Prop :=
  ∃ c, W.CoupledInto obs g c ∧ L.Exchanges h c

/-- `g` lies within `f`'s coupling closure: the closure under being affected through what couples
in. -/
def WithinCoupling (obs : F → C → Prop) (f g : F) : Prop :=
  WithinClosure (L.CoupledFrom W obs) f g

/-- Affected through what couples in, in either of two flows. -/
def CoupledFromEither (L' : Flow F C) (obs : F → C → Prop) (g h : F) : Prop :=
  L.CoupledFrom W obs g h ∨ L'.CoupledFrom W obs g h

/-- The exchange on what couples into `g` follows what couples into `g`: wherever the flows are
alike through `g`'s couplings up to `t`, they take from and give to every condition coupled into
`g` alike across the step from `t`, in total over every formation present. A hypothesis on the
whole exchange around `g`: it excludes others responding to what does not couple into `g`. -/
def ExchangeFollows (L' : Flow F C) (W' : Web F C) (obs : F → C → Prop) (g : F) : Prop :=
  ∀ t, W.AlikeThroughUpTo obs g W.level W'.level t → ∀ c, W.CoupledInto obs g c →
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

/-- **A model of the exchange crosses the horizon.** Relative to the level histories of a flow,
every false claim that a stock comes to nothing is excluded at the first step at a formation into
which the stock couples by level. -/
theorem excludes_tail_within {l : Nat → C → Nat} {c : C} (observed : obs g c)
    (history : L.BalancedHistory l) (never : ∀ T, ¬ l T c = 0) :
    W.ExcludesWithin L.BalancedHistory obs (fun l' => ∃ T, l' T c = 0) g l 0 :=
  fun _ history' ⟨T, zero⟩ alike =>
    never T ((BalancedHistory.agree history history' ((alike 0 (Nat.le_refl 0)).2 c observed)
      T).trans zero)

/-- The coupling closure holds the influence closure. -/
theorem withinCoupling_of_withinInfluence {f g : F} (within : L.WithinInfluence W f g) :
    L.WithinCoupling W obs f g :=
  WithinClosure.mono (fun _ _ ⟨c, depends, exchanges⟩ => ⟨c, .inl depends, exchanges⟩) within

/-- Where coupling is by threshold only, the coupling closure is the influence closure. -/
theorem withinCoupling_thresholdOnly {f g : F} :
    L.WithinCoupling W thresholdOnly f g ↔ L.WithinInfluence W f g :=
  ⟨WithinClosure.mono fun _ _ ⟨c, registers, exchanges⟩ => match registers with
     | .inl depends => ⟨c, depends, exchanges⟩
     | .inr no => False.elim no,
   withinCoupling_of_withinInfluence⟩

/-- The coupling closure grows with coupling by level. -/
theorem withinCoupling_mono_obs (larger : ∀ g c, obs g c → obs' g c) {f g : F}
    (within : L.WithinCoupling W obs f g) : L.WithinCoupling W obs' f g :=
  WithinClosure.mono (fun _ _ ⟨c, registers, exchanges⟩ =>
    ⟨c, registers.imp id (larger _ c), exchanges⟩) within

/-- The coupling closure grows with exchange. -/
theorem withinCoupling_mono_flow (more : ∀ h c, L.Exchanges h c → L'.Exchanges h c)
    {f g : F} (within : L.WithinCoupling W obs f g) : L'.WithinCoupling W obs f g :=
  WithinClosure.mono (fun _ _ ⟨c, registers, exchanges⟩ =>
    ⟨c, registers, more _ c exchanges⟩) within

/-- Nothing beyond a formation's coupling closure exchanges with a condition coupled into a
formation within it. -/
theorem beyond_coupling {f g h : F} (within : L.WithinCoupling W obs f g)
    (beyond : ¬ L.WithinCoupling W obs f h) {c : C} (registers : W.CoupledInto obs g c) :
    ¬ L.Exchanges h c :=
  fun exchanges => WithinClosure.not_rel within beyond ⟨c, registers, exchanges⟩

/-- Within a region closed in both flows under being affected through what couples in, each
formation's exchange on a condition coupled into a member agrees in the two flows wherever the
members' does: a formation exchanging there is a member. -/
theorem exchange_agrees_within {region : F → Prop} {h : F} {c : C} {t : Nat}
    (closed : ClosedUnder (L.CoupledFrom W obs) region)
    (closed' : ClosedUnder (L'.CoupledFrom W obs) region)
    (present : L.present t = L'.present t) (member : region g) (registers : W.CoupledInto obs g c)
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
present, balancing on each condition coupled into a member, and a region closed in both under
being affected through what couples in.
Let the levels start alike on everything that couples into a member, and let each member take
from and give to what couples into the members alike in the two flows wherever the flows have
been alike through its couplings. Then the flows are alike through every member's couplings at
every step, whatever differs beyond the region, in what members do with conditions coupled into
no member, or in levels coupled into no member. -/
theorem alike_within_closed {region : F → Prop}
    (balanced : ∀ t g c, region g → W.CoupledInto obs g c → L.BalancesOn W [c] t)
    (balanced' : ∀ t g c, region g → W.CoupledInto obs g c → L'.BalancesOn W' [c] t)
    (closed : ClosedUnder (L.CoupledFrom W obs) region)
    (closed' : ClosedUnder (L'.CoupledFrom W obs) region)
    (present : ∀ t, L.present t = L'.present t)
    (start : ∀ g, region g → ∀ c, W.CoupledInto obs g c → W.level 0 c = W'.level 0 c)
    (responds : ∀ h, region h → ∀ t, W.AlikeThroughUpTo obs h W.level W'.level t →
      ∀ g c, region g → W.CoupledInto obs g c →
        L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c) :
    ∀ t g, region g → W.AlikeThrough obs g W.level W'.level t :=
  have alikeOf : ∀ t, (∀ g, region g → ∀ c, W.CoupledInto obs g c → W.level t c = W'.level t c) →
      ∀ g, region g → W.AlikeThrough obs g W.level W'.level t := fun t same g member =>
    ⟨⟨fun admits c requires => Nat.le_trans (admits c requires)
        (Nat.le_of_eq (same g member c (.inl ⟨t, requires⟩))),
      fun admits c requires => Nat.le_trans (admits c requires)
        (Nat.le_of_eq (same g member c (.inl ⟨t, requires⟩)).symm)⟩,
     fun c observed => same g member c (.inr observed)⟩
  have levels : ∀ t, ∀ s, s ≤ t →
      ∀ g, region g → ∀ c, W.CoupledInto obs g c → W.level s c = W'.level s c := fun t =>
    Nat.rec (motive := fun t => ∀ s, s ≤ t →
        ∀ g, region g → ∀ c, W.CoupledInto obs g c → W.level s c = W'.level s c)
      (fun s le => match s, le with
        | 0, _ => start
        | _ + 1, le => absurd le (Nat.not_succ_le_zero _))
      (fun t ih s le g member c registers =>
        match Nat.lt_or_eq_of_le le with
        | .inl before => ih s (Nat.le_of_lt_succ before) g member c registers
        | .inr same => same ▸
          have upTo : ∀ h, region h → W.AlikeThroughUpTo obs h W.level W'.level t :=
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

/-- Reach blindness where the members respond, for `f`'s coupling closure drawn through both
flows. -/
theorem alike_within_coupling {f : F}
    (balanced : ∀ t g c, WithinClosure (L.CoupledFromEither W L' obs) f g →
      W.CoupledInto obs g c → L.BalancesOn W [c] t)
    (balanced' : ∀ t g c, WithinClosure (L.CoupledFromEither W L' obs) f g →
      W.CoupledInto obs g c → L'.BalancesOn W' [c] t)
    (present : ∀ t, L.present t = L'.present t)
    (start : ∀ g, WithinClosure (L.CoupledFromEither W L' obs) f g →
      ∀ c, W.CoupledInto obs g c → W.level 0 c = W'.level 0 c)
    (responds : ∀ h, WithinClosure (L.CoupledFromEither W L' obs) f h →
      ∀ t, W.AlikeThroughUpTo obs h W.level W'.level t →
      ∀ g c, WithinClosure (L.CoupledFromEither W L' obs) f g → W.CoupledInto obs g c →
        L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c) :
    ∀ t g, WithinClosure (L.CoupledFromEither W L' obs) f g →
      W.AlikeThrough obs g W.level W'.level t :=
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
beyond `f`'s coupling closure, the flows with and without the part are alike through the
couplings of each formation within the closure at every step: an instance of
`alike_within_closed`, whose second flow is the flow with the part withheld. Where coupling is by
threshold only, this is P42's `uncoupled_beyond_influence`. -/
theorem uncoupled_beyond_coupling {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {f : F}
    (balanced : ∀ t g c, L.WithinCoupling W obs f g → W.CoupledInto obs g c →
      L.BalancesOn W [c] t)
    (beyond : ∀ h, part h = true → ¬ L.WithinCoupling W obs f h) :
    ∀ t g, L.WithinCoupling W obs f g → W.AlikeThrough obs g W.level l t :=
  have closed : ClosedUnder (L.CoupledFrom W obs) (L.WithinCoupling W obs f) :=
    closedUnder_withinClosure f
  have closed' : ClosedUnder ((L.withhold part).CoupledFrom W obs)
      (L.WithinCoupling W obs f) :=
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

/-- What a part beyond the coupling closure does cannot be tested within it: no claim met by
the levels without the part is excluded, at any step, at a formation within the closure. -/
theorem unexcluded_beyond_coupling {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {f : F}
    (balanced : ∀ t g c, L.WithinCoupling W obs f g → W.CoupledInto obs g c →
      L.BalancesOn W [c] t)
    (beyond : ∀ h, part h = true → ¬ L.WithinCoupling W obs f h)
    {claim : (Nat → C → Nat) → Prop} (meets : claim l) :
    ∀ t g, L.WithinCoupling W obs f g → ¬ W.Excludes obs claim g W.level t :=
  fun _ g within => Web.Excludes.not_of_alike meets fun s _ =>
    uncoupled_beyond_coupling without balanced beyond s g within

/-- **Beyond the coupling closure, only a model can judge.** Where a claim is excluded relative to
a model at a formation within the closure, the model and the claim together exclude the levels
without a part beyond it: the exclusion rests on a model of the part's exchange. -/
theorem beyond_needs_model {l₀ : Nat → C → Nat}
    (without : L.WithheldLevels part W l₀) {f : F}
    (balanced : ∀ t g c, L.WithinCoupling W obs f g → W.CoupledInto obs g c →
      L.BalancesOn W [c] t)
    (beyond : ∀ h, part h = true → ¬ L.WithinCoupling W obs f h)
    (within : L.WithinCoupling W obs f g) {admitted : (Nat → C → Nat) → Prop}
    {claim : (Nat → C → Nat) → Prop} {t : Nat}
    (refutes : W.ExcludesWithin admitted obs claim g W.level t) : ¬ (admitted l₀ ∧ claim l₀) :=
  fun ⟨inside, meets⟩ => refutes l₀ inside meets fun s _ =>
    uncoupled_beyond_coupling without balanced beyond s g within

/-! ## Threshold blindness: a difference persists until support diverges -/

/-- **Differences kept.** While the flows are alike through `g`'s couplings, exchange following
what couples into `g` keeps every difference on a condition coupled into `g` as it was at the
start. -/
theorem difference_kept
    (balanced : ∀ t e, W.CoupledInto obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.CoupledInto obs g e → L'.BalancesOn W' [e] t)
    (follows : L.ExchangeFollows W L' W' obs g) :
    ∀ t, (∀ s, s < t → W.AlikeThrough obs g W.level W'.level s) →
      ∀ e, W.CoupledInto obs g e → W'.level t e + W.level 0 e = W.level t e + W'.level 0 e
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

/-- While the flows are alike through `g`'s couplings, a second web starting at least as high on
what couples into `g` and alike on what couples into it by level still stands so. -/
theorem levelsAtLeast_while_alike
    (balanced : ∀ t e, W.CoupledInto obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.CoupledInto obs g e → L'.BalancesOn W' [e] t)
    (higher : ∀ e, W.CoupledInto obs g e → W.level 0 e ≤ W'.level 0 e)
    (observedAlike : ∀ e, obs g e → W.level 0 e = W'.level 0 e)
    (follows : L.ExchangeFollows W L' W' obs g) {t : Nat}
    (alike : ∀ s, s < t → W.AlikeThrough obs g W.level W'.level s) :
    W.LevelsAtLeast W' obs g t :=
  ⟨fun e registers => le_of_add_eq_of_le (difference_kept balanced balanced' follows t alike e
      registers) (higher e registers),
   fun e observed => eq_of_add_eq_of_eq (difference_kept balanced balanced' follows t alike e
      (.inr observed)) (observedAlike e observed)⟩

/-- **Alike while supported.** A second web starting at least as high on what couples into `g`
and alike on what couples into it by level: the flows are alike through `g`'s couplings at every
step before which the first web supported `g`. Any number of conditions may differ. -/
theorem alike_while_supported
    (balanced : ∀ t e, W.CoupledInto obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.CoupledInto obs g e → L'.BalancesOn W' [e] t)
    (higher : ∀ e, W.CoupledInto obs g e → W.level 0 e ≤ W'.level 0 e)
    (observedAlike : ∀ e, obs g e → W.level 0 e = W'.level 0 e)
    (follows : L.ExchangeFollows W L' W' obs g) :
    ∀ t, (∀ s, s < t → W.Supported s g) → ∀ s, s < t → W.AlikeThrough obs g W.level W'.level s
  | 0, _, s, before => absurd before (Nat.not_lt_zero s)
  | t + 1, supported, s, before =>
    have past := alike_while_supported balanced balanced' higher observedAlike follows t
      (fun s before => supported s (Nat.lt_succ_of_lt before))
    match Nat.lt_or_eq_of_le (Nat.le_of_lt_succ before) with
    | .inl earlier => past s earlier
    | .inr same => same ▸
        (Web.alikeThrough_iff_of_levelsAtLeast (levelsAtLeast_while_alike balanced balanced'
          higher observedAlike follows past)).mpr fun _ => supported t (Nat.lt_succ_self t)

/-- **A difference changes only after a divergence.** Where a difference on a condition coupled
into `g` has changed by a step, the second web's levels admitted `g` and the first web did not
support it at some earlier step (not every earlier step is otherwise); where activity needs
support, `g` was not active in the first web at every earlier step. A failure of both webs
together is not a divergence. -/
theorem difference_changes_after_divergence
    (balanced : ∀ t e, W.CoupledInto obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.CoupledInto obs g e → L'.BalancesOn W' [e] t)
    (higher : ∀ e, W.CoupledInto obs g e → W.level 0 e ≤ W'.level 0 e)
    (observedAlike : ∀ e, obs g e → W.level 0 e = W'.level 0 e)
    (follows : L.ExchangeFollows W L' W' obs g) {t : Nat} {e : C}
    (registers : W.CoupledInto obs g e)
    (changed : W'.level t e + W.level 0 e ≠ W.level t e + W'.level 0 e) :
    ¬ (∀ s, s < t → (W.Admits (W'.level s) s g → W.Supported s g)) ∧
      (W.Dependent → ¬ ∀ s, s < t → W.active s g) :=
  have diverged : ¬ ∀ s, s < t → (W.Admits (W'.level s) s g → W.Supported s g) := fun never =>
    have alike : ∀ t', t' ≤ t → ∀ s, s < t' → W.AlikeThrough obs g W.level W'.level s :=
      fun t' => Nat.rec (motive := fun t' => t' ≤ t → ∀ s, s < t' →
          W.AlikeThrough obs g W.level W'.level s)
        (fun _ s before => absurd before (Nat.not_lt_zero s))
        (fun k ih le s before =>
          have past := ih (Nat.le_of_succ_le le)
          match Nat.lt_or_eq_of_le (Nat.le_of_lt_succ before) with
          | .inl earlier => past s earlier
          | .inr same => same ▸ (Web.alikeThrough_iff_of_levelsAtLeast
              (levelsAtLeast_while_alike balanced balanced' higher observedAlike follows
                past)).mpr (never k (Nat.lt_of_lt_of_le (Nat.lt_succ_self k) le)))
        t'
    changed (difference_kept balanced balanced' follows t (alike t (Nat.le_refl t)) e registers)
  ⟨diverged, fun dependent active => diverged fun s before _ => dependent s g (active s before)⟩

/-- **Threshold blindness.** Let two flows balance on each condition coupled into `g`, the
exchange there following what couples into `g`, and start alike on every condition coupled into
`g` except a stock `c` coupled into `g` by threshold only, which stands `d` higher in the second.
Then at every step before which the first web supported `g` at every step, the stock stands
exactly `d` higher in the second, every other condition coupled into `g` stands alike, and the
flows have been alike through `g`'s couplings at every earlier step. Where the webs agree on what
`g` requires and needs, being alike through `g`'s couplings is the same support in both
(`Web.admits_iff_supported_of_agree`). -/
theorem subthreshold_alike [DecidableEq C] {c : C} {d : Nat}
    (balanced : ∀ t e, W.CoupledInto obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.CoupledInto obs g e → L'.BalancesOn W' [e] t)
    (depends : W.DependsOn g c) (unobserved : ¬ obs g c)
    (stock : W'.level 0 c = W.level 0 c + d)
    (start : ∀ e, W.CoupledInto obs g e → e ≠ c → W.level 0 e = W'.level 0 e)
    (follows : L.ExchangeFollows W L' W' obs g) :
    ∀ t, (∀ s, s < t → W.Supported s g) →
      W'.level t c = W.level t c + d ∧ (∀ e, W.CoupledInto obs g e → e ≠ c →
        W.level t e = W'.level t e) ∧ ∀ s, s < t → W.AlikeThrough obs g W.level W'.level s :=
  have higher : ∀ e, W.CoupledInto obs g e → W.level 0 e ≤ W'.level 0 e := fun e registers =>
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
the flows are alike through `g`'s couplings at every step. -/
theorem subthreshold_alike_always [DecidableEq C] {c : C} {d : Nat}
    (balanced : ∀ t e, W.CoupledInto obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.CoupledInto obs g e → L'.BalancesOn W' [e] t)
    (depends : W.DependsOn g c) (unobserved : ¬ obs g c)
    (stock : W'.level 0 c = W.level 0 c + d)
    (start : ∀ e, W.CoupledInto obs g e → e ≠ c → W.level 0 e = W'.level 0 e)
    (follows : L.ExchangeFollows W L' W' obs g) (supported : ∀ t, W.Supported t g) :
    ∀ t, W'.level t c = W.level t c + d ∧ W.AlikeThrough obs g W.level W'.level t :=
  fun t =>
    ⟨(subthreshold_alike balanced balanced' depends unobserved stock start follows t
        fun s _ => supported s).1,
     (subthreshold_alike balanced balanced' depends unobserved stock start follows (t + 1)
        fun s _ => supported s).2.2 t (Nat.lt_succ_self t)⟩

end Flow

/-! ## Witnesses -/

/-! ### A formation into which its stock couples by level

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

/-- The stock coupled by level. -/
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
higher. With the stock coupled by level, the two webs are apart through the formation's couplings
at the first step, so exchange following what couples in constrains nothing there; with coupling
by threshold only, the exchange does not follow what couples in. -/
theorem gauge_changes_difference :
    (flow 1).Balances (web 1) ∧ (flow 2).Balances (web 2) ∧ (web 1).Dependent ∧
      (web 2).Dependent ∧ (∀ t, (web 1).Supported t () ∧ (web 2).Supported t ()) ∧
      (web 2).level 0 () = (web 1).level 0 () + 1 ∧
      (web 2).level 1 () ≠ (web 1).level 1 () + 1 ∧
      ¬ (web 1).AlikeThrough stock () (web 1).level (web 2).level 0 ∧
      (flow 1).ExchangeFollows (web 1) (flow 2) (web 2) stock () ∧
      ¬ (flow 1).ExchangeFollows (web 1) (flow 2) (web 2) thresholdOnly () :=
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
gauge of the stock: under `ownStanding` the two webs are apart through the formation's couplings
at the first step. A formation carved so that its reserve is its own standing is never blind below its
threshold there. -/
theorem own_is_stock :
    (∀ g c, stock g c ↔ ownStanding g c) ∧
      ¬ (web 1).AlikeThrough ownStanding () (web 1).level (web 2).level 0 :=
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
alike; from the third, the support passes differently. -/
theorem follows : (flow lowerDraw).ExchangeFollows (web lowerLevel) (flow higherDraw)
    (web higherLevel) thresholdOnly ()
  | 0, _, (), _ => ⟨rfl, rfl⟩
  | 1, _, (), _ => ⟨rfl, rfl⟩
  | t + 2, alike, (), _ => absurd ((alike 2 (Nat.le_add_left 2 t)).1.mpr
      (fun _ _ => Nat.le_refl 1) () trivial) (Nat.not_succ_le_zero 0)

/-- **The difference waits for the divergence.** Through its support only, the higher stock
passes into the formation as the lower before the third step, where the lower web fails to
support it and the higher does: the difference of one unit stands through the third step, as
`Flow.subthreshold_alike` gives, and has changed by the fourth. -/
theorem difference_waits :
    (flow lowerDraw).Balances (web lowerLevel) ∧ (flow higherDraw).Balances (web higherLevel) ∧
      (web lowerLevel).Dependent ∧ (web higherLevel).Dependent ∧
      (flow lowerDraw).ExchangeFollows (web lowerLevel) (flow higherDraw) (web higherLevel)
        thresholdOnly () ∧
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
      (flow draw).ExchangeFollows (web 2) (flow draw) (web 3) thresholdOnly () ∧
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
still supports it. The flows are alike through the dependent's couplings at the first step and the
totals taken differ there: the exchange does not follow what couples into it. -/
theorem higher_breaks_first :
    lowerFlow.Balances (web lowerLevel) ∧ higherFlow.Balances (web higherLevel) ∧
      (web lowerLevel).Dependent ∧ (web higherLevel).Dependent ∧
      (web higherLevel).level 0 () = (web lowerLevel).level 0 () + 1 ∧
      (web lowerLevel).AlikeThrough thresholdOnly dependent (web lowerLevel).level
        (web higherLevel).level 0 ∧
      (web lowerLevel).Supported 1 dependent ∧ ¬ (web higherLevel).Supported 1 dependent ∧
      ¬ (web lowerLevel).AlikeThrough thresholdOnly dependent (web lowerLevel).level
        (web higherLevel).level 1 ∧
      ¬ lowerFlow.ExchangeFollows (web lowerLevel) higherFlow (web higherLevel) thresholdOnly
        dependent :=
  have alike0 : (web lowerLevel).AlikeThrough thresholdOnly dependent (web lowerLevel).level
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

/-- **A gauge of one's own standing passes being taken from.** The predator lies beyond the
prey's influence closure and within its coupling closure under `ownStanding`. With the rest
of the exchange fixed, the flows with and without the predator's part are alike through the prey's
support at every step, and not through a gauge of its own standing after the bite. -/
theorem couples_taking :
    ¬ flow.WithinInfluence web prey predator ∧
      flow.WithinCoupling web ownStanding prey predator ∧
      (∀ t, web.AlikeThrough thresholdOnly prey web.level spared t) ∧
      ¬ web.AlikeThrough ownStanding prey web.level spared 1 :=
  have beyond : ¬ flow.WithinInfluence web prey predator := fun within =>
    Relatum.noConfusion (within (fun x => x = prey) preyAlone_closed rfl)
  ⟨beyond,
   WithinClosure.of_rel ⟨prey, .inr rfl, ⟨0, .head _, .inl Nat.zero_lt_one⟩⟩,
   fun t => Flow.uncoupled_beyond_coupling withheld (fun t _ c _ _ => balances.on [c] t)
     (fun h member => match h, member with
       | predator, _ => fun within => beyond (Flow.withinCoupling_thresholdOnly.mp within)
       | food, no => nomatch no
       | prey, no => nomatch no)
     t prey (WithinClosure.refl _),
   fun alike => absurd (alike.2 prey rfl) (by decide)⟩

/-- **What `Prey` omits.** The difference coupled in makes no difference to the prey: it is
supported, active and admitted by the spared levels at every step. The prey does not bear on
itself, and the predator is active with no standing: the first part of `couples_taking` rests on
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
support it passes alike with the spared levels at every step, while through a gauge of its own
standing it passes at the second step. A bite of two passes through support at the
second step. -/
theorem threshold_on_oneself :
    (∀ t, (web 1).AlikeThrough thresholdOnly prey (web 1).level Prey.spared t) ∧
      ¬ (web 1).AlikeThrough ownStanding prey (web 1).level Prey.spared 1 ∧
      ¬ (web 2).AlikeThrough thresholdOnly prey (web 2).level Prey.spared 1 :=
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

/-- The stock coupled by level. -/
def gauge : Unit → Unit → Prop := fun _ _ => True

/-- **A wrong model excludes what holds.** Relative to the model, at a formation gauging the
stock the claim that the stock comes to nothing, which holds of the actual history, is excluded
at the first step. -/
theorem model_error :
    (∃ T, actual T () = 0) ∧ ¬ still.BalancedHistory actual ∧
      web.ExcludesWithin still.BalancedHistory gauge (fun l' => ∃ T, l' T () = 0) () actual 0 :=
  ⟨⟨1, rfl⟩, fun history => Nat.noConfusion (history 0 ()),
   fun l' history' ⟨T, zero⟩ alike =>
     have same : ∀ s, l' s () = l' 0 () := fun s =>
       Nat.rec (motive := fun s => l' s () = l' 0 ()) rfl
         (fun s ih => (history' s ()).trans ih) s
     have two : l' 0 () = 2 := ((alike 0 (Nat.le_refl 0)).2 () trivial).symm
     Nat.noConfusion ((zero.symm.trans (same T)).trans two)⟩

/-- **What couples in excludes the model.** At the second step no history the model admits is
alike through the gauging formation's couplings: within the model the class alike through it is
empty. -/
theorem model_excluded :
    web.ExcludesWithin still.BalancedHistory gauge (fun _ => True) () actual 1 :=
  fun l' history' _ alike =>
    have zero : l' 1 () = 0 := ((alike 1 (Nat.le_refl 1)).2 () trivial).symm
    have two : l' 0 () = 2 := ((alike 0 (Nat.zero_le 1)).2 () trivial).symm
    Nat.noConfusion (zero.symm.trans ((history' 0 ()).trans two))

end Stationary

namespace Clearing

/-- The source and the clearer: the region of what couples into the clearer. -/
def clearerSide : Formation → Prop
  | .source => True
  | .clearer => True
  | .dweller => False

/-- What couples into a member of the clearer's side, by threshold only, is the resource. -/
theorem couples_resource {g : Formation} {c : Place} (member : clearerSide g)
    (registers : web.CoupledInto thresholdOnly g c) : c = .resource :=
  match registers with
  | .inr no => False.elim no
  | .inl ⟨_, depends⟩ => match g, c, member, depends with
    | .clearer, .resource, _, _ => rfl
    | .source, _, _, no => nomatch no
    | .clearer, .habitat, _, no => nomatch no
    | .clearer, .fuel _, _, no => nomatch no

/-- In a flow in which the dweller does not exchange with the resource, the clearer's side is
closed under being affected through what couples in. -/
theorem clearerSide_closed (L : Flow Formation Place)
    (dwellerQuiet : ∀ t, L.take t .dweller .resource = 0 ∧ L.give t .dweller .resource = 0) :
    ClosedUnder (L.CoupledFrom web thresholdOnly) clearerSide :=
  fun _ h member ⟨c, registers, t, _, exchanges⟩ =>
    match c, couples_resource member registers, h, exchanges with
    | _, rfl, .source, _ => trivial
    | _, rfl, .clearer, _ => trivial
    | _, rfl, .dweller, .inl pos =>
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (dwellerQuiet t).1))
    | _, rfl, .dweller, .inr pos =>
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (dwellerQuiet t).2))

/-- The flows are alike through the clearer's couplings at every step whether or not it clears
the habitat: an instance of `Flow.alike_within_closed`, the clearing being an act on a condition
coupled into no member of its side. -/
theorem alike_for_clearer :
    ∀ t, web.AlikeThroughUpTo thresholdOnly .clearer web.level sparedWeb.level t :=
  fun _ s _ => Flow.alike_within_closed (region := clearerSide)
    (fun t _ c _ _ => balances.on [c] t) (fun t _ c _ _ => spared_balances.on [c] t)
    (clearerSide_closed flow fun _ => ⟨rfl, rfl⟩)
    (clearerSide_closed sparedFlow fun _ => ⟨rfl, rfl⟩)
    (fun _ => rfl)
    (fun _ member c registers => match c, couples_resource member registers with
      | _, rfl => rfl)
    (fun h _ _ _ _ c member registers => match c, couples_resource member registers with
      | _, rfl => match h with
        | .source => ⟨rfl, rfl⟩
        | .clearer => ⟨rfl, rfl⟩
        | .dweller => ⟨rfl, rfl⟩)
    s .clearer trivial

/-- The dweller is ended: from the third step on the levels do not admit it. -/
def DwellerEnded (l : Nat → Place → Nat) : Prop :=
  ∀ n, ¬ web.Admits (l (n + 2)) (n + 2) .dweller

/-- **Testing is relational.** In the world with the habitat spared, the claim that the dweller
is ended is excluded at the clearer at no step, and at the dweller at the third step. -/
theorem tested_by_dweller :
    DwellerEnded web.level ∧
      (∀ t, ¬ web.Excludes thresholdOnly DwellerEnded .clearer sparedWeb.level t) ∧
      web.Excludes thresholdOnly DwellerEnded .dweller sparedWeb.level 2 :=
  ⟨unsupported_with,
   fun t => Web.Excludes.not_of_alike (claim := DwellerEnded) (l' := web.level) unsupported_with
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

/-- **Pooled testing.** In the spared world, the claim that one of them is not admitted at the
third step is excluded there at neither the clearer nor the dweller; at the two together it is. -/
theorem pooled :
    ¬ web.Excludes thresholdOnly EitherEnded .clearer sparedWeb.level 2 ∧
      ¬ web.Excludes thresholdOnly EitherEnded .dweller sparedWeb.level 2 ∧
      web.ExcludesBy thresholdOnly EitherEnded clearerAndDweller sparedWeb.level 2 :=
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

/-- **A complete model idles coupling.** With a model fixing the start and the exchange, the
claim that the dweller is admitted at the third step is excluded at the clearer at the first
step, though nothing about the habitat couples into it. -/
theorem model_idles_coupling :
    web.ExcludesWithin FixedStartAndExchange thresholdOnly (fun l' => web.Admits (l' 2) 2 .dweller)
      .clearer web.level 0 :=
  fun l' ⟨history', start⟩ admits _ =>
    have same : l' 2 .habitat = web.level 2 .habitat :=
      Flow.BalancedHistory.agree history' balances (start .habitat) 2
    Nat.not_succ_le_zero 0 (Nat.le_trans (admits .habitat trivial) (Nat.le_of_eq same))

end Clearing

end Becoming
