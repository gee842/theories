import Becoming.Joint
import Becoming.Recurrence

/-!
# Experiment: what varying one's own act tests, and what it needs

`Becoming.Testing` leaves one question open: what an act does compares two histories, the one
with the act and the one without it, and one unfolding has only one of them. This module
states, with no premise, when the unfolding itself compares them. A configuration is what an
unfolding is at a step and a move is what is done there, as in `Becoming.Joint`; the move
determines the step where `Joint.Determined` holds. Nothing is assumed of the process beyond
what each theorem states.

* **What the record fixes.** Along a run, relative to determinacy, the record fixes what a
  move does at a configuration where the run takes that move there (`Run.fixes_of_takes`),
  and fixes nothing where it does not, even with every configuration registered: a determined
  process sending the untaken move anywhere at all has the same run (`retarget`,
  `Run.not_fixes_of_untaken`). So what one's own act would have done otherwise is fixed only
  where the configuration returns and the move differs there
  (`Run.other_move_fixed_of_return`); a run that never returns fixes no move other than the
  one it takes at each configuration it passes (`Run.not_fixes_other_of_new`).
* **A kept history never returns.** A configuration that keeps the history of configurations
  and moves (`keepHistory`, the counterpart with moves of `Law.withHistory`) is new at every
  step (`keepHistory_new`). So a formation that keeps everything it has passed through, and
  counts it as part of what it is, fixes nothing about its own acts but what it did
  (`keepHistory_fixes_nothing_else`).
* **Experiment needs a model of what is irrelevant.** Read through a projection `π` of the
  configuration, the record fixes, relative to every determined process admitting its steps so
  read, what a move does at a projected configuration it takes (`Run.fixesThrough_of_takes`).
  Where the process's step factors through `π` into such a process, one occasion then stands
  for every configuration with that projection, observed or not (`Run.generalizes`). Within
  finitely many projected configurations a run's projection returns from every step on
  (`Run.projection_returns`, an instance of `revisits_from`). The projection is a model.
  Where the step does not factor through it, the record fixes a difference between two moves
  that make no difference anywhere (`Confound.misattributes`). Moving in step with what the
  projection leaves out, the wrong model is admitted at every step and never refuted
  (`Confound.confounded`); varying the move against it, a later step refutes the model, since
  no determined process admits the steps so read (`Confound.varied_refutes`).

**Readings (the AI's, adopted on Ren's delegation of 15 October 2026, DELEGATED-CHOICES D25).** An
experiment is varying one's own act where the
configuration, read as the experimenter reads it, returns. Replication is that return. A
control is the claim that what differs between the occasions is irrelevant: the model that
the step factors through the reading. Varying the act independently of what the reading
leaves out is what can refute a wrong control; acts in step with it never refute it. With the
registration of `Becoming.Testing` as the reading, an experiment through what registers is
right where the unfolding factors through what registers; threshold and reach blindness are
cases where it does not.

What is not derived: that a formation varies its acts, keeps or forgets its history, or forms a
projection; which projection the actual unfolding factors through; and that what is fixed is
registered by anything other than the full configuration or its projection. No ethical
predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w

variable {S : Type u} {A : Type v}

/-! ## What the record fixes -/

namespace Run

variable {P : Process S A}

/-- Before step `t` the run takes move `a` at configuration `s`. -/
def Takes (r : Run P) (t : Nat) (s : S) (a : A) : Prop :=
  ∃ n, n < t ∧ r.state n = s ∧ r.act n = a

/-- Process `Q` admits every step of the run before step `t`. -/
def StepsOf (r : Run P) (Q : Process S A) (t : Nat) : Prop :=
  ∀ n, n < t → Q.step (r.state n) (r.act n) (r.state (n + 1))

/-- Relative to determinacy, the record up to step `t` fixes the outcome of `a` at `s` to
`u`: every determined process admitting each step of the run before `t` sends `a` at `s` to
`u`, wherever it sends it. -/
def Fixes (r : Run P) (t : Nat) (s : S) (a : A) (u : S) : Prop :=
  ∀ Q : Process S A, Determined Q → r.StepsOf Q t → ∀ u', Q.step s a u' → u' = u

/-- **A move taken is fixed.** Once the run has taken `a` at `s`, every determined process
admitting its steps sends `a` at `s` where the run went. -/
theorem fixes_of_takes (r : Run P) {n t : Nat} (before : n < t) :
    r.Fixes t (r.state n) (r.act n) (r.state (n + 1)) :=
  fun _ determined steps _ step => determined _ _ _ _ step (steps n before)

end Run

/-- `P` with move `b` at `s` sent to `u₀`, and every other step as in `P`. -/
def retarget (P : Process S A) (s : S) (b : A) (u₀ : S) : Process S A :=
  ⟨fun s' a u => (¬ (s' = s ∧ a = b) ∧ P.step s' a u) ∨ (s' = s ∧ a = b ∧ u = u₀)⟩

/-- Retargeting a determined process leaves it determined. -/
theorem retarget_determined {P : Process S A} (determined : Determined P) (s : S) (b : A)
    (u₀ : S) : Determined (retarget P s b u₀)
  | _, _, _, _, .inl ⟨_, step⟩, .inl ⟨_, step'⟩ => determined _ _ _ _ step step'
  | _, _, _, _, .inl ⟨other, _⟩, .inr ⟨same, same', _⟩ => absurd ⟨same, same'⟩ other
  | _, _, _, _, .inr ⟨same, same', _⟩, .inl ⟨other, _⟩ => absurd ⟨same, same'⟩ other
  | _, _, _, _, .inr ⟨_, _, to⟩, .inr ⟨_, _, to'⟩ => to.trans to'.symm

/-- The retargeted process sends `b` at `s` to `u₀`. -/
theorem retarget_step (P : Process S A) (s : S) (b : A) (u₀ : S) :
    (retarget P s b u₀).step s b u₀ :=
  .inr ⟨rfl, rfl, rfl⟩

namespace Run

variable {P : Process S A}

/-- A run that has not taken `b` at `s` before `t` has every step before `t` admitted by every
retargeting there. -/
theorem stepsOf_retarget (r : Run P) {t : Nat} {s : S} {b : A} (untaken : ¬ r.Takes t s b)
    (u₀ : S) : r.StepsOf (retarget P s b u₀) t :=
  fun n before => .inl ⟨fun ⟨same, same'⟩ => untaken ⟨n, before, same, same'⟩, r.step n⟩

/-- **A move not taken is not fixed.** Where the run has not taken `b` at `s` before `t`, and
the process is determined, the record up to `t` fixes no outcome of `b` at `s`, whatever
registers: determined processes admitting every step of the run send it to any two
configurations. -/
theorem not_fixes_of_untaken (determined : Determined P) (r : Run P) {t : Nat} {s : S} {b : A}
    (untaken : ¬ r.Takes t s b) {x y : S} (two : x ≠ y) : ¬ ∃ u, r.Fixes t s b u :=
  fun ⟨_, fixes⟩ => two
    ((fixes _ (retarget_determined determined s b x) (r.stepsOf_retarget untaken x) x
        (retarget_step P s b x)).trans
      (fixes _ (retarget_determined determined s b y) (r.stepsOf_retarget untaken y) y
        (retarget_step P s b y)).symm)

/-- **What one's act would have done otherwise is fixed where the configuration returns.**
Where the run comes back at step `m` to the configuration of step `n` and takes a move
there, that move's outcome at the configuration of step `n` is fixed from step `m + 1` on. -/
theorem fixes_on_return (r : Run P) {n m t : Nat} (back : r.state m = r.state n)
    (before : m < t) : r.Fixes t (r.state n) (r.act m) (r.state (m + 1)) :=
  back ▸ r.fixes_of_takes before

/-- Two different steps are ordered one way or the other. -/
theorem ordered_of_ne {i j : Nat} (ne : i ≠ j) : i < j ∨ j < i :=
  match Nat.lt_or_ge i j with
  | .inl lt => .inl lt
  | .inr ge => .inr (Nat.lt_of_le_of_ne ge fun same => ne same.symm)

/-- **A run that never returns fixes no other move.** Where no configuration comes back, at
each configuration the run passes, the record fixes the outcome of no move other than the one
the run takes there. -/
theorem not_fixes_other_of_new (determined : Determined P) (r : Run P)
    (new : ∀ i j, i < j → r.state i ≠ r.state j) {n t : Nat} {b : A} (other : b ≠ r.act n)
    {x y : S} (two : x ≠ y) : ¬ ∃ u, r.Fixes t (r.state n) b u :=
  r.not_fixes_of_untaken determined (fun ⟨m, _, same, takes⟩ =>
    have distinct : m ≠ n := fun same' => other (takes.symm.trans (congrArg r.act same'))
    match ordered_of_ne distinct with
    | .inl lt => new m n lt same
    | .inr gt => new n m gt same.symm) two

end Run

/-! ## A kept history never returns -/

variable {K : Type w}

/-- The configuration with the history of configurations and moves it has passed through:
each step goes on by `P` and passes the configuration and the move into the past. -/
def keepHistory (P : Process S A) : Process (S × List (S × A)) A :=
  ⟨fun h a h' => P.step h.1 a h'.1 ∧ h'.2 = (h.1, a) :: h.2⟩

/-- Along a run keeping its history, the past grows by one at each step. -/
theorem keepHistory_length {P : Process S A} (r : Run (keepHistory P)) :
    ∀ n, (r.state n).2.length = (r.state 0).2.length + n
  | 0 => rfl
  | n + 1 => (congrArg List.length (r.step n).2).trans
      (congrArg Nat.succ (keepHistory_length r n))

/-- **A kept history is new at every step.** -/
theorem keepHistory_new {P : Process S A} (r : Run (keepHistory P)) :
    ∀ i j, i < j → r.state i ≠ r.state j :=
  fun i j lt same =>
    Nat.ne_of_lt (Nat.add_lt_add_left lt (r.state 0).2.length)
      (((keepHistory_length r i).symm.trans (congrArg (fun h => h.2.length) same)).trans
        (keepHistory_length r j))

/-- Keeping its history keeps a process determined. -/
theorem keepHistory_determined {P : Process S A} (determined : Determined P) :
    Determined (keepHistory P)
  | _, _, (_, _), (_, _), ⟨step, past⟩, ⟨step', past'⟩ =>
    congr (congrArg Prod.mk (determined _ _ _ _ step step')) (past.trans past'.symm)

/-- **Keeping everything, nothing about one's own acts is fixed but what one did.** A run
keeping its history fixes, at each configuration, the outcome of no move other than the one
it takes there. -/
theorem keepHistory_fixes_nothing_else {P : Process S A} (determined : Determined P)
    (r : Run (keepHistory P)) {n t : Nat} {b : A} (other : b ≠ r.act n)
    {x y : S × List (S × A)} (two : x ≠ y) : ¬ ∃ u, r.Fixes t (r.state n) b u :=
  r.not_fixes_other_of_new (keepHistory_determined determined) (keepHistory_new r) other two

/-! ## Experiment through a projection -/

namespace Run

variable {P : Process S A}

/-- `Q` admits every step of the run before `t`, read through `π`. -/
def StepsThrough (r : Run P) (π : S → K) (Q : Process K A) (t : Nat) : Prop :=
  ∀ n, n < t → Q.step (π (r.state n)) (r.act n) (π (r.state (n + 1)))

/-- Read through `π`, the record up to `t` fixes the outcome of `a` at `k` to `κ`: every
determined process admitting the run's steps before `t` so read sends `a` at `k` to `κ`,
wherever it sends it. -/
def FixesThrough (r : Run P) (π : S → K) (t : Nat) (k : K) (a : A) (κ : K) :
    Prop :=
  ∀ Q : Process K A, Determined Q → r.StepsThrough π Q t → ∀ κ', Q.step k a κ' → κ' = κ

/-- **An experiment through a projection.** Once the run has taken `a` at a configuration
projecting to `k`, the outcome of `a` at `k`, read through `π`, is fixed. -/
theorem fixesThrough_of_takes (r : Run P) (π : S → K) {n t : Nat} (before : n < t) :
    r.FixesThrough π t (π (r.state n)) (r.act n) (π (r.state (n + 1))) :=
  fun _ determined steps _ step => determined _ _ _ _ step (steps n before)

end Run

/-- The step of `P` factors through `π` into `Q`: every step of `P`, read through `π`, is a
step of `Q`. A model of what in the configuration is irrelevant to its change. -/
def FactorsThrough (P : Process S A) (π : S → K) (Q : Process K A) : Prop :=
  ∀ s a u, P.step s a u → Q.step (π s) a (π u)

namespace Run

variable {P : Process S A}

/-- Where `P` factors through `π` into `Q`, `Q` admits every step of every run read through
`π`. -/
theorem stepsThrough_of_factors (r : Run P) {π : S → K} {Q : Process K A}
    (factors : FactorsThrough P π Q) (t : Nat) : r.StepsThrough π Q t :=
  fun n _ => factors _ _ _ (r.step n)

/-- **One occasion stands for every configuration in its class.** Where the step of `P`
factors through `π` into a determined process, an outcome the record fixes for `a` at `k` is
the outcome, read through `π`, of `a` at every configuration projecting to `k`, whether or
not the run has passed through it. -/
theorem generalizes (r : Run P) {π : S → K} {Q : Process K A} (determined : Determined Q)
    (factors : FactorsThrough P π Q) {t : Nat} {k : K} {a : A} {κ : K}
    (fixes : r.FixesThrough π t k a κ) {s u : S} (at_k : π s = k) (step : P.step s a u) :
    π u = κ :=
  fixes Q determined (r.stepsThrough_of_factors factors t) (π u) (at_k ▸ factors _ _ _ step)

/-- **Within finitely many projected configurations, the projection returns.** Where a list
holds every projected configuration of the run, from every step on two steps have the same
projection: an instance of `revisits_from`. -/
theorem projection_returns (r : Run P) {π : S → K} {l : List K}
    (held : ∀ n, π (r.state n) ∈ l) (T : Nat) :
    ∃ i j, T ≤ i ∧ i < j ∧ π (r.state i) = π (r.state j) :=
  Becoming.revisits_from held T

end Run

/-! ## A wrong projection

The configuration is a hidden bit and an outcome. Each step flips the hidden bit and sets the
outcome to the hidden bit before the step, whatever the move: the move makes no difference
anywhere. The projection reads the outcome only. -/

namespace Confound

/-- Two moves. -/
inductive Move where
  | left
  | right

open Move

/-- Flip the hidden bit; the outcome becomes the hidden bit. -/
def next (s : Bool × Bool) : Bool × Bool := (!s.1, s.1)

/-- The move does nothing. -/
def process : Process (Bool × Bool) Move := ⟨fun s _ u => u = next s⟩

/-- The configurations from hidden bit and outcome both false. -/
def states : Nat → Bool × Bool := Law.orbit next (false, false)

/-- The outcome read alone. -/
def outcome : Bool × Bool → Bool := fun s => s.2

theorem determined : Determined process :=
  fun _ _ _ _ step step' => step.trans step'.symm

/-- The move makes no difference anywhere. -/
theorem move_idle (s : Bool × Bool) (a b : Move) (u : Bool × Bool) :
    process.step s a u ↔ process.step s b u :=
  Iff.rfl

theorem not_not (b : Bool) : (!!b) = b :=
  match b with
  | true => rfl
  | false => rfl

/-- The hidden bit comes back every two steps. -/
theorem hidden_two (n : Nat) : (states (n + 2)).1 = (states n).1 :=
  not_not (states n).1

/-- Moving in step with the hidden bit: left, right, left, right, … -/
def aligned : Nat → Move
  | 0 => left
  | 1 => right
  | n + 2 => aligned n

/-- Moving left except at the second step. -/
def varied : Nat → Move
  | 1 => right
  | _ => left

/-- The run of the process under a sequence of moves. -/
def run (moves : Nat → Move) : Run process :=
  ⟨states, moves, fun _ => rfl⟩

/-- The aligned move is left exactly where the hidden bit is false. -/
theorem aligned_with_hidden : ∀ n,
    (aligned n = left ∧ (states n).1 = false) ∨ (aligned n = right ∧ (states n).1 = true)
  | 0 => .inl ⟨rfl, rfl⟩
  | 1 => .inr ⟨rfl, rfl⟩
  | n + 2 => match aligned_with_hidden n with
    | .inl ⟨move, hidden⟩ => .inl ⟨move, (hidden_two n).trans hidden⟩
    | .inr ⟨move, hidden⟩ => .inr ⟨move, (hidden_two n).trans hidden⟩

/-- The model in which the move decides the outcome: left gives false, right gives true. -/
def moveDecides : Process Bool Move :=
  ⟨fun _ a κ => (a = left ∧ κ = false) ∨ (a = right ∧ κ = true)⟩

theorem moveDecides_determined : Determined moveDecides
  | _, _, _, _, .inl ⟨_, to⟩, .inl ⟨_, to'⟩ => to.trans to'.symm
  | _, _, _, _, .inr ⟨_, to⟩, .inr ⟨_, to'⟩ => to.trans to'.symm
  | _, _, _, _, .inl ⟨move, _⟩, .inr ⟨move', _⟩ => Move.noConfusion (move.symm.trans move')
  | _, _, _, _, .inr ⟨move, _⟩, .inl ⟨move', _⟩ => Move.noConfusion (move.symm.trans move')

/-- **A wrong projection misattributes.** Read through the outcome, the record up to the
second step fixes left at false to false and right at false to true: a difference between two
moves that make no difference anywhere. It holds of both runs. -/
theorem misattributes (moves : Nat → Move) (first : moves 0 = left) (second : moves 1 = right)
    {t : Nat} (two : 2 ≤ t) :
    (∀ s a b u, process.step s a u ↔ process.step s b u) ∧
      (run moves).FixesThrough outcome t false left false ∧
      (run moves).FixesThrough outcome t false right true :=
  ⟨move_idle,
   first ▸ (run moves).fixesThrough_of_takes outcome (n := 0)
     (Nat.lt_of_lt_of_le (by decide) two),
   second ▸ (run moves).fixesThrough_of_takes outcome (n := 1)
     (Nat.lt_of_lt_of_le (by decide) two)⟩

/-- **A confound is never refuted.** Moving in step with the hidden bit, every step read
through the outcome is admitted by the determined model in which the move decides the
outcome, at every step: the record never refutes the wrong projection. -/
theorem confounded : ∀ t, (run aligned).StepsThrough outcome moveDecides t :=
  fun _ n _ => match aligned_with_hidden n with
    | .inl ⟨move, hidden⟩ => .inl ⟨move, hidden⟩
    | .inr ⟨move, hidden⟩ => .inr ⟨move, hidden⟩

/-- **Varying the move against the hidden bit refutes the projection.** Moving left again at
the fourth step, where the hidden bit differs from the first, no determined process admits
the steps up to the fifth read through the outcome. -/
theorem varied_refutes :
    ¬ ∃ Q : Process Bool Move, Determined Q ∧ (run varied).StepsThrough outcome Q 4 :=
  fun ⟨_, determined, steps⟩ =>
    Bool.noConfusion (determined _ _ _ _ (steps 0 (by decide)) (steps 3 (by decide)))

end Confound

end Becoming
