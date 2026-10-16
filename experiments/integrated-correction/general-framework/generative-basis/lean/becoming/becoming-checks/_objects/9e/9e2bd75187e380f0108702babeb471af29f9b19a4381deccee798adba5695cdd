import Becoming.Renewal

/-!
# Dependence that forms, holds, breaks and transforms

`Becoming.Renewal` reads a run through conditions whose dependences are fixed: which
conditions a formation needs, at what level, and which it draws on stay the same
throughout. Here they are observables of the configuration as well. A formation can
come to depend on a condition, need more or less of it, or cease to depend on it.
These changes belong to the same unfolding as the levels they concern.

A dependence holding at a step is read across that step. It is *kept* when the
condition meets it at the step and after it, and *broken* when it was met and the
condition falls below it. One step does not say whether a dependence that changes
during the step ended before the fall or because of it; the reading counts the fall
against the dependence as it stood when the step began.

Results:
* Constant dependence is the static reading of `RelationalRenewal`, recovered exactly:
  support, renewal, consumption and the classes of formations agree.
* Change is made at a step: a dependence that holds at one step and not at a later
  one dissolved across a step between, and one that comes to hold formed across one.
  This is stated without excluded middle: no stretch of the run avoids such a step.
* Renewal and consumption remain exclusive, and renewal keeps every renewing
  formation supported.
* Every met dependence is kept or broken across each step, and not both.
* A formation that continues after a loss with a dependence at least as strong as
  before finds the condition restored. After a loss without return, a formation that
  continues has therefore transformed its dependence; with constant dependence it
  ends. Ending, transformation and restoration are the three ways through a loss.
* The three ways are distinct possibilities: in one process, from one configuration,
  the same broken dependence leads to an ending, to a transformation (one dependence
  dissolves as another forms) and to a restoration. The loss does not decide its issue.
* A stepwise reading credits a formation's event when its step keeps every dependence
  on the conditions the formation participates in. Whole-run renewal credits every
  active step. Otherwise the two readings differ in both directions: a formation can
  draw within renewal at first and consume later, and an event can break a condition
  that is later restored, so that its formation does not consume in the run. A
  formation can also keep its conditions at each of its own steps while another
  formation breaks them, so whole-run renewal is not the conjunction of a formation's
  steps.

No ethical predicate, ranking or axiom occurs. Which observables represent an actual
history, and whether a change of dependence preceded a fall, are application duties.
-/

namespace Becoming

open Generative RelationalRenewal

universe u v

/-! ## Change is made at a step -/

/-- What holds at `T` and fails at a later `t` ceased across some step between them. -/
theorem ceases_at_a_step {p : Nat → Prop} {T t : Nat} (le : T ≤ t) (holds : p T)
    (fails : ¬ p t) : ¬ ∀ s, T ≤ s → s < t → ¬ (p s ∧ ¬ p (s + 1)) := by
  induction le with
  | refl => exact fun _ => fails holds
  | @step m within earlier =>
    intro none
    exact earlier (fun yes => none m within (Nat.lt_succ_self m) ⟨yes, fails⟩)
      (fun s from_ below => none s from_ (Nat.lt_succ_of_lt below))

/-- What fails at `T` and holds at a later `t` arose across some step between them. -/
theorem arises_at_a_step {p : Nat → Prop} {T t : Nat} (le : T ≤ t) (absent : ¬ p T)
    (holds : p t) : ¬ ∀ s, T ≤ s → s < t → ¬ (¬ p s ∧ p (s + 1)) := by
  induction le with
  | refl => exact fun _ => absent holds
  | @step m within earlier =>
    intro none
    exact none m within (Nat.lt_succ_self m) ⟨fun yes =>
      earlier yes (fun s from_ below => none s from_ (Nat.lt_succ_of_lt below)), holds⟩

/-! ## Dependence as an observable of the configuration -/

/-- Levels of conditions, the formations active at each configuration, and which
conditions each formation there depends on (at what level) and draws on. -/
structure Dependence (S : Type u) (F C : Type) where
  level : S → C → Nat
  active : S → F → Prop
  requires : S → F → C → Prop
  need : S → F → C → Nat
  draws : S → F → C → Prop

/-- One unfolding read through conditions and the dependences among them, all of
which may change from step to step. -/
structure Web (F C : Type) where
  level : Nat → C → Nat
  active : Nat → F → Prop
  requires : Nat → F → C → Prop
  need : Nat → F → C → Nat
  draws : Nat → F → C → Prop

variable {S : Type u} {A : Type v} {F C : Type}

/-- A run read through its dependences. -/
def Dependence.along (K : Dependence S F C) {P : Process S A} (r : Run P) : Web F C :=
  ⟨fun t => K.level (r.state t), fun t => K.active (r.state t),
    fun t => K.requires (r.state t), fun t => K.need (r.state t), fun t => K.draws (r.state t)⟩

/-- Fixed dependences: the conditions of `Becoming.Renewal`. -/
def Conditions.dependence (K : Conditions S F C) : Dependence S F C :=
  ⟨K.level, K.active, fun _ => K.requires, fun _ => K.need, fun _ => K.draws⟩

namespace Web

variable (W : Web F C)

/-- The conditions a formation depends on at a step support it there. -/
def Supported (t : Nat) (f : F) : Prop :=
  ∀ c, W.requires t f c → W.need t f c ≤ W.level t c

/-- A formation is active only where the conditions it then depends on support it. -/
def Dependent : Prop :=
  ∀ t f, W.active t f → W.Supported t f

/-- The step from `t` keeps `g`'s dependence on `c`: met at `t` and after the step. -/
def Kept (t : Nat) (g : F) (c : C) : Prop :=
  W.need t g c ≤ W.level t c ∧ W.need t g c ≤ W.level (t + 1) c

/-- The step from `t` breaks `g`'s dependence on `c`: met at `t`, not after the step. -/
def Broken (t : Nat) (g : F) (c : C) : Prop :=
  W.requires t g c ∧ W.need t g c ≤ W.level t c ∧ W.level (t + 1) c < W.need t g c

/-- Every dependence on the condition is kept at every step. -/
def Renewed (c : C) : Prop :=
  ∀ t g, W.requires t g c → W.Kept t g c

/-- A dependence holding at some step is never met again afterwards. -/
def Consumed (c : C) : Prop :=
  ∃ g T, W.requires T g c ∧ ∀ t, T < t → W.level t c < W.need T g c

/-- A met dependence is broken and never met again: a formed relationship is lost. -/
def Lost (c : C) : Prop :=
  ∃ g T, W.Broken T g c ∧ ∀ t, T < t → W.level t c < W.need T g c

/-- The relations a formation participates in at a step, through dependence or drawing. -/
def Participates (t : Nat) (f : F) (c : C) : Prop :=
  W.requires t f c ∨ W.draws t f c

def RenewingIn (f : F) : Prop :=
  ∀ t c, W.Participates t f c → W.Renewed c

def ConsumingIn (f : F) : Prop :=
  ∃ t c, W.draws t f c ∧ W.Consumed c

/-- A dependence forms across the step from `t`. -/
def Forms (t : Nat) (g : F) (c : C) : Prop :=
  ¬ W.requires t g c ∧ W.requires (t + 1) g c

/-- A dependence dissolves across the step from `t`. -/
def Dissolves (t : Nat) (g : F) (c : C) : Prop :=
  W.requires t g c ∧ ¬ W.requires (t + 1) g c

/-! ## Constant dependence is the static reading -/

/-- The static unfolding of `RelationalRenewal`, whose dependences never change. -/
def static (U : Unfolding F C) : Web F C :=
  ⟨U.level, U.active, fun _ => U.requires, fun _ => U.need, fun _ => U.draws⟩

variable {W}

theorem static_supported (U : Unfolding F C) (t : Nat) (f : F) :
    (static U).Supported t f ↔ RelationalRenewal.Supported U t f :=
  Iff.rfl

theorem static_dependent (U : Unfolding F C) :
    (static U).Dependent ↔ RelationalRenewal.Dependent U :=
  Iff.rfl

theorem static_renewed (U : Unfolding F C) (c : C) :
    (static U).Renewed c ↔ RelationalRenewal.Renewed U c :=
  ⟨fun renewed t g depends => (renewed t g depends).1,
   fun renewed t g depends => ⟨renewed t g depends, renewed (t + 1) g depends⟩⟩

theorem static_consumed (U : Unfolding F C) (c : C) :
    (static U).Consumed c ↔ RelationalRenewal.Consumed U c :=
  ⟨fun ⟨g, T, depends, below⟩ => ⟨g, T + 1, depends, below⟩,
   fun ⟨g, T, depends, below⟩ => ⟨g, T, depends, fun t later => below t (Nat.le_of_lt later)⟩⟩

theorem static_renewingIn (U : Unfolding F C) (f : F) :
    (static U).RenewingIn f ↔ RelationalRenewal.RenewingIn U f :=
  ⟨fun renewing c joins => (static_renewed U c).mp (renewing 0 c joins),
   fun renewing _ c joins => (static_renewed U c).mpr (renewing c joins)⟩

theorem static_consumingIn (U : Unfolding F C) (f : F) :
    (static U).ConsumingIn f ↔ RelationalRenewal.ConsumingIn U f :=
  ⟨fun ⟨_, c, drawn, consumed⟩ => ⟨c, drawn, (static_consumed U c).mp consumed⟩,
   fun ⟨c, drawn, consumed⟩ => ⟨0, c, drawn, (static_consumed U c).mpr consumed⟩⟩

/-- Reading a run through fixed dependences is the static reading of the run. -/
theorem conditions_along (K : Conditions S F C) {P : Process S A} (r : Run P) :
    K.dependence.along r = static (K.along r) :=
  rfl

/-! ## Renewal, consumption and loss -/

theorem renewed_not_consumed {c : C} (renewed : W.Renewed c) : ¬ W.Consumed c
  | ⟨g, T, depends, below⟩ =>
    Nat.not_le_of_gt (below (T + 1) (Nat.lt_succ_self T)) (renewed T g depends).2

theorem renewing_not_consuming {f : F} (renewing : W.RenewingIn f) : ¬ W.ConsumingIn f
  | ⟨t, c, drawn, consumed⟩ => renewed_not_consumed (renewing t c (Or.inr drawn)) consumed

/-- Renewal keeps a renewing formation supported at every step. -/
theorem renewing_keeps_support {f : F} (renewing : W.RenewingIn f) (t : Nat) :
    W.Supported t f :=
  fun c depends => (renewing t c (Or.inl depends) t f depends).1

theorem lost_consumed {c : C} : W.Lost c → W.Consumed c
  | ⟨g, T, ⟨depends, _, _⟩, below⟩ => ⟨g, T, depends, below⟩

/-- A dependence holding at `T` and not at a later `t` dissolved across a step between. -/
theorem dissolves_between {T t : Nat} {g : F} {c : C} (le : T ≤ t)
    (held : W.requires T g c) (gone : ¬ W.requires t g c) :
    ¬ ∀ s, T ≤ s → s < t → ¬ W.Dissolves s g c :=
  ceases_at_a_step (p := fun s => W.requires s g c) le held gone

/-- A dependence absent at `T` and holding at a later `t` formed across a step between. -/
theorem forms_between {T t : Nat} {g : F} {c : C} (le : T ≤ t)
    (absent : ¬ W.requires T g c) (held : W.requires t g c) :
    ¬ ∀ s, T ≤ s → s < t → ¬ W.Forms s g c :=
  arises_at_a_step (p := fun s => W.requires s g c) le absent held

/-- Every met dependence is kept or broken across each step. -/
theorem kept_or_broken {t : Nat} {g : F} {c : C} (depends : W.requires t g c)
    (met : W.need t g c ≤ W.level t c) : W.Kept t g c ∨ W.Broken t g c :=
  match Nat.lt_or_ge (W.level (t + 1) c) (W.need t g c) with
  | .inl fell => .inr ⟨depends, met, fell⟩
  | .inr held => .inl ⟨met, held⟩

theorem kept_not_broken {t : Nat} {g : F} {c : C} (kept : W.Kept t g c) : ¬ W.Broken t g c
  | ⟨_, _, fell⟩ => Nat.not_le_of_gt fell kept.2

/-! ## Three ways through a loss -/

/-- A formation active with a dependence at least as strong as an earlier one finds
the condition meeting the earlier need: continuing unchanged is restoration. -/
theorem continuing_restores (dependent : W.Dependent) {T t : Nat} {g : F} {c : C}
    (active : W.active t g) (depends : W.requires t g c)
    (unchanged : W.need T g c ≤ W.need t g c) : W.need T g c ≤ W.level t c :=
  Nat.le_trans unchanged (dependent t g active c depends)

/-- After a loss without return, a formation that is still active has transformed its
dependence: it no longer depends on the condition as strongly as before. -/
theorem consumed_continues_transformed (dependent : W.Dependent) {T : Nat} {g : F} {c : C}
    (below : ∀ t, T < t → W.level t c < W.need T g c) {t : Nat} (later : T < t)
    (active : W.active t g) : ¬ (W.requires t g c ∧ W.need T g c ≤ W.need t g c)
  | ⟨depends, unchanged⟩ =>
    Nat.not_le_of_gt (below t later) (continuing_restores dependent active depends unchanged)

/-- With dependence that does not change, a loss without return ends the formation. -/
theorem consumed_ends_when_fixed (dependent : W.Dependent) {T : Nat} {g : F} {c : C}
    (fixed : ∀ t, T < t → W.requires t g c ∧ W.need T g c ≤ W.need t g c)
    (below : ∀ t, T < t → W.level t c < W.need T g c) :
    ∀ t, T < t → ¬ W.active t g :=
  fun t later active => consumed_continues_transformed dependent below later active (fixed t later)

/-! ## A stepwise reading -/

/-- A formation's event at `t` is within renewal: it is active, and the step keeps
every dependence on every condition it participates in. -/
def RenewingAt (t : Nat) (f : F) : Prop :=
  W.active t f ∧ ∀ c, W.Participates t f c → ∀ g, W.requires t g c → W.Kept t g c

/-- Whole-run renewal credits every active step. -/
theorem renewing_at_active {f : F} (renewing : W.RenewingIn f) {t : Nat}
    (active : W.active t f) : W.RenewingAt t f :=
  ⟨active, fun c joins g depends => renewing t c joins t g depends⟩

/-- An event whose step breaks a dependence on a condition it participates in is not
within renewal. -/
theorem not_renewing_at_of_broken {t : Nat} {f g : F} {c : C} (joins : W.Participates t f c)
    (broken : W.Broken t g c) : ¬ W.RenewingAt t f
  | ⟨_, keeps⟩ => kept_not_broken (keeps c joins g broken.1) broken

end Web

/-! ## The three ways are distinct possibilities -/

namespace Crossing

/-- How the formation stands: active on the first condition, dormant on it, active on
the second instead, or ended. -/
inductive Mode where
  | onFirst
  | dormant
  | onSecond
  | ended

inductive Source where
  | first
  | second

/-- The level of the first condition and the formation's mode; the second condition
stays at level one. -/
structure State where
  first : Nat
  mode : Mode

inductive Move where
  | rest
  /-- The first condition falls to zero while the formation takes the given mode. -/
  | fall (mode : Mode)
  /-- The first condition is renewed and a dormant formation resumes on it. -/
  | renew

def process : Process State Move where
  step s a t := match a with
    | .rest => t = s
    | .fall m => s.first = 1 ∧ t = ⟨0, m⟩
    | .renew => s.mode = .dormant ∧ t = ⟨1, .onFirst⟩

/-- Whether the formation is active in a mode. -/
def Mode.active : Mode → Prop
  | .onFirst => True
  | .dormant => False
  | .onSecond => True
  | .ended => False

/-- Which condition the formation depends on in a mode. -/
def Mode.requires : Mode → Source → Prop
  | .onFirst, .first => True
  | .onFirst, .second => False
  | .dormant, .first => True
  | .dormant, .second => False
  | .onSecond, .first => False
  | .onSecond, .second => True
  | .ended, _ => False

def dependence : Dependence State Unit Source where
  level s
    | .first => s.first
    | .second => 1
  active s _ := s.mode.active
  requires s _ c := s.mode.requires c
  need _ _ _ := 1
  draws _ _ _ := False

def start : State := ⟨1, .onFirst⟩

def endingState : Nat → State
  | 0 => start
  | _ + 1 => ⟨0, .ended⟩

def transformingState : Nat → State
  | 0 => start
  | _ + 1 => ⟨0, .onSecond⟩

def restoringState : Nat → State
  | 0 => start
  | 1 => ⟨0, .dormant⟩
  | _ + 2 => start

/-- The formation ends with the loss. -/
def ending : Run process :=
  ⟨endingState, fun | 0 => .fall .ended | _ + 1 => .rest,
    fun | 0 => ⟨rfl, rfl⟩ | _ + 1 => rfl⟩

/-- The formation ceases to depend on the first condition and comes to depend on the
second. -/
def transforming : Run process :=
  ⟨transformingState, fun | 0 => .fall .onSecond | _ + 1 => .rest,
    fun | 0 => ⟨rfl, rfl⟩ | _ + 1 => rfl⟩

/-- The formation waits on the first condition, which is renewed. -/
def restoring : Run process :=
  ⟨restoringState, fun | 0 => .fall .dormant | 1 => .renew | _ + 2 => .rest,
    fun | 0 => ⟨rfl, rfl⟩ | 1 => ⟨rfl, rfl⟩ | _ + 2 => rfl⟩

theorem ending_dependent : (dependence.along ending).Dependent
  | 0, _, _, .first, _ => Nat.le_refl 1
  | 0, _, _, .second, depends => False.elim depends
  | _ + 1, _, active, _, _ => False.elim active

theorem transforming_dependent : (dependence.along transforming).Dependent
  | 0, _, _, .first, _ => Nat.le_refl 1
  | 0, _, _, .second, depends => False.elim depends
  | _ + 1, _, _, .first, depends => False.elim depends
  | _ + 1, _, _, .second, _ => Nat.le_refl 1

theorem restoring_dependent : (dependence.along restoring).Dependent
  | 0, _, _, .first, _ => Nat.le_refl 1
  | 0, _, _, .second, depends => False.elim depends
  | 1, _, active, _, _ => False.elim active
  | _ + 2, _, _, .first, _ => Nat.le_refl 1
  | _ + 2, _, _, .second, depends => False.elim depends

/-- One process, one configuration, one broken dependence, three issues. Each run
breaks the formation's dependence on the first condition at its first step. In the
first the formation ends and the loss has no return. In the second the dependence
dissolves as one on the second condition forms, the formation stays active, and the
loss has no return. In the third the formation waits, the condition is renewed, and
the same dependence is kept again from then on. -/
theorem loss_does_not_decide :
    ending.state 0 = transforming.state 0 ∧ transforming.state 0 = restoring.state 0 ∧
    (dependence.along ending).Broken 0 () .first ∧
    (dependence.along transforming).Broken 0 () .first ∧
    (dependence.along restoring).Broken 0 () .first ∧
    (dependence.along ending).Lost .first ∧
    (∀ t, 0 < t → ¬ (dependence.along ending).active t ()) ∧
    (dependence.along transforming).Lost .first ∧
    (dependence.along transforming).Dissolves 0 () .first ∧
    (dependence.along transforming).Forms 0 () .second ∧
    (∀ t, (dependence.along transforming).active t ()) ∧
    ¬ (dependence.along restoring).Consumed .first ∧
    (∀ t, 2 ≤ t → (dependence.along restoring).active t () ∧
      (dependence.along restoring).requires t () .first ∧
      (dependence.along restoring).Kept t () .first) := by
  refine ⟨rfl, rfl, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩,
    ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩,
    ⟨(), 0, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩, fun | _ + 1, _ => Nat.zero_lt_one⟩,
    fun | _ + 1, _ => id,
    ⟨(), 0, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩, fun | _ + 1, _ => Nat.zero_lt_one⟩,
    ⟨trivial, id⟩, ⟨id, trivial⟩, fun | 0 => trivial | _ + 1 => trivial, ?_,
    fun | _ + 2, _ => ⟨trivial, trivial, Nat.le_refl 1, Nat.le_refl 1⟩⟩
  intro ⟨_, T, _, below⟩
  exact Nat.lt_irrefl 1 (below (T + 2) (Nat.lt_of_lt_of_le (Nat.lt_succ_self T) (Nat.le_succ _)))

end Crossing

/-! ## The stepwise and whole-run readings differ -/

namespace Commons

def escalatingState : Nat → Nat
  | 0 => 1
  | 1 => 1
  | _ + 2 => 0

/-- Drawing within renewal at first, then beyond it. -/
def escalating : Run process :=
  ⟨escalatingState, fun | 0 => 1 | _ + 1 => 2, fun | 0 => rfl | 1 => rfl | _ + 2 => rfl⟩

/-- The whole-run reading counts the focal formation as consuming, while the stepwise
reading credits its first event, which drew within renewal, and not its second. -/
theorem stepwise_credits_before_escalation :
    (conditions.dependence.along escalating).ConsumingIn .focal ∧
    (conditions.dependence.along escalating).RenewingAt 0 .focal ∧
    ¬ (conditions.dependence.along escalating).RenewingAt 1 .focal := by
  refine ⟨⟨0, (), trivial, .sustaining, 1, trivial, fun | _ + 2, _ => Nat.zero_lt_one⟩,
    ⟨trivial, fun _ _ g depends => ?_⟩, fun ⟨_, keeps⟩ => ?_⟩
  · cases g with
    | focal => exact False.elim depends
    | sustaining => exact ⟨Nat.le_refl 1, Nat.le_refl 1⟩
  · exact Nat.not_succ_le_zero 0 (keeps () (Or.inr trivial) .sustaining trivial).2

def dippingState : Nat → Nat
  | 0 => 1
  | 1 => 0
  | _ + 2 => 1

/-- Drawing beyond renewal once, then pausing while the condition is renewed. -/
def dipping : Run process :=
  ⟨dippingState, fun | 0 => 2 | 1 => 0 | _ + 2 => 1, fun | 0 => rfl | 1 => rfl | _ + 2 => rfl⟩

/-- The whole-run reading does not count the focal formation as consuming, since the
condition returns, while the stepwise reading withholds its first event, whose step
breaks the sustaining formation's dependence. -/
theorem dip_breaks_without_consuming :
    ¬ (conditions.dependence.along dipping).ConsumingIn .focal ∧
    ¬ (conditions.dependence.along dipping).RenewingAt 0 .focal := by
  refine ⟨fun ⟨_, _, _, g, T, depends, below⟩ => ?_,
    Web.not_renewing_at_of_broken (g := .sustaining) (c := ()) (Or.inr trivial)
      ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩⟩
  cases g with
  | focal => exact depends
  | sustaining =>
    exact Nat.lt_irrefl 1 (below (T + 2) (Nat.lt_of_lt_of_le (Nat.lt_succ_self T) (Nat.le_succ _)))

end Commons

namespace Dip

inductive Formation where
  | keeper
  | drawer

/-- A shared condition dips for one step and is renewed. -/
def levels : Nat → Nat
  | 0 => 1
  | 1 => 1
  | 2 => 0
  | _ + 3 => 1

/-- The keeper is active wherever the condition meets its need at both ends of its step. -/
def keeperActive : Nat → Prop
  | 0 => True
  | 1 => False
  | 2 => False
  | _ + 3 => True

/-- The drawer draws on the condition once. -/
def drawerActive : Nat → Prop
  | 0 => False
  | 1 => True
  | _ + 2 => False

/-- The keeper depends on the condition throughout; the drawer only draws on it. -/
def web : Web Formation Unit where
  level t _ := levels t
  active t
    | .keeper => keeperActive t
    | .drawer => drawerActive t
  requires _ f _ := match f with
    | .keeper => True
    | .drawer => False
  need _ _ _ := 1
  draws t
    | .keeper => fun _ => False
    | .drawer => fun _ => drawerActive t

/-- The keeper is within renewal at each of its own steps, yet does not renew in the
run: the drawer breaks the shared condition while the keeper is inactive. Whole-run
renewal reads the shared condition, so it is not the conjunction of a formation's
steps. -/
theorem renewing_at_each_step_not_in_run :
    web.Dependent ∧ (∀ t, web.active t .keeper → web.RenewingAt t .keeper) ∧
    ¬ web.RenewingIn .keeper := by
  refine ⟨?_, ?_, fun renewing => ?_⟩
  · intro t f active c depends
    cases f with
    | drawer => exact False.elim depends
    | keeper =>
      match t, active with
      | 0, _ => exact Nat.le_refl 1
      | _ + 3, _ => exact Nat.le_refl 1
  · intro t active
    refine ⟨active, fun _ _ g depends => ?_⟩
    cases g with
    | drawer => exact False.elim depends
    | keeper =>
      match t, active with
      | 0, _ => exact ⟨Nat.le_refl 1, Nat.le_refl 1⟩
      | _ + 3, _ => exact ⟨Nat.le_refl 1, Nat.le_refl 1⟩
  · exact Nat.not_succ_le_zero 0 (renewing 0 () (Or.inl trivial) 1 .keeper trivial).2

end Dip

end Becoming
