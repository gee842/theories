import Becoming.Return

/-!
# Joint activity and difference-making

A loss across a step can be read in two ways. The relational reading of
`Becoming.Dependence` asks which formations participate in the condition that is lost:
every formation drawing on a consumed condition is consuming in the run. The but-for
reading asks whose part of the activity the loss depends on: a formation's part makes
the difference when, with that part withheld and the rest as it was, the change keeps
the dependence.

Withholding stays within the unfolding: the alternative is another configuration of
the same process, the one in which that part is absent. Nothing outside the process
supplies the comparison.

Results:
* Keeping and breaking across a change of configuration are exclusive. Along a run they
  are the keeping and breaking of `Becoming.Dependence`.
* When a loss is overdetermined, so that withholding any single part still leaves a
  breaking step, no single formation's part makes the difference.
* Difference-making belongs to the joint activity, not to a formation's own part. In one
  process, from configurations at the same level where a drawer takes the same amount,
  its part makes the difference when one other formation draws, and does not when two
  others draw. Withholding two parts then keeps the dependence: the difference is made
  jointly. In both runs the relational reading counts the drawer as consuming, and it
  counts a formation that takes nothing as not consuming.
* A formation's events over time are a joint activity too. Drawing beyond renewal at
  every step drains the condition, so the run consumes it. The first event's step keeps
  the dependence, so it does not break for any cycle. With any single event's draw
  withheld, the condition is still consumed, so no event alone makes the difference.
  Of the readings here, only the whole-run reading counts the depletion.

No ethical predicate, ranking or axiom occurs. Whether withholding a part leaves the rest
of the activity as it was is a modelling duty of each application. Responsibility is
not inferred from either reading.
-/

namespace Becoming

open Generative

universe u v

variable {S : Type u} {A : Type v} {F C : Type}

namespace Dependence

variable (K : Dependence S F C)

/-- The change from `s` to `t` keeps `g`'s dependence on `c` as it stands at `s`. -/
def Keeps (s t : S) (g : F) (c : C) : Prop :=
  K.need s g c ≤ K.level s c ∧ K.need s g c ≤ K.level t c

/-- The change from `s` to `t` breaks `g`'s dependence on `c`: met at `s`, not at `t`. -/
def Breaks (s t : S) (g : F) (c : C) : Prop :=
  K.requires s g c ∧ K.need s g c ≤ K.level s c ∧ K.level t c < K.need s g c

/-- Some admissible step from `s` breaks `g`'s dependence on `c`. -/
def BreaksFrom (P : Process S A) (s : S) (g : F) (c : C) : Prop :=
  ∃ a t, P.step s a t ∧ K.Breaks s t g c

/-- The but-for test: some step from `s` breaks the dependence, and with `f`'s part
withheld every step keeps it. -/
def MakesDifference (P : Process S A) (withhold : F → S → S) (f : F) (s : S) (g : F)
    (c : C) : Prop :=
  K.BreaksFrom P s g c ∧ ∀ a t, P.step (withhold f s) a t → K.Keeps (withhold f s) t g c

/-- Withholding any single part still leaves a breaking step. -/
def Overdetermined (P : Process S A) (withhold : F → S → S) (s : S) (g : F) (c : C) :
    Prop :=
  K.BreaksFrom P s g c ∧ ∀ f, K.BreaksFrom P (withhold f s) g c

variable {K}

theorem keeps_not_breaks {s t : S} {g : F} {c : C} (keeps : K.Keeps s t g c) :
    ¬ K.Breaks s t g c
  | ⟨_, _, fell⟩ => Nat.not_le_of_gt fell keeps.2

theorem along_kept {P : Process S A} (r : Run P) (n : Nat) (g : F) (c : C) :
    (K.along r).Kept n g c ↔ K.Keeps (r.state n) (r.state (n + 1)) g c :=
  Iff.rfl

theorem along_broken {P : Process S A} (r : Run P) (n : Nat) (g : F) (c : C) :
    (K.along r).Broken n g c ↔ K.Breaks (r.state n) (r.state (n + 1)) g c :=
  Iff.rfl

/-- When the loss is overdetermined, no single part makes the difference. -/
theorem Overdetermined.no_difference {P : Process S A} {withhold : F → S → S} {s : S}
    {g : F} {c : C} (over : K.Overdetermined P withhold s g c) (f : F) :
    ¬ K.MakesDifference P withhold f s g c
  | ⟨_, keeps⟩ =>
    match over.2 f with
    | ⟨a, t, step, breaks⟩ => keeps_not_breaks (keeps a t step) breaks

end Dependence

/-! ## Difference-making belongs to the joint activity -/

namespace Pool

inductive Formation where
  | first
  | second
  | third
  | sustaining

/-- What each drawer takes from the shared condition in one step. -/
structure Draw where
  first : Nat
  second : Nat
  third : Nat

def Draw.total (d : Draw) : Nat :=
  d.first + d.second + d.third

def Draw.part : Draw → Formation → Nat
  | d, .first => d.first
  | d, .second => d.second
  | d, .third => d.third
  | _, .sustaining => 0

def Draw.without : Formation → Draw → Draw
  | .first, d => ⟨0, d.second, d.third⟩
  | .second, d => ⟨d.first, 0, d.third⟩
  | .third, d => ⟨d.first, d.second, 0⟩
  | .sustaining, d => d

/-- The level of the shared condition and the draws being taken from it. -/
structure State where
  level : Nat
  drawing : Draw

/-- The condition is renewed by one unit while the current draws are taken; the action
sets the next draws. -/
def process : Process State Draw :=
  ⟨fun s next t => t = ⟨s.level + 1 - s.drawing.total, next⟩⟩

/-- The same configuration with one formation's part withheld. -/
def withhold (f : Formation) (s : State) : State :=
  ⟨s.level, s.drawing.without f⟩

/-- Which formation depends on the condition: the sustaining one, at level one. -/
def Formation.requires : Formation → Prop
  | .first => False
  | .second => False
  | .third => False
  | .sustaining => True

/-- The drawers are active throughout; the sustaining formation while supported. -/
def Formation.active (s : State) : Formation → Prop
  | .first => True
  | .second => True
  | .third => True
  | .sustaining => 1 ≤ s.level

def dependence : Dependence State Formation Unit where
  level s _ := s.level
  active s f := f.active s
  requires _ f _ := f.requires
  need _ _ _ := 1
  draws s f _ := 0 < s.drawing.part f

/-- Two drawers take one unit each. -/
def pair : Draw := ⟨1, 1, 0⟩

/-- Three drawers take one unit each. -/
def all : Draw := ⟨1, 1, 1⟩

/-- The condition starts at level one and is drawn down to zero, where it stays. -/
def steady (d : Draw) : Nat → State
  | 0 => ⟨1, d⟩
  | _ + 1 => ⟨0, d⟩

def pairRun : Run process :=
  ⟨steady pair, fun _ => pair, fun | 0 => rfl | _ + 1 => rfl⟩

def allRun : Run process :=
  ⟨steady all, fun _ => all, fun | 0 => rfl | _ + 1 => rfl⟩

/-- From level one, draws that take everything the step leaves break the dependence. -/
theorem breaks_from_one (d : Draw) (exhausts : 1 + 1 - d.total = 0) :
    dependence.BreaksFrom process ⟨1, d⟩ .sustaining () :=
  ⟨d, ⟨0, d⟩, (congrArg (State.mk · d) exhausts).symm, trivial, Nat.le_refl 1,
    Nat.zero_lt_one⟩

/-- Drawn down to zero and left there, the condition is consumed. -/
theorem steady_consumed (d : Draw) (steps : ∀ n, process.step (steady d n) d (steady d (n + 1))) :
    (dependence.along ⟨steady d, fun _ => d, steps⟩).Consumed () :=
  ⟨.sustaining, 0, trivial, fun | _ + 1, _ => Nat.zero_lt_one⟩

/-- One process, two configurations at the same level, the first drawer taking the same
amount. With one other drawer the first drawer's part makes the difference to the loss;
with two others the loss is overdetermined and it does not, while withholding two parts
keeps the dependence. In both runs the relational reading counts the first drawer as
consuming; in the first it counts the third, which takes nothing, as not consuming. -/
theorem difference_belongs_to_the_joint :
    (pairRun.state 0).level = (allRun.state 0).level ∧
    (pairRun.state 0).drawing.first = (allRun.state 0).drawing.first ∧
    dependence.MakesDifference process withhold .first (pairRun.state 0) .sustaining () ∧
    dependence.Overdetermined process withhold (allRun.state 0) .sustaining () ∧
    ¬ dependence.MakesDifference process withhold .first (allRun.state 0) .sustaining () ∧
    (∀ a t, process.step (withhold .second (withhold .first (allRun.state 0))) a t →
      dependence.Keeps (withhold .second (withhold .first (allRun.state 0))) t
        .sustaining ()) ∧
    (dependence.along pairRun).ConsumingIn .first ∧
    ¬ (dependence.along pairRun).ConsumingIn .third ∧
    (dependence.along allRun).ConsumingIn .first := by
  have over : dependence.Overdetermined process withhold (allRun.state 0) .sustaining () :=
    ⟨breaks_from_one all rfl, fun
      | .first => breaks_from_one _ rfl
      | .second => breaks_from_one _ rfl
      | .third => breaks_from_one _ rfl
      | .sustaining => breaks_from_one _ rfl⟩
  refine ⟨rfl, rfl, ⟨breaks_from_one pair rfl, fun _ _ step => ?_⟩, over,
    over.no_difference .first, fun _ _ step => ?_,
    ⟨0, (), Nat.zero_lt_one, steady_consumed pair pairRun.step⟩,
    fun ⟨t, _, drawn, _⟩ => ?_, ⟨0, (), Nat.zero_lt_one, steady_consumed all allRun.step⟩⟩
  · subst step
    exact ⟨Nat.le_refl 1, Nat.le_refl 1⟩
  · subst step
    exact ⟨Nat.le_refl 1, Nat.le_refl 1⟩
  · match t, drawn with
    | 0, drawn => exact Nat.lt_irrefl 0 drawn
    | _ + 1, drawn => exact Nat.lt_irrefl 0 drawn

end Pool

/-! ## A formation's events over time are a joint activity -/

/-- As `Nat.sub_self_add`, with an empty axiom report. -/
theorem sub_self_add (n : Nat) : ∀ m, n - (n + m) = 0
  | 0 => Nat.sub_self n
  | m + 1 => congrArg Nat.pred (sub_self_add n m)

namespace Commons

/-- The levels of the shared condition from `start` under the draws `draw`. -/
def levels (start : Nat) (draw : Nat → Nat) : Nat → Nat
  | 0 => start
  | t + 1 => levels start draw t + 1 - draw t

/-- The run of the commons from `start` under the draws `draw`. -/
def drawing (start : Nat) (draw : Nat → Nat) : Run process :=
  ⟨levels start draw, draw, fun _ => rfl⟩

/-- A step drawing at least two units, where one is renewed, lowers the level. -/
theorem overdraw_lowers (s : Nat) : ∀ a, 2 ≤ a → s + 1 - a ≤ s.pred
  | 0, over => absurd over (Nat.not_succ_le_zero 1)
  | 1, over => absurd over (Nat.not_succ_le_self 1)
  | 2, _ => Nat.le_refl _
  | a + 3, _ => Nat.le_trans (Nat.pred_le _) (overdraw_lowers s (a + 2) (Nat.le_add_left 2 a))

/-- Drawing at least two units at every step from `N` drains the condition step by step. -/
theorem drains {start : Nat} {draw : Nat → Nat} {N : Nat} (over : ∀ t, N ≤ t → 2 ≤ draw t) :
    ∀ k, levels start draw (N + k) ≤ levels start draw N - k
  | 0 => Nat.le_refl _
  | k + 1 => Nat.le_trans (overdraw_lowers _ _ (over (N + k) (Nat.le_add_right N k)))
      (Nat.pred_le_pred (drains over k))

/-- Drawing at least two units at every step from some step on consumes the condition. -/
theorem overdraw_consumes {start : Nat} {draw : Nat → Nat} {N : Nat}
    (over : ∀ t, N ≤ t → 2 ≤ draw t) :
    (conditions.dependence.along (drawing start draw)).Consumed () :=
  ⟨.sustaining, N + levels start draw N, trivial, fun t later =>
    match Nat.le.dest later with
    | ⟨m, sum⟩ =>
      have reached : N + (levels start draw N + (m + 1)) = t :=
        (Nat.add_assoc _ _ _).symm.trans ((Nat.succ_add _ m).symm.trans sum)
      Nat.lt_succ_of_le
        (Nat.le_trans (Nat.le_of_eq (congrArg (levels start draw) reached.symm))
          (Nat.le_trans (drains over _) (Nat.le_of_eq (sub_self_add _ _))))⟩

/-- Two units drawn at every step, from level two. -/
def depleting : Run process := drawing 2 fun _ => 2

/-- The same draws with the one at step `n` withheld. -/
def withheld (n : Nat) : Run process := drawing 2 fun t => if t = n then 0 else 2

/-- Depletion is the joint activity of a formation's events. The run consumes the
condition. The first event's step keeps the dependence, so it does not break for any
cycle. With any single event's draw withheld the condition is still consumed, so no
event alone makes the difference. -/
theorem depletion_is_joint :
    (conditions.dependence.along depleting).ConsumingIn .focal ∧
    (∀ p, 0 < p → ¬ (conditions.dependence.along depleting).BreakingFor p 0 .focal) ∧
    ∀ n, (conditions.dependence.along (withheld n)).Consumed () :=
  ⟨⟨0, (), trivial, overdraw_consumes (N := 0) fun _ _ => Nat.le_refl 2⟩,
   fun _ positive ⟨_, g, _, depends, _, unmet⟩ =>
     match g, depends with
     | .sustaining, _ => Nat.lt_irrefl 1 (unmet 1 Nat.zero_lt_one positive),
   fun n => overdraw_consumes (N := n + 1) fun _ later =>
     Nat.le_of_eq (if_neg (Nat.ne_of_gt later)).symm⟩

end Commons

end Becoming
