import Becoming.FormedLoops
import Becoming.Frame

/-!
# Coupling traces: couplings read as the steps of a process

`Becoming.Loops`, `Becoming.Remainder`, `Becoming.Closing`, `Becoming.Thresholds`,
`Becoming.Observation` and `Becoming.Frequency` state their laws of loops and chains on an array of
coupling strengths: a level of `d` is coupled into `c` (`Couples`) where some formation present,
outside the part, exchanges with `c` with positive strength on a level of `d`; chains of couplings
lead from one condition to another (`Upstream`) or back to it (`OnLoop`), and chains in time order
read, at each coupling, a level the coupling before had reached (`CoupledIntoBy`, `ChainInTime`).
A relation stepping from one condition to another is a process of the spine, and a chain is a
trace of it. This module reads the couplings so, exactly, and states those modules' laws of the
traces. No premise enters beyond what each theorem names.

* **The couplings as a process.** The coupling process (`couplingProcess`) steps from `d` to `c` by
  the step `u` at which a coupling of `d` into `c` acts. A coupling is a step of it
  (`couples_iff_step`); what lies upstream is what it reaches (`upstream_iff_reach`); a loop through
  `e` is a trace of one step or more from `e` back to `e` (`onLoop_iff_trace`). A sequence whose
  successive members are steps of a process is a trace of it, for every process
  (`chain_iff_trace`).
* **Chains in time order as traces back in time.** The retrace process (`retraceProcess`) steps
  from the level of `c` at `t` back, by a coupling acting at `u` before `t`, to the level of `d` at
  `s` that the coupling reads. A chain in time order of `j` couplings ending at `c` by `t` is a
  trace of `j` steps of it from the level of `c` at `t` (`coupledIntoBy_iff_trace`); a chain in
  time order along a sequence is such a trace (`chainInTime_trace`), and a return is a trace back
  to its condition (`returns_trace`).
* **How loops form (`Becoming.Closing`).** A loop of the coupling process is a loop of the
  couplings formed before some step (`loop_iff_formed`), and what it reaches is what the couplings
  formed by some step reach (`reach_iff_formed`). A loop that forms at a step passes through a step
  of the process labelled by that step (`loop_forms_by_closing`), as does a route that forms
  (`route_forms_by_closing`, `Becoming.Observation`). The self-loop acting from `T` on has a loop
  formed by `T + 1` (`onset_forms`) and none formed by `T` (`onset_not_formed`).
* **Loops lie within what is read (`Becoming.Thresholds`, `Becoming.Observation`).** With strengths
  restricted to a schedule of what the law reads, a loop forms through a reading
  (`loop_succ_reads`), a step from a condition into itself is read (`self_step_reads`), and the
  routes of the restricted strengths are routes of reading (`reach_readCouplings`). Under a law
  reading a stock only below a threshold, the standing law's restricted couplings have no loop
  through the stock and reach nothing else from it (`standing_no_loop_traces`), while every
  strengths of the draw have a loop through the stock (`draw_loop`). In the measurement, before
  `T` the stock reaches only itself (`measure_reach_before`) and lies on no loop
  (`measure_no_loop_before`); at `T` a loop through it forms (`measure_loop_at`).
* **Chains in time order (`Becoming.Remainder`).** A trace back from a level is one from every later
  level (`retrace_later`), and its first steps are traces back too (`retrace_shorten`). A coupling
  recurs exactly where it is a step of the couplings from every step on (`recurs_iff_steps`), so a
  schedule has settled by `N` exactly where every step of the couplings from `N` on is a step of the
  couplings from every later step (`settled_iff_steps`); couplings that read the current level at
  every step have settled from the start (`settled_zero_of_always`). Every coupling process with its
  conditions listed settles exactly where every decided two-place family of Booleans has every row
  `true` somewhere or some row `false` throughout (`settled_every_iff_steps`, through
  `Becoming.Frequency`'s `settled_every_iff`): settling for every coupling process is a principle of
  reasoning, exactly. The loop acting once has no
  trace back of two steps (`once_no_retrace_of_two`) and has settled from the second step
  (`once_settled`).
* **How often couplings act (`Becoming.Frequency`).** The self-loop on a schedule steps back from
  a level exactly by the marked steps before it, reading the current level (`selfLoop_retrace_iff`),
  and each marked step is a return (`selfLoop_returns`). A coupling all of whose steps back read
  levels before `N` is not a step of the couplings from every step on (`stops_not_recurs`). The
  self-loop's world coupling at every step is the world of `Becoming.Loops`' self-loop
  (`scheduleWorld_always`), and coupling from `T` on the world of the loop forming at `T`
  (`scheduleWorld_onset`).

What is not derived: the converse of `chainInTime_trace` (a trace back read as a chain along a
sequence; `coupledIntoBy_iff_trace` is the exact form); the strengths, supplied as in
`Becoming.Propagation`. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v

namespace CouplingTraces

/-! ## Chains are traces -/

section Chains

variable {X : Type u} {L : Type v} {P : Process X L}

/-- A sequence begun at `e`. -/
def consSeq (e : X) (v : Nat → X) : Nat → X
  | 0 => e
  | i + 1 => v i

/-- **A chain of steps along a sequence is a trace**, for every process: a sequence from `e` to
`c` whose first `j` successive members are steps of the process is a trace of `j` moves. -/
theorem chain_iff_trace : ∀ (j : Nat) {e c : X},
    (∃ v : Nat → X, v 0 = e ∧ v j = c ∧ ∀ i, i < j → ∃ a, P.step (v i) a (v (i + 1))) ↔
      ∃ as : List L, as.length = j ∧ Trace P e as c
  | 0, e, _ =>
    ⟨fun ⟨_, start, ends, _⟩ =>
      ⟨[], rfl, Eq.subst (motive := fun x => Trace P e [] x) (start.symm.trans ends) (.nil e)⟩,
     fun ⟨as, len, tr⟩ => match as, len, tr with
      | [], _, tr => ⟨fun _ => e, rfl, trace_nil_iff.mp tr, fun i lt => absurd lt (Nat.not_lt_zero i)⟩
      | _ :: _, len, _ => Nat.noConfusion len⟩
  | j + 1, e, c =>
    ⟨fun ⟨v, start, ends, steps⟩ =>
      match steps 0 (Nat.succ_pos j),
        (chain_iff_trace j (e := v 1) (c := c)).mp
          ⟨fun i => v (i + 1), rfl, ends, fun i lt => steps (i + 1) (Nat.succ_lt_succ lt)⟩ with
      | ⟨a, first⟩, ⟨as, len, tr⟩ =>
        ⟨a :: as, congrArg (· + 1) len,
         Eq.subst (motive := fun x => Trace P x (a :: as) c) start (.cons first tr)⟩,
     fun ⟨as, len, tr⟩ => match as, len, tr with
      | [], len, _ => Nat.noConfusion len
      | a :: as, len, tr =>
        match trace_cons_iff.mp tr with
        | ⟨m, first, rest⟩ =>
          match (chain_iff_trace j (e := m) (c := c)).mpr ⟨as, Nat.succ.inj len, rest⟩ with
          | ⟨v, start, ends, steps⟩ =>
            ⟨consSeq e v, rfl, ends, fun i lt => match i, lt with
              | 0, _ => ⟨a, Eq.subst (motive := fun x => P.step e a x) start.symm first⟩
              | i + 1, lt => steps i (Nat.lt_of_succ_lt_succ lt)⟩⟩

end Chains

/-! ## The couplings as a process -/

section Couplings

variable {F C : Type} {cs : List C} {part : F → Bool} {k : Nat → F → C → Nat → C → Nat}
  {present : Nat → List F}

/-- **The coupling process.** It steps from `d` to `c` by the step `u` at which the level of `d` is
coupled into `c`: a formation present at `u`, outside the part, exchanges with `c` with positive
strength on a level of `d` up to `u`. -/
def couplingProcess (cs : List C) (part : F → Bool) (k : Nat → F → C → Nat → C → Nat)
    (present : Nat → List F) : Process C Nat :=
  ⟨fun d u c => ∃ s, CouplesAt cs part k present u s d c⟩

/-- **What lies upstream is what the coupling process reaches.** -/
theorem upstream_iff_reach {e c : C} :
    Upstream cs part k present e c ↔ Reach (couplingProcess cs part k present) e c :=
  ⟨fun ⟨v, j, start, ends, chain⟩ =>
    match (chain_iff_trace j).mp ⟨v, start, ends, fun i lt => couples_iff_couplesAt.mp (chain i lt)⟩ with
    | ⟨as, _, tr⟩ => ⟨as, tr⟩,
   fun ⟨as, tr⟩ =>
    match (chain_iff_trace as.length).mpr ⟨as, rfl, tr⟩ with
    | ⟨v, start, ends, steps⟩ =>
      ⟨v, as.length, start, ends, fun i lt => couples_iff_couplesAt.mpr (steps i lt)⟩⟩

/-- **A loop through `e` is a trace of the coupling process of one step or more from `e` back to
`e`.** -/
theorem onLoop_iff_trace {e : C} :
    OnLoop cs part k present e ↔
      ∃ u us, Trace (couplingProcess cs part k present) e (u :: us) e :=
  ⟨fun ⟨v, m, pos, start, back, chain⟩ =>
    match (chain_iff_trace m).mp ⟨v, start, back, fun i lt => couples_iff_couplesAt.mp (chain i lt)⟩ with
    | ⟨as, len, tr⟩ => match as, len, tr with
      | [], len, _ => absurd (Eq.subst (motive := fun x => 0 < x) len.symm pos) (Nat.lt_irrefl 0)
      | u :: us, _, tr => ⟨u, us, tr⟩,
   fun ⟨u, us, tr⟩ =>
    match (chain_iff_trace (us.length + 1)).mpr ⟨u :: us, rfl, tr⟩ with
    | ⟨v, start, back, steps⟩ =>
      ⟨v, us.length + 1, Nat.succ_pos _, start, back, fun i lt => couples_iff_couplesAt.mpr (steps i lt)⟩⟩

/-- **The retrace process.** It steps from the level of `c` at step `t` back, by a coupling acting
at a step `u` before `t`, to the level of `d` at the step `s` that the coupling reads. -/
def retraceProcess (cs : List C) (part : F → Bool) (k : Nat → F → C → Nat → C → Nat)
    (present : Nat → List F) : Process (Nat × C) Nat :=
  ⟨fun x u y => u < x.1 ∧ CouplesAt cs part k present u y.1 y.2 x.2⟩

/-- **A chain in time order is a trace back in time.** A chain in time order of `j` couplings ends
at `c` by step `t` exactly where the retrace process has a trace of `j` steps from the level of
`c` at `t`. -/
theorem coupledIntoBy_iff_trace : ∀ (j t : Nat) (c : C),
    CoupledIntoBy cs part k present j t c ↔
      ∃ as y, as.length = j ∧ Trace (retraceProcess cs part k present) (t, c) as y
  | 0, _, _ => ⟨fun _ => ⟨[], _, rfl, .nil _⟩, fun _ => trivial⟩
  | j + 1, _, _ =>
    ⟨fun ⟨u, s, d, lt, at_, chain⟩ =>
      match (coupledIntoBy_iff_trace j s d).mp chain with
      | ⟨as, y, len, tr⟩ => ⟨u :: as, y, congrArg (· + 1) len, .cons ⟨lt, at_⟩ tr⟩,
     fun ⟨as, y, len, tr⟩ => match as, len, tr with
      | [], len, _ => Nat.noConfusion len
      | u :: as, len, tr =>
        match trace_cons_iff.mp tr with
        | ⟨m, ⟨lt, at_⟩, rest⟩ =>
          ⟨u, m.1, m.2, lt, at_,
           (coupledIntoBy_iff_trace j m.1 m.2).mpr ⟨as, y, Nat.succ.inj len, rest⟩⟩⟩

/-- **A chain in time order along a sequence is a trace back in time**, from the level of its last
condition at the step it ends by to a level of its first condition read from the step it starts
from on. -/
theorem chainInTime_trace {v : Nat → C} {T : Nat} : ∀ {p T' : Nat},
    ChainInTime cs part k present v T p T' →
      ∃ as s, as.length = p ∧ Trace (retraceProcess cs part k present) (T', v p) as (s, v 0) ∧
        T ≤ s
  | 0, T', le => ⟨[], T', rfl, .nil _, le⟩
  | _ + 1, _, ⟨u, _, lt, at_, chain⟩ =>
    match chainInTime_trace chain with
    | ⟨as, s', len, tr, le⟩ => ⟨u :: as, s', congrArg (· + 1) len, .cons ⟨lt, at_⟩ tr, le⟩

/-- **A return is a trace back to its condition**: from the level of `e` at the step it returns by,
of one step or more, to a level of `e` read from the step it starts from on. -/
theorem returns_trace {e : C} {T T' : Nat} (back : RoundTrip cs part k present e T T') :
    ∃ u us s, Trace (retraceProcess cs part k present) (T', e) (u :: us) (s, e) ∧ T ≤ s :=
  match back with
  | ⟨v, _, start, close, chain⟩ =>
    match chainInTime_trace chain with
    | ⟨as, s, len, tr, le⟩ => match as, len, tr with
      | u :: us, _, tr =>
        ⟨u, us, s,
         Eq.subst (motive := fun x => Trace (retraceProcess cs part k present) (T', e) (u :: us) (s, x))
           start (Eq.subst (motive := fun x =>
             Trace (retraceProcess cs part k present) (T', x) (u :: us) (s, v 0)) close tr), le⟩

end Couplings

/-! ## How loops form -/

section Forming

variable {F C : Type} {cs : List C} {part : F → Bool} {k : Nat → F → C → Nat → C → Nat}
  {present : Nat → List F}

/-- **The loops of the coupling process are the loops of the couplings formed before some step.** -/
theorem loop_iff_formed {e : C} :
    (∃ u us, Trace (couplingProcess cs part k present) e (u :: us) e) ↔
      ∃ T, ∃ u us, Trace (couplingProcess cs part (strengthsBefore T k) present) e (u :: us) e :=
  onLoop_iff_trace.symm.trans (onLoop_iff_formed.trans
    ⟨fun ⟨T, loop⟩ => ⟨T, onLoop_iff_trace.mp loop⟩, fun ⟨T, loop⟩ => ⟨T, onLoop_iff_trace.mpr loop⟩⟩)

/-- **What the coupling process reaches is what the couplings formed by some step reach.** -/
theorem reach_iff_formed {e c : C} :
    Reach (couplingProcess cs part k present) e c ↔
      ∃ T, Reach (couplingProcess cs part (strengthsBefore T k) present) e c :=
  upstream_iff_reach.symm.trans (upstream_iff_formed.trans
    ⟨fun ⟨T, up⟩ => ⟨T, upstream_iff_reach.mp up⟩, fun ⟨T, up⟩ => ⟨T, upstream_iff_reach.mpr up⟩⟩)

/-- **A loop that forms passes through a step labelled by the step it forms.** Where the couplings
formed by `T + 1` have a loop through `e` and those formed by `T` have none, some step from `d` to
`c` acts at `T`, with `c` reaching `e` and `e` reaching `d` by the couplings formed by `T + 1`. -/
theorem loop_forms_by_closing {T : Nat} {e : C}
    (now : ∃ u us, Trace (couplingProcess cs part (strengthsBefore (T + 1) k) present) e (u :: us) e)
    (before : ¬ ∃ u us, Trace (couplingProcess cs part (strengthsBefore T k) present) e (u :: us) e) :
    ∃ d c, (couplingProcess cs part k present).step d T c ∧
      Reach (couplingProcess cs part (strengthsBefore (T + 1) k) present) c e ∧
        Reach (couplingProcess cs part (strengthsBefore (T + 1) k) present) e d :=
  match forms_by_closing (onLoop_iff_trace.mpr now) (fun loop => before (onLoop_iff_trace.mp loop)) with
  | ⟨d, c, s, at_, up, down⟩ => ⟨d, c, ⟨s, at_⟩, upstream_iff_reach.mp up, upstream_iff_reach.mp down⟩

/-- **A route that forms passes through a step labelled by the step it forms.** -/
theorem route_forms_by_closing {T : Nat} {c e : C}
    (now : Reach (couplingProcess cs part (strengthsBefore (T + 1) k) present) c e)
    (before : ¬ Reach (couplingProcess cs part (strengthsBefore T k) present) c e) :
    ∃ d d', (couplingProcess cs part k present).step d T d' ∧
      Reach (couplingProcess cs part (strengthsBefore (T + 1) k) present) c d ∧
        Reach (couplingProcess cs part (strengthsBefore (T + 1) k) present) d' e :=
  match Becoming.route_forms_by_closing (upstream_iff_reach.mpr now)
      (fun up => before (upstream_iff_reach.mp up)) with
  | ⟨d, d', s, at_, up, down⟩ =>
    ⟨d, d', ⟨s, at_⟩, upstream_iff_reach.mp up, upstream_iff_reach.mp down⟩

end Forming

/-- **The self-loop acting from `T` on has a loop formed by `T + 1`.** -/
theorem onset_forms (T : Nat) :
    ∃ u us, Trace (couplingProcess [()] (fun _ => false)
      (strengthsBefore (T + 1) (Closing.Onset.strengths T)) (fun _ => [()])) () (u :: us) () :=
  onLoop_iff_trace.mp (Closing.Onset.forms T)

/-- **The self-loop acting from `T` on has no loop formed by `T`.** -/
theorem onset_not_formed (T : Nat) :
    ¬ ∃ u us, Trace (couplingProcess [()] (fun _ => false)
      (strengthsBefore T (Closing.Onset.strengths T)) (fun _ => [()])) () (u :: us) () :=
  fun loop => Closing.Onset.not_formed T (onLoop_iff_trace.mpr loop)

/-! ## Loops lie within what is read -/

section Reading

variable {F C : Type} {cs : List C} {part : F → Bool} {k : Nat → F → C → Nat → C → Nat}
  {present : Nat → List F}

/-- **A loop forms through a reading.** With the strengths restricted to a schedule of what is
read, the loops formed by `T + 1` are those formed by `T` and those through a formation that, at
`T`, reads the level of a condition `d` and gives to a condition `c` from which the couplings formed
by `T + 1` reach `d` through the loop. -/
theorem loop_succ_reads {reads : Nat → F → C → Bool} {T : Nat} {e : C} :
    (∃ u us, Trace (couplingProcess cs part (strengthsBefore (T + 1) (restrictReads reads k)) present)
        e (u :: us) e) ↔
      (∃ u us, Trace (couplingProcess cs part (strengthsBefore T (restrictReads reads k)) present)
        e (u :: us) e) ∨
        ∃ d c s h, h ∈ present T ∧ part h = false ∧ s ≤ T ∧ d ∈ cs ∧ reads T h d = true ∧
          0 < k T h c s d ∧
          Reach (couplingProcess cs part (strengthsBefore (T + 1) (restrictReads reads k)) present)
            c e ∧
          Reach (couplingProcess cs part (strengthsBefore (T + 1) (restrictReads reads k)) present)
            e d :=
  onLoop_iff_trace.symm.trans (onLoop_succ_reads.trans
    ⟨fun formed => match formed with
      | .inl before => .inl (onLoop_iff_trace.mp before)
      | .inr ⟨d, c, s, h, mem, out, le, dMem, read, pos, up, down⟩ =>
        .inr ⟨d, c, s, h, mem, out, le, dMem, read, pos, upstream_iff_reach.mp up,
          upstream_iff_reach.mp down⟩,
     fun formed => match formed with
      | .inl before => .inl (onLoop_iff_trace.mpr before)
      | .inr ⟨d, c, s, h, mem, out, le, dMem, read, pos, up, down⟩ =>
        .inr ⟨d, c, s, h, mem, out, le, dMem, read, pos, upstream_iff_reach.mpr up,
          upstream_iff_reach.mpr down⟩⟩)

/-- **A step from a condition into itself is read.** With the strengths restricted to what is
read, a step of the coupling process from `c` into `c` is read by a formation outside the part. -/
theorem self_step_reads {reads : Nat → F → C → Bool} {c : C} {u : Nat}
    (step : (couplingProcess cs part (restrictReads reads k) present).step c u c) :
    ∃ u' h, h ∈ present u' ∧ part h = false ∧ reads u' h c = true :=
  self_coupling_reads (couples_iff_couplesAt.mpr ⟨u, step⟩)

/-- **The routes of the restricted strengths are routes of reading**, formed by the same step. -/
theorem reach_readCouplings {reads : Nat → F → C → Nat → C → Bool} {T : Nat} {c e : C}
    (reach : Reach (couplingProcess cs part (strengthsBefore T (restrictInto reads k)) present) c e) :
    Reach (couplingProcess cs part (strengthsBefore T (readCouplings reads)) present) c e :=
  upstream_iff_reach.mp (upstream_readCouplings (upstream_iff_reach.mpr reach))

/-- **The standing law's restricted couplings have no loop through the stock and reach nothing
else from it.** For a law reading a stock only below a threshold and every strengths of its
standing law, with the strengths restricted to what the standing law reads. -/
theorem standing_no_loop_traces {law : ExchangeLaw F C} {c : C} {θ : Nat → Nat} {mark : C → Bool}
    (r : law.ReadsBelow part c θ) (marked : mark c = true) (only : ∀ e, e ≠ c → mark e = false)
    (strengths : ∀ t h e s d, part h = false → s ≤ t →
      (law.standing mark θ).RespondsWithin t h e s d (k t h e s d)) :
    (¬ ∃ u us, Trace (couplingProcess cs part (restrictReads (offStock mark) k) present)
        c (u :: us) c) ∧
      ∀ e, Reach (couplingProcess cs part (restrictReads (offStock mark) k) present) c e → e = c :=
  ⟨fun loop => (r.standing_no_loop marked only (cs := cs) (present := present) strengths).2.1
      (onLoop_iff_trace.mpr loop),
   fun e reach => (r.standing_no_loop marked only (cs := cs) (present := present) strengths).2.2 e
      (upstream_iff_reach.mpr reach)⟩

end Reading

/-- **Every strengths of the draw have a loop through the stock**, however the stock stood before
the break. -/
theorem draw_loop (N : Nat) {k : Nat → Unit → Bool → Nat → Bool → Nat}
    (strengths : ∀ t h c s d, s ≤ t →
      (Thresholds.Draw.law (N + 1)).RespondsWithin t h c s d (k t h c s d)) :
    ∃ u us, Trace (couplingProcess [true, false] (fun _ => false) k (fun _ => [()]))
      true (u :: us) true :=
  onLoop_iff_trace.mp (Thresholds.Draw.forms_at_break N strengths).2.2

/-- **Before `T`, the stock of the measurement reaches only itself.** -/
theorem measure_reach_before {T T' : Nat} (le : T' ≤ T) {e : Bool}
    (reach : Reach (couplingProcess [true, false] (fun _ => false)
      (strengthsBefore T' (readCouplings (Observation.Measure.reads T))) (fun _ => [()])) true e) :
    e = true :=
  Observation.Measure.downstream_before le (upstream_iff_reach.mpr reach)

/-- **Before `T`, no loop of the measurement passes through the stock.** -/
theorem measure_no_loop_before {T : Nat} :
    ¬ ∃ u us, Trace (couplingProcess [true, false] (fun _ => false)
      (strengthsBefore T (readCouplings (Observation.Measure.reads T))) (fun _ => [()]))
      true (u :: us) true :=
  fun loop => Observation.Measure.no_loop_before (onLoop_iff_trace.mpr loop)

/-- **At `T` the loop of the measurement through the stock forms.** -/
theorem measure_loop_at (T : Nat) :
    ∃ u us, Trace (couplingProcess [true, false] (fun _ => false)
      (strengthsBefore (T + 1) (readCouplings (Observation.Measure.reads T))) (fun _ => [()]))
      true (u :: us) true :=
  onLoop_iff_trace.mp (Observation.Measure.loop_at T)

/-! ## Chains in time order -/

section Remainder

variable {F C : Type} {cs : List C} {part : F → Bool} {k : Nat → F → C → Nat → C → Nat}
  {present : Nat → List F}

/-- **A trace back from a level is a trace back from every later level of its condition**, of as
many steps. -/
theorem retrace_later {j t t' : Nat} {c : C} (le : t ≤ t')
    (back : ∃ as y, as.length = j ∧ Trace (retraceProcess cs part k present) (t, c) as y) :
    ∃ as y, as.length = j ∧ Trace (retraceProcess cs part k present) (t', c) as y :=
  (coupledIntoBy_iff_trace j t' c).mp (((coupledIntoBy_iff_trace j t c).mpr back).later le)

/-- **Fewer steps back are a trace back too.** -/
theorem retrace_shorten {i j t : Nat} {c : C} (le : i ≤ j)
    (back : ∃ as y, as.length = j ∧ Trace (retraceProcess cs part k present) (t, c) as y) :
    ∃ as y, as.length = i ∧ Trace (retraceProcess cs part k present) (t, c) as y :=
  (coupledIntoBy_iff_trace i t c).mp (CoupledIntoBy.shorten le ((coupledIntoBy_iff_trace j t c).mpr back))

/-- **A coupling recurs exactly where it is a step of the couplings from every step on.** -/
theorem recurs_iff_steps {d c : C} :
    CouplingRecurs cs part k present d c ↔
      ∀ N, ∃ u, (couplingProcess cs part (strengthsFrom N k) present).step d u c :=
  couplingRecurs_iff.trans
    ⟨fun from_ N => couples_iff_couplesAt.mp (from_ N), fun from_ N => couples_iff_couplesAt.mpr (from_ N)⟩

/-- **A schedule has settled by `N` exactly where every step of the couplings from `N` on is a step
of the couplings from every later step.** -/
theorem settled_iff_steps {N : Nat} :
    SettledFrom cs part k present N ↔
      ∀ d u c, (couplingProcess cs part (strengthsFrom N k) present).step d u c →
        ∀ N', ∃ u', (couplingProcess cs part (strengthsFrom N' k) present).step d u' c :=
  ⟨fun settled d u c step => recurs_iff_steps.mp (settled d c (couples_iff_couplesAt.mpr ⟨u, step⟩)),
   fun steps d c from_ => match couples_iff_couplesAt.mp from_ with
    | ⟨u, step⟩ => recurs_iff_steps.mpr (steps d u c step)⟩

/-- **Couplings that read the current level at every step have settled from the start.** Where
every step of the coupling process from `d` into `c` comes with a step back from the level of `c`
after each step to the level of `d` then, every step of the couplings from the start on is a step
of the couplings from every step on. -/
theorem settled_zero_of_always
    (always : ∀ d u c, (couplingProcess cs part k present).step d u c →
      ∀ t, (retraceProcess cs part k present).step (t + 1, c) t (t, d)) :
    ∀ d u c, (couplingProcess cs part (strengthsFrom 0 k) present).step d u c →
      ∀ N', ∃ u', (couplingProcess cs part (strengthsFrom N' k) present).step d u' c :=
  settled_iff_steps.mp (settledFrom_zero_of_always fun d c couples =>
    match couples_iff_couplesAt.mp couples with
    | ⟨u, step⟩ => fun t => match (always d u c step t).2 with
      | ⟨h, mem, out, _, dMem, pos⟩ => ⟨h, mem, out, dMem, pos⟩)

end Remainder

/-- **Every coupling process settles exactly where the dichotomy holds.** For every coupling process
with its conditions listed, some step `N` has every step of the couplings from `N` on a step of the
couplings from every later step, exactly where every decided two-place family of Booleans has every
row `true` somewhere or some row `false` throughout (`RecursOrStops`). -/
theorem settled_every_iff_steps :
    (∀ (F' C' : Type) (cs : List C') (part : F' → Bool) (k : Nat → F' → C' → Nat → C' → Nat)
        (present : Nat → List F'), (∀ c, c ∈ cs) →
        ∃ N, ∀ d u c, (couplingProcess cs part (strengthsFrom N k) present).step d u c →
          ∀ N', ∃ u', (couplingProcess cs part (strengthsFrom N' k) present).step d u' c) ↔
      RecursOrStops :=
  Iff.trans
    ⟨fun settles F' C' cs part k present every => match settles F' C' cs part k present every with
      | ⟨N, steps⟩ => ⟨N, settled_iff_steps.mpr steps⟩,
     fun settles F' C' cs part k present every => match settles F' C' cs part k present every with
      | ⟨N, settled⟩ => ⟨N, settled_iff_steps.mp settled⟩⟩
    settled_every_iff

/-- **The loop acting once has no trace back of two steps**, though it has a loop. -/
theorem once_no_retrace_of_two (t : Nat) :
    ¬ ∃ as y, as.length = 2 ∧
      Trace (retraceProcess [()] (fun _ => false) Loops.Once.strengths (fun _ => [()])) (t, ()) as y :=
  fun back => Loops.Once.no_chain_of_two t ((coupledIntoBy_iff_trace 2 t ()).mpr back)

/-- **The loop acting once has settled from the second step.** -/
theorem once_settled :
    ∀ d u c, (couplingProcess [()] (fun _ => false) (strengthsFrom 1 Loops.Once.strengths)
        (fun _ => [()])).step d u c →
      ∀ N', ∃ u', (couplingProcess [()] (fun _ => false) (strengthsFrom N' Loops.Once.strengths)
        (fun _ => [()])).step d u' c :=
  settled_iff_steps.mp Loops.Once.settled

/-! ## How often couplings act -/

/-- **The self-loop on a schedule steps back exactly by the marked steps**, reading the current
level, where its strength is positive. -/
theorem selfLoop_retrace_iff {on : Nat → Bool} {M t u s : Nat} :
    (retraceProcess [()] (fun _ => false) (Frequency.SelfLoop.strengths on M) (fun _ => [()])).step
        (t, ()) u (s, ()) ↔
      u < t ∧ on u = true ∧ s = u ∧ 0 < M :=
  ⟨fun ⟨lt, at_⟩ => ⟨lt, Frequency.SelfLoop.couplesAt_iff.mp at_⟩,
   fun ⟨lt, rest⟩ => ⟨lt, Frequency.SelfLoop.couplesAt_iff.mpr rest⟩⟩

/-- **Each marked step of the self-loop is a return**: a trace back from its level after the step
to its level at a step from the marked one on. -/
theorem selfLoop_returns {on : Nat → Bool} {M u : Nat} (yes : on u = true) (strong : 0 < M) :
    ∃ a as s, Trace (retraceProcess [()] (fun _ => false) (Frequency.SelfLoop.strengths on M)
      (fun _ => [()])) (u + 1, ()) (a :: as) (s, ()) ∧ u ≤ s :=
  returns_trace (Frequency.SelfLoop.roundTrip yes strong)

/-- **A coupling all of whose steps back read levels before `N` is not a step of the couplings from
every step on.** -/
theorem stops_not_recurs {F C : Type} {cs : List C} {part : F → Bool}
    {k : Nat → F → C → Nat → C → Nat} {present : Nat → List F} {d c : C} {N : Nat}
    (stops : ∀ t u s, (retraceProcess cs part k present).step (t, c) u (s, d) → s < N) :
    ¬ ∀ N', ∃ u, (couplingProcess cs part (strengthsFrom N' k) present).step d u c :=
  fun from_ => StopsBy.not_recurs (N := N) (fun u s at_ => stops (u + 1) u s ⟨Nat.lt_succ_self u, at_⟩)
    (recurs_iff_steps.mpr from_)

/-- **The world of the self-loop coupling at every step is the world of `Becoming.Loops`'
self-loop.** -/
theorem scheduleWorld_always (M D : Nat) :
    FormedLoops.scheduleWorld (fun _ => true) M D =
      carriedWorld [()] (fun _ => false) (fun _ _ _ => 0) (Loops.SelfLoop.strengths M)
        (fun _ => [()]) (fun _ => D) :=
  congrArg (fun k => carriedWorld [()] (fun _ => false) (fun _ _ _ => 0) k (fun _ => [()])
    (fun _ => D)) (Frequency.SelfLoop.always M)

/-- **The world of the self-loop coupling from `T` on is the world of the loop forming at `T`.** -/
theorem scheduleWorld_onset (T D : Nat) :
    FormedLoops.scheduleWorld (Nat.ble T) 1 D = FormedLoops.onsetWorld T D :=
  congrArg (fun k => carriedWorld [()] (fun _ => false) (fun _ _ _ => 0) k (fun _ => [()])
    (fun _ => D)) (Frequency.SelfLoop.onset T)

end CouplingTraces

end Becoming
