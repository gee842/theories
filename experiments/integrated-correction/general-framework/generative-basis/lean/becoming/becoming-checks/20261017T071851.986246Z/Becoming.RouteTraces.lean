import Becoming.FormedLoops

/-!
# Route traces: the orders of a sum over a process's histories

`Becoming.Routes` expands every sum over histories of `Becoming.Weighted` by order
(`Weights.within`): each step's weight split into a ground part and a response part, order `j`
reads the response part at most `j` times. Its laws are stated for weights on any configurations
and moves. `Becoming.Weighted` reads counting weights of a process's steps as its traces: the count
of courses is not zero exactly where a trace of the process exists (`counting_transfer_iff`). This
module states the orders' laws of the traces of a process, and the bounds of `Becoming.Loops`,
`Becoming.Frequency` and `Becoming.Routes` for the self-loop as standings of its world
(`FormedLoops.scheduleWorld`). No premise enters beyond what each theorem names.

* **Each order counts only courses the process has.** Where the counting weights of the ground and
  the response parts together are not zero exactly at the process's steps, with every move and
  configuration listed, an order of the sum over histories that is not zero has a trace of the
  process of as many moves to a configuration where the read amount is not zero
  (`within_trace`). Read as possibility, order by order, the same holds (`possibility_within_trace`):
  the possibility orders are the counting orders read through whether a count is zero.
* **The self-loop's world.** The world of the self-loop coupling at every step stands at the most
  the strengths can carry, `Loops.geomBound` (`selfLoopWorld_geomBound`), so its standing never
  falls (`selfLoopWorld_mono`), and at the full order of the sum over its histories
  (`selfLoopWorld_full_order`). The world of the self-loop coupling on any schedule stands at most
  where the one coupling at every step does (`scheduleWorld_le_always`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace RouteTraces

/-- A count at most another that is not zero leaves the other not zero. -/
theorem nonzero_of_le : ∀ {a b : Nat}, a ≤ b → nonzero a = true → nonzero b = true
  | 0, _, _, pos => Bool.noConfusion pos
  | _ + 1, 0, le, _ => absurd le (Nat.not_succ_le_zero _)
  | _ + 1, _ + 1, _, _ => rfl

section Orders

variable {S A : Type}

/-- **Each order counts only courses the process has.** Where the counting weights of the ground
and response parts together are not zero exactly at the steps of `P`, with every move and
configuration listed, an order of the sum over histories that is not zero at `s` after `n` steps
has a trace of `P` of `n` moves from `s` to a configuration where `f` is not zero. -/
theorem within_trace (P : Process S A) (ground response : S → A → S → Nat)
    (reads : ∀ s a t, nonzero (ground s a t + response s a t) = true ↔ P.step s a t)
    (moves : List A) (all : List S) (every_move : ∀ a, a ∈ moves) (every : ∀ s, s ∈ all)
    (f : S → Nat) (j n : Nat) (s : S)
    (pos : nonzero (counting.within ground response moves all f j n s) = true) :
    ∃ as t, as.length = n ∧ Trace P s as t ∧ nonzero (f t) = true :=
  (counting_transfer_iff P (fun s a t => ground s a t + response s a t) reads moves all every_move
      every f n s).mp
    (nonzero_of_le (counting_within_le_transfer ground response moves all f j n s) pos)

/-- **Read as possibility, each order holds only along courses the process has.** The possibility
order read off whether each count is zero holds at `s` after `n` steps only where `P` has a trace
of `n` moves from `s` to a configuration where `f` is not zero. -/
theorem possibility_within_trace (P : Process S A) (ground response : S → A → S → Nat)
    (reads : ∀ s a t, nonzero (ground s a t + response s a t) = true ↔ P.step s a t)
    (moves : List A) (all : List S) (every_move : ∀ a, a ∈ moves) (every : ∀ s, s ∈ all)
    (f : S → Nat) (j n : Nat) (s : S)
    (holds : possibility.within (fun s a t => nonzero (ground s a t))
      (fun s a t => nonzero (response s a t)) moves all (fun s => nonzero (f s)) j n s = true) :
    ∃ as t, as.length = n ∧ Trace P s as t ∧ nonzero (f t) = true :=
  within_trace P ground response reads moves all every_move every f j n s
    ((Weights.Hom.within support ground response moves all f j n s).trans holds)

end Orders

/-! ## The self-loop's world -/

/-- **The world of the self-loop coupling at every step stands at the most the strengths can
carry**: `D` multiplied by `1 + M` at each step. -/
theorem selfLoopWorld_geomBound (M D t : Nat) :
    (FormedLoops.scheduleWorld (fun _ => true) M D).web.level t (.inr ()) = Loops.geomBound M D t :=
  ((FormedLoops.scheduleWorld_course (fun _ => true) M D).2.1 t).trans
    ((congrArg (fun n => D * (1 + M) ^ n) (Frequency.count_always t)).trans
      (Loops.geomBound_eq M D t).symm)

/-- **The standing of the self-loop's world never falls.** -/
theorem selfLoopWorld_mono (M D : Nat) {s t : Nat} (le : s ≤ t) :
    (FormedLoops.scheduleWorld (fun _ => true) M D).web.level s (.inr ()) ≤
      (FormedLoops.scheduleWorld (fun _ => true) M D).web.level t (.inr ()) :=
  Nat.le_trans (Nat.le_of_eq (selfLoopWorld_geomBound M D s))
    (Nat.le_trans (Loops.geomBound_mono M D le) (Nat.le_of_eq (selfLoopWorld_geomBound M D t).symm))

/-- **The self-loop's world stands at the full order of the sum over its histories**: its starting
gap times the order `t` of `Becoming.Routes`' self-loop at horizon `t`. -/
theorem selfLoopWorld_full_order (M D t : Nat) :
    (FormedLoops.scheduleWorld (fun _ => true) M D).web.level t (.inr ()) = D * Loops.orderSum M t t :=
  ((FormedLoops.scheduleWorld_course (fun _ => true) M D).2.1 t).trans
    ((congrArg (fun n => D * (1 + M) ^ n) (Frequency.count_always t)).trans
      (congrArg (D * ·) (Routes.SelfLoop.within_exact M t).symm))

/-- **A self-loop coupling on any schedule stands at most where the one coupling at every step
does**: its world stands at most at `D * (1 + M) ^ t`, since a schedule marks at most every step. -/
theorem scheduleWorld_le_always (on : Nat → Bool) (M D t : Nat) :
    (FormedLoops.scheduleWorld on M D).web.level t (.inr ()) ≤ D * (1 + M) ^ t :=
  Nat.le_trans (Nat.le_of_eq ((FormedLoops.scheduleWorld_course on M D).2.1 t))
    (Nat.mul_le_mul_left D (Loops.pow_le_pow_exp (Nat.lt_of_lt_of_le Nat.one_pos
      (Nat.le_add_right 1 M)) (Frequency.count_le on t)))

end RouteTraces

end Becoming
