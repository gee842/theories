import Becoming.Countdown

/-!
# Countdown on the courses of a partial law's process

`Becoming.Countdown` states counted work and a reserved exit for a partial law, on its runs of
ticks and of plans (`ticks`, `Assurance.runPartial`). A partial law is a process of the spine
(`Assurance.ofPartial`), whose traces are exactly the courses its run completes
(`Assurance.trace_ofPartial_iff`), and `n` ticks are its run along `n` unit moves
(`Countdown.ticks_eq_runPartial`). `Becoming.Courses` states completion and the shorter courses on
that process; this module states the rest of `Becoming.Countdown` on its courses.

* **No shorter course finishes.** Where pending and finished exclude each other, no course of at
  most `work` unit moves of the tick's process from a pending configuration ends finished
  (`not_done_before_course`).
* **The bound of the reserved exit is attained.** In `Slow`, every course of the partial law's
  process longer than the margin from `some n` ends at the exit (`slow_exits`), while the course
  of exactly `n` moves ends at `some 0`, not at the exit (`slow_misses`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative Assurance

universe u

namespace CountdownCourses

/-- **No shorter course finishes.** Where pending and finished exclude each other, every course of
at most `work` unit moves of the tick's process from a pending configuration ends at a
configuration that is not finished. -/
theorem not_done_before_course {S : Type u} {tick : S → Option S} {busy done : S → Prop}
    {work fuel : S → Nat} (counts : Countdown.CountedWork tick busy done work fuel)
    (apart : ∀ s, busy s → done s → False) {s t : S} {k : Nat} (pending : busy s)
    (within : k ≤ work s)
    (path : Trace (ofPartial fun s (_ : Unit) => tick s) s (List.replicate k ()) t) : ¬ done t :=
  Countdown.not_done_before counts apart pending within
    ((Countdown.ticks_eq_runPartial tick k s).trans ((trace_ofPartial_iff _).mp path))

/-- **Every course longer than the margin ends at the exit.** In `Slow`, every course of the
partial law's process from `some n` with more than `n` moves ends at the exit `none`. -/
theorem slow_exits {n : Nat} {plan : List Unit} (long : n < plan.length) {t : Option Nat}
    (path : Trace (ofPartial Countdown.Slow.step) (some n) plan t) : t = none :=
  match Countdown.exits Countdown.Slow.reserved plan (some n) trivial (fun _ _ => trivial) long with
  | ⟨_, ran, _, out⟩ =>
    (Option.some.inj (((trace_ofPartial_iff _).mp path).symm.trans ran)).trans out

/-- **The bound is attained on a course.** In `Slow`, the course of the partial law's process of
exactly `n` moves from `some n` ends at `some 0`, which is not the exit. -/
theorem slow_misses (n : Nat) :
    Trace (ofPartial Countdown.Slow.step) (some n) (List.replicate n ()) (some 0) :=
  (trace_ofPartial_iff _).mpr (Countdown.Slow.misses n)

end CountdownCourses

end Becoming
