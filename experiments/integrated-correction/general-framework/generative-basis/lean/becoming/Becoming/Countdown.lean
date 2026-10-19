import Becoming.Assurance

/-!
# Countdown: counted work, kept properties of admitted courses, and a reserved exit

Protocols that carry pending work through interruptions share three local structures. This
module states each as a law for every process or partial law of its kind.

* **Kept along admitted courses.** A property holds at the end of every course from every start
  where it holds exactly when every step keeps it (`invariant_iff_reach`). Read on the steps a
  partial law takes where a move is admitted (`admitted`), interruptions and ordinary moves are
  steps alike, so a protocol's history keeps its invariant exactly when each kind of step does.
* **Counted work (`CountedWork`).** A partial law `tick` that, while a task is pending (`busy`),
  does one unit of remaining work for one unit of fuel, finishes into `done` when no work remains
  and fuel is left, and stalls without fuel. From every pending configuration, `work + 1` ticks
  finish the task exactly when the fuel covers them (`completes_iff`); every shorter run leaves the
  task pending with the work and fuel each lowered by the ticks taken (`pending_before`,
  `ticks_busy`), so where pending and finished are exclusive no shorter run finishes
  (`not_done_before`), and with fuel short of the work every run stalls
  (`stalls_beyond`). Read as a plan of the partial law, this is completion in the sense of
  `Assurance` (`completes_plan_iff`). With no fuel, a task advancing by one unit per tick
  finishes in exactly `work + 1` ticks (`Advances.completes`).
* **A reserved exit (`Reserved`).** A partial law whose every admitted move from a valid
  configuration goes on, stays valid, and either takes the exit or lowers a margin by one, while
  the exit is kept by every move. From a valid configuration every admitted course runs and stays
  valid (`runs_valid`), and every admitted course longer than the margin ends at the exit
  (`exits`). The bound is attained: a course as long as the margin can miss the exit
  (`Slow.misses`).

These are local conditions on single steps, and every law follows from them alone. Which
configurations count as pending, what the fuel and the margin represent, and whether the
protocol's steps are atomic are supplied with each application. No premise is added; every
declaration has an empty axiom report.
-/

namespace Becoming

open Generative Generative.InquirySufficiency Becoming.Assurance

universe u v

namespace Countdown

variable {S : Type u} {A : Type v}

/-! ## Kept along admitted courses -/

/-- **A property holds at the end of every course from every start where it holds exactly when
every step keeps it.** -/
theorem invariant_iff_reach {P : Process S A} {I : S → Prop} :
    Invariant P I ↔ ∀ s t, Reach P s t → I s → I t :=
  ⟨fun inv _ _ reach => inv.reach reach,
   fun along s _ t step => along s t (Reach.of_step step)⟩

/-- The steps a partial law takes where a move is admitted. -/
def admitted (f : S → A → Option S) (allow : S → A → Prop) : Process S A :=
  ⟨fun s a t => allow s a ∧ f s a = some t⟩

/-- **An admitted course keeps a property from every start where it holds exactly when every
admitted step keeps it.** -/
theorem admitted_invariant_iff {f : S → A → Option S} {allow : S → A → Prop} {I : S → Prop} :
    (∀ s a t, allow s a → f s a = some t → I s → I t) ↔
      ∀ s t, Reach (admitted f allow) s t → I s → I t :=
  ⟨fun kept => invariant_iff_reach.mp fun s a t ⟨admits, moved⟩ => kept s a t admits moved,
   fun along s _ t admits moved => along s t (Reach.of_step ⟨admits, moved⟩)⟩

/-! ## Counted work -/

/-- Running a partial step `n` times. -/
def ticks (tick : S → Option S) : Nat → S → Option S
  | 0, s => some s
  | n + 1, s => (tick s).bind (ticks tick n)

/-- The last tick of a run. -/
theorem ticks_succ (tick : S → Option S) :
    ∀ (n : Nat) (s : S), ticks tick (n + 1) s = (ticks tick n s).bind tick
  | 0, s => by
    show (tick s).bind some = tick s
    cases tick s with
    | none => rfl
    | some _ => rfl
  | n + 1, s => by
    show (tick s).bind (ticks tick (n + 1)) = ((tick s).bind (ticks tick n)).bind tick
    cases tick s with
    | none => rfl
    | some t => exact ticks_succ tick n t

/-- `n` ticks are the run of the partial law along `n` unit moves. -/
theorem ticks_eq_runPartial (tick : S → Option S) :
    ∀ (n : Nat) (s : S), ticks tick n s = runPartial (fun s (_ : Unit) => tick s) s (List.replicate n ())
  | 0, _ => rfl
  | n + 1, s => by
    show (tick s).bind (ticks tick n) =
      (tick s).bind fun t => runPartial (fun s (_ : Unit) => tick s) t (List.replicate n ())
    cases tick s with
    | none => rfl
    | some t => exact ticks_eq_runPartial tick n t

/-- **Counted work**: while pending, one tick does one unit of work for one unit of fuel; with
no work left and fuel left, a tick finishes; without fuel, a tick stalls. -/
structure CountedWork (tick : S → Option S) (busy done : S → Prop) (work fuel : S → Nat) : Prop where
  advance : ∀ s, busy s → 0 < fuel s → 0 < work s →
    ∃ t, tick s = some t ∧ busy t ∧ work t + 1 = work s ∧ fuel t + 1 = fuel s
  finish : ∀ s, busy s → 0 < fuel s → work s = 0 → ∃ t, tick s = some t ∧ done t
  stall : ∀ s, busy s → fuel s = 0 → tick s = none

theorem eq_zero_of_add_eq {n : Nat} : ∀ k, n + k = k → n = 0
  | 0, same => same
  | k + 1, same => eq_zero_of_add_eq k (Nat.succ.inj same)

theorem pos_of_add_eq {f : Nat} : ∀ {w F : Nat}, f + w = F → w + 1 ≤ F → 0 < f
  | 0, _, same, le => Nat.le_trans le (Nat.le_of_eq same.symm)
  | w + 1, _, same, le =>
    pos_of_add_eq (F := f + w) rfl (Nat.le_of_succ_le_succ (Nat.le_trans le (Nat.le_of_eq same.symm)))

/-- **Within the work and the fuel, every run of ticks leaves the task pending**, with the work
and the fuel each lowered by the number of ticks. -/
theorem ticks_busy {tick : S → Option S} {busy done : S → Prop} {work fuel : S → Nat}
    (counts : CountedWork tick busy done work fuel) :
    ∀ (k : Nat) (s : S), busy s → k ≤ work s → k ≤ fuel s →
      ∃ t, ticks tick k s = some t ∧ busy t ∧ work t + k = work s ∧ fuel t + k = fuel s
  | 0, s, pending, _, _ => ⟨s, rfl, pending, rfl, rfl⟩
  | k + 1, s, pending, worked, fueled =>
    match counts.advance s pending (Nat.lt_of_lt_of_le (Nat.succ_pos k) fueled)
        (Nat.lt_of_lt_of_le (Nat.succ_pos k) worked) with
    | ⟨t, moved, pending', lowered, spent⟩ =>
      match ticks_busy counts k t pending'
          (Nat.le_of_succ_le_succ (Nat.le_trans worked (Nat.le_of_eq lowered.symm)))
          (Nat.le_of_succ_le_succ (Nat.le_trans fueled (Nat.le_of_eq spent.symm))) with
      | ⟨u, ran, pendingU, workU, fuelU⟩ =>
        ⟨u, by
          show (tick s).bind (ticks tick k) = some u
          rw [moved]
          exact ran,
         pendingU, (congrArg Nat.succ workU).trans lowered,
         (congrArg Nat.succ fuelU).trans spent⟩

/-- **With fuel short of the work, every run longer than the fuel stalls.** -/
theorem stalls_beyond {tick : S → Option S} {busy done : S → Prop} {work fuel : S → Nat}
    (counts : CountedWork tick busy done work fuel) :
    ∀ (n : Nat) (s : S), busy s → fuel s ≤ work s → fuel s < n → ticks tick n s = none
  | 0, _, _, _, beyond => absurd beyond (Nat.not_lt_zero _)
  | n + 1, s, pending, short, beyond => by
    show (tick s).bind (ticks tick n) = none
    cases fueled : fuel s with
    | zero =>
      rw [counts.stall s pending fueled]
      rfl
    | succ f =>
      have positive : 0 < fuel s := fueled ▸ Nat.succ_pos f
      match counts.advance s pending positive (Nat.lt_of_lt_of_le positive short) with
      | ⟨t, moved, pending', lowered, spent⟩ =>
        rw [moved]
        have shortT : fuel t + 1 ≤ work t + 1 := by
          rw [spent, lowered]
          exact short
        have beyondT : fuel t + 1 < n + 1 := by
          rw [spent]
          exact beyond
        exact stalls_beyond counts n t pending'
          (Nat.le_of_succ_le_succ shortT) (Nat.lt_of_succ_lt_succ beyondT)

/-- **Counted work finishes in `work + 1` ticks exactly when the fuel covers them.** -/
theorem completes_iff {tick : S → Option S} {busy done : S → Prop} {work fuel : S → Nat}
    (counts : CountedWork tick busy done work fuel) {s : S} (pending : busy s) :
    (∃ t, ticks tick (work s + 1) s = some t ∧ done t) ↔ work s + 1 ≤ fuel s :=
  ⟨fun ⟨t, ran, _⟩ =>
    match Nat.lt_or_ge (work s) (fuel s) with
    | .inl covered => covered
    | .inr short =>
      absurd ((stalls_beyond counts (work s + 1) s pending short
        (Nat.lt_succ_of_le short)).symm.trans ran) ListTests.none_ne_some,
   fun covered =>
    match ticks_busy counts (work s) s pending (Nat.le_refl _)
        (Nat.le_of_succ_le covered) with
    | ⟨t, ran, pending', workT, fuelT⟩ =>
      match counts.finish t pending' (pos_of_add_eq fuelT covered)
          (eq_zero_of_add_eq (work s) workT) with
      | ⟨u, moved, finished⟩ =>
        ⟨u, by
          rw [ticks_succ, ran]
          exact moved,
         finished⟩⟩

/-- **Every shorter run leaves the task pending**: every run of at most `work` ticks leaves the task pending,
with the work lowered by the ticks taken. -/
theorem pending_before {tick : S → Option S} {busy done : S → Prop} {work fuel : S → Nat}
    (counts : CountedWork tick busy done work fuel) {s t : S} {k : Nat} (pending : busy s)
    (within : k ≤ work s) (ran : ticks tick k s = some t) : busy t ∧ work t + k = work s :=
  match Nat.lt_or_ge (fuel s) k with
  | .inl beyond =>
    absurd ((stalls_beyond counts k s pending
      (Nat.le_trans (Nat.le_of_lt beyond) within) beyond).symm.trans ran) ListTests.none_ne_some
  | .inr fueled =>
    match ticks_busy counts k s pending within fueled with
    | ⟨u, ran', pendingU, workU, _⟩ =>
      have same : u = t := Option.some.inj (ran'.symm.trans ran)
      same ▸ ⟨pendingU, workU⟩

/-- Where pending and finished exclude each other, the task finishes at no earlier tick. -/
theorem not_done_before {tick : S → Option S} {busy done : S → Prop} {work fuel : S → Nat}
    (counts : CountedWork tick busy done work fuel) (apart : ∀ s, busy s → done s → False)
    {s t : S} {k : Nat} (pending : busy s) (within : k ≤ work s)
    (ran : ticks tick k s = some t) : ¬ done t :=
  fun finished => apart t (pending_before counts pending within ran).1 finished

/-- **As a plan of the partial law, counted work completes exactly when the fuel covers it**
(`Assurance.Completes` with no safety condition). -/
theorem completes_plan_iff {tick : S → Option S} {busy done : S → Prop} {work fuel : S → Nat}
    (counts : CountedWork tick busy done work fuel) {s : S} (pending : busy s) :
    Completes (ofPartial fun s (_ : Unit) => tick s) free done s (List.replicate (work s + 1) ()) ↔
      work s + 1 ≤ fuel s :=
  (completes_ofPartial_iff _).trans
    ((⟨fun ⟨t, ran, finished⟩ => ⟨t, (ticks_eq_runPartial tick _ s).trans ran, finished⟩,
       fun ⟨t, ran, finished⟩ => ⟨t, (ticks_eq_runPartial tick _ s).symm.trans ran, finished⟩⟩ :
        (∃ t, runPartial (fun s (_ : Unit) => tick s) s (List.replicate (work s + 1) ()) = some t ∧
            done t) ↔ ∃ t, ticks tick (work s + 1) s = some t ∧ done t).trans
      (completes_iff counts pending))

/-- **Work advancing by one unit per tick**, with no fuel. -/
structure Advances (tick : S → Option S) (busy done : S → Prop) (work : S → Nat) : Prop where
  advance : ∀ s, busy s → 0 < work s → ∃ t, tick s = some t ∧ busy t ∧ work t + 1 = work s
  finish : ∀ s, busy s → work s = 0 → ∃ t, tick s = some t ∧ done t

/-- Unfuelled work is counted work whose fuel is one more than the work. -/
theorem Advances.countedWork {tick : S → Option S} {busy done : S → Prop} {work : S → Nat}
    (advances : Advances tick busy done work) :
    CountedWork tick busy done work (fun s => work s + 1) :=
  ⟨fun s pending _ positive =>
    match advances.advance s pending positive with
    | ⟨t, moved, pending', lowered⟩ => ⟨t, moved, pending', lowered, congrArg Nat.succ lowered⟩,
   fun s pending _ finished => advances.finish s pending finished,
   fun _ _ empty => Nat.noConfusion empty⟩

/-- **Unfuelled work finishes in exactly `work + 1` ticks.** -/
theorem Advances.completes {tick : S → Option S} {busy done : S → Prop} {work : S → Nat}
    (advances : Advances tick busy done work) {s : S} (pending : busy s) :
    ∃ t, ticks tick (work s + 1) s = some t ∧ done t :=
  (completes_iff advances.countedWork pending).mpr (Nat.le_refl _)

/-! ## A reserved exit -/

/-- **A reserved exit**: every admitted move from a valid configuration goes on, stays valid,
and either takes the exit or lowers the margin by one; every move from the exit stays there. -/
structure Reserved (f : S → A → Option S) (adm : A → Prop) (valid exit : S → Prop)
    (margin : S → Nat) : Prop where
  moves : ∀ s a, valid s → adm a →
    ∃ t, f s a = some t ∧ valid t ∧ (exit t ∨ margin t + 1 = margin s)
  kept : ∀ s a t, exit s → f s a = some t → exit t

/-- **From a valid configuration every admitted course runs and stays valid.** -/
theorem runs_valid {f : S → A → Option S} {adm : A → Prop} {valid exit : S → Prop}
    {margin : S → Nat} (reserved : Reserved f adm valid exit margin) :
    ∀ (plan : List A) (s : S), valid s → (∀ a, a ∈ plan → adm a) →
      ∃ t, runPartial f s plan = some t ∧ valid t
  | [], s, held, _ => ⟨s, rfl, held⟩
  | a :: rest, s, held, admissible =>
    match reserved.moves s a held (admissible a (.head _)) with
    | ⟨t, moved, held', _⟩ =>
      match runs_valid reserved rest t held' fun b mem => admissible b (.tail _ mem) with
      | ⟨u, ran, heldU⟩ => ⟨u, by
          show (f s a).bind (fun t => runPartial f t rest) = some u
          rw [moved]
          exact ran, heldU⟩

/-- From a valid configuration at the exit, every admitted course stays at the exit. -/
theorem stays_exit {f : S → A → Option S} {adm : A → Prop} {valid exit : S → Prop}
    {margin : S → Nat} (reserved : Reserved f adm valid exit margin) :
    ∀ (plan : List A) (s : S), valid s → exit s → (∀ a, a ∈ plan → adm a) →
      ∃ t, runPartial f s plan = some t ∧ valid t ∧ exit t
  | [], s, held, out, _ => ⟨s, rfl, held, out⟩
  | a :: rest, s, held, out, admissible =>
    match reserved.moves s a held (admissible a (.head _)) with
    | ⟨t, moved, held', _⟩ =>
      match stays_exit reserved rest t held' (reserved.kept s a t out moved)
          fun b mem => admissible b (.tail _ mem) with
      | ⟨u, ran, heldU, outU⟩ => ⟨u, by
          show (f s a).bind (fun t => runPartial f t rest) = some u
          rw [moved]
          exact ran, heldU, outU⟩

/-- **Every admitted course longer than the margin ends at the exit**, valid. -/
theorem exits {f : S → A → Option S} {adm : A → Prop} {valid exit : S → Prop}
    {margin : S → Nat} (reserved : Reserved f adm valid exit margin) :
    ∀ (plan : List A) (s : S), valid s → (∀ a, a ∈ plan → adm a) → margin s < plan.length →
      ∃ t, runPartial f s plan = some t ∧ valid t ∧ exit t
  | [], _, _, _, long => absurd long (Nat.not_lt_zero _)
  | a :: rest, s, held, admissible, long =>
    match reserved.moves s a held (admissible a (.head _)) with
    | ⟨t, moved, held', next⟩ =>
      have onward : ∃ u, runPartial f t rest = some u ∧ valid u ∧ exit u :=
        match next with
        | .inl out => stays_exit reserved rest t held' out fun b mem => admissible b (.tail _ mem)
        | .inr lowered =>
          have longT : margin t + 1 < rest.length + 1 := by
            rw [lowered]
            exact long
          exits reserved rest t held' (fun b mem => admissible b (.tail _ mem))
            (Nat.lt_of_succ_lt_succ longT)
      match onward with
      | ⟨u, ran, heldU, outU⟩ => ⟨u, by
          show (f s a).bind (fun t => runPartial f t rest) = some u
          rw [moved]
          exact ran, heldU, outU⟩

namespace Slow

/-- The margin counts down by one at each move and the exit (`none`) follows at zero. -/
def step : Option Nat → Unit → Option (Option Nat)
  | none, _ => some none
  | some 0, _ => some none
  | some (n + 1), _ => some (some n)

def margin : Option Nat → Nat
  | none => 0
  | some n => n

theorem reserved :
    Reserved step (fun _ => True) (fun _ => True) (fun s => s = none) margin :=
  ⟨fun s _ _ _ => match s with
    | none => ⟨none, rfl, trivial, .inl rfl⟩
    | some 0 => ⟨none, rfl, trivial, .inl rfl⟩
    | some (n + 1) => ⟨some n, rfl, trivial, .inr rfl⟩,
   fun s _ t out moved => by
    subst out
    exact (Option.some.inj moved).symm⟩

/-- **The bound is attained**: a course as long as the margin can miss the exit. -/
theorem misses : ∀ n : Nat, runPartial step (some n) (List.replicate n ()) = some (some 0)
  | 0 => rfl
  | n + 1 => misses n

end Slow

end Countdown

end Becoming

section CountdownCourses

/-!
## Countdown on the courses of a partial law's process

`Becoming.Countdown` states counted work and a reserved exit for a partial law, on its runs of
ticks and of plans (`ticks`, `Assurance.runPartial`). A partial law is a process of the spine
(`Assurance.ofPartial`), whose traces are exactly the courses its run completes
(`Assurance.trace_ofPartial_iff`), and `n` ticks are its run along `n` unit moves
(`Countdown.ticks_eq_runPartial`). `Becoming.Courses` states completion and the shorter courses on
that process; this section states the rest of `Becoming.Countdown` on its courses.

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

end CountdownCourses
