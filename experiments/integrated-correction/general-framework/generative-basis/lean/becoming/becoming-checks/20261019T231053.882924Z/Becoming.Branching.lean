import Becoming.Unfolding
import Becoming.Attraction
import Becoming.Capture

/-!
# Branching: what every process keeps, loses, returns to and is drawn into, and determinacy up to likeness

`Becoming.Recurrence` (R6) and `Becoming.Attraction` (P67) state their laws for a determined law
`next`, where the configuration fixes its whole course. A process of the spine fixes only which
steps are admissible: from one configuration several moves, or several outcomes of one move, can
be open, and the course branches. Ren, 12 October 2026: "move towards 100%". This module states
R6's and P67's laws for every process, with no premise beyond what each law names, says which
survive, which hold one way only and which fail, with witnesses; it restates theorems of
`Becoming.Experiment` and `Becoming.Mechanism` stated with `Determined` up to likeness
(`DeterminedAt` of `Becoming.Unfolding`), naming with a witness where equality is needed; and it
states Capture's rule region as an instance of P67's absorbing regions.

* **What R6's notions become.** A configuration can be had `n` steps on where some course of `n`
  moves leads to it (`Branching.Reachable`); it returns where a step from it leads to where it can
  be had again (`Branching.Returns`); a process merges where two distinct configurations step to
  one (`Branching.Merges`, `Branching.Lossless`). These five are stated in `Becoming.Recurrence`,
  and R6's notions of a determined law are them at the law's process by definition (`Law.Lossless`
  and the others are abbreviations at `Law.process next`), so the bridges `law_reachable_iff`,
  `law_keeps_iff`, `law_returns_iff`, `law_lossless_iff` and `law_merges_iff` hold by `Iff.rfl`;
  the courses of a determined law are its orbits (`law_trace_iff`, `law_reach_iff`, also in
  `Becoming.Recurrence`).
* **What survives with no premise.** A possibility lost stays lost (`Branching.lost_stays`). A
  configuration that returns can be had at every step (`Branching.Returns.reachable`), so where
  every configuration returns every possibility is kept (`keeps_of_returns`); every possibility
  is kept exactly where every configuration can be had at the next step (`keeps_iff_fed`).
* **The exact condition for returning.** A configuration returns exactly where its own course can
  have it at the next step (`returns_iff_fed_ahead`). Every configuration returns exactly where
  every region the process never leaves keeps every possibility of its own
  (`returns_iff_keepsWithin`), that is, has each of its configurations at the next step from
  within it (`returns_iff_fedWithin`, `keepsWithin_iff_fedWithin`). No finiteness is used.
  Keeping every possibility is the case of the region of all configurations alone, and is not
  enough (next bullet).
* **What holds one way only, within finitely many configurations.** Keeping every possibility
  does not give returning: in `Transit` three configurations, each of which can move and each of
  which can be had at every step, and `between` never returns (`Transit.keeps_not_returns`).
  Merging nothing gives returning along runs: where a list holds the configurations of a run of a
  process that merges nothing, every configuration of the run comes back on the run itself
  (`Lossless.comes_back`, `Lossless.recurs`), so a configuration at which a run begins returns
  (`Branching.Lossless.returns`), nothing rises along a run (`Branching.Lossless.no_rise`), a
  rise along a run needs a merge (`Branching.rise_not_lossless`), and merging nothing while a
  configuration with a run never returns needs openness (`Branching.Lossless.unlisted`). The run
  is needed: the fork of `Becoming.Unfolding`, whose ends cannot move, merges nothing and its
  origin never returns (`fork_lossless_not_returns`). Returning does not give merging nothing,
  and a merge need not lose a possibility: `OneWay` merges `false` and `true`, both return, and
  every possibility is kept (`OneWay.merge_keeps`).
* **Merged stays merged needs determinacy.** Under a determined process runs that meet stay
  together while they take the same moves (`Determined.stays_merged`); in `Coarse` of
  `Becoming.Mechanism`, two runs from one configuration with the same moves part at the first
  step (`Coarse.meet_and_part`).
* **Possibly and necessarily drawn.** A configuration outside a region is possibly drawn into it
  where some course from it enters it (`PossiblyDrawnInto`), and necessarily drawn where every
  run from it does (`NecessarilyDrawnInto`); drawn, where some region the process never leaves
  (`Frame.Invariant`) so draws it (`PossiblyDrawn`, `NecessarilyDrawn`). Under a determined law
  both are P67's (`law_possibly_iff`, `law_necessarily_iff`, `law_drawn_iff`). A configuration
  that returns has a run that never loses it, going round its course back to it forever
  (`Branching.Returns.run`). So **every process necessarily draws exactly what does not return**
  (`necessarilyDrawn_iff_not_returns`, the process form of `Law.drawn_iff_not_returns`): what is
  necessarily drawn never returns (`NecessarilyDrawnInto.not_returns`), and what does not return
  is necessarily drawn into what lies ahead of it at the first step
  (`necessarilyDrawnInto_ahead`). Possibly drawn is losing oneself on some course
  (`possiblyDrawn_iff`), locked in along that course (`Invariant.locks_out`); a
  configuration possibly drawn may return on another course: `OneWay`'s `false` is possibly
  drawn into `{true}`, not necessarily, and returns (`OneWay.possibly_not_necessarily`). Under a
  determined process the moves decide whether a run is drawn in (`Determined.moves_decide`,
  `OneWay.moves_decide`).
* **Which of P67's laws hold.** The future narrows under every process: what can be had `n`
  steps on is a region the process never leaves (`reachable_invariant`), and a lost possibility
  is necessarily drawn into it (`lost_necessarily_drawn`, `necessarilyDrawn_of_lost`). Within
  finitely many configurations every run enters what returns (`Run.enters_returning`), and a
  configuration necessarily drawn at which a run begins means a merge
  (`NecessarilyDrawn.not_lossless`). They fail for processes: what returns is not a region the
  process never leaves (`Transit.returning_not_invariant`); a merge need draw neither of the two
  (`OneWay.merge_keeps`); necessarily drawn need not be lost at any step
  (`Transit.keeps_not_returns`); and possibly drawn needs no merge (`fork_lossless_not_returns`).
* **Determinacy up to likeness.** Determinacy is determinacy up to likeness where the claims
  name the configurations (`determined_iff_named`, `alike_configurations`), so each theorem with
  `Determined` is the named instance of one with `DeterminedAt`; the question is which hold for
  every claims. These do: going alike through likeness is determinacy up to likeness
  (`goesAlike_iff`, after `goAlike_id_iff`); runs alike stay alike (`DeterminedAt.stays_alike`,
  after `GoAlike.runs_agree`); what the step does not depend on is re-absorbed up to likeness
  (`DependsOnlyOnAlike.reabsorbed`, after `DependsOnlyOn.reabsorbed`); with the noise forgotten,
  the standard model is determined up to likeness exactly where the noise makes no difference up
  to likeness (`forget_inputs_determinedAt_iff`); a move taken is fixed up to likeness
  (`Run.fixesAlike_of_takes`) and one occasion stands for its class (`Run.generalizesAlike`); a
  move taken at no configuration alike to the one named is not fixed, for outcomes that differ
  in a claim (`Run.not_fixesAlike_of_untaken`), through an intervention on a whole likeness class
  (`retargetAlike`, `retargetAlike_determinedAt`). These need equality, or claims telling apart
  what equality tells apart: retargeting one of two alike configurations breaks determinacy up
  to likeness (`Twins.retarget_breaks`), so `retarget_determined` holds up to likeness only for
  the class; a kept history returns up to likeness where its present does and no claim tells
  the past apart (`keepFrame_alike_iff`, `keepHistory_returns_alike`), so `keepHistory_new` and
  `keepHistory_fixes_nothing_else` need the past claimed (`keepHistory_new_named`); with
  nothing claimed, every description carries a law and no confound is excluded
  (`carries_unregistered`, `Confound.refutes_registered`), so `carries_law_iff`,
  `Switching.no_state_law` and `Confound.varied_refutes` need the description claimed.
* **Capture's rule region.** Where the rule keeps itself, the configurations with a given rule
  are a region the law never leaves (`Law.rule_absorbing`); where the next configuration also
  depends on the rule alone, the configuration the rule holds is fixed (`Law.held_absorbing`) and
  a perturbed state is drawn into it at the first step (`Law.perturbation_drawnInto`). In `Captured`
  (P62) these are `Captured.rule_region_absorbing` and `Captured.held_absorbing`, and a perturbed
  state or a perturbed rule is drawn in and never returns (`Captured.state_perturbation_drawn`,
  `Captured.rule_perturbation_drawn`).

**Readings (the AI's, adopted on Ren's delegation of 15 October 2026, DELEGATED-CHOICES D32).**
- Where the course branches, returning asks more than keeping every possibility: a
  configuration can be had again and again from elsewhere and never come back to itself. What
  returns is what its own course can have again; the exact condition is local to the regions a
  course cannot leave.
- Possibly and necessarily drawn come apart exactly where the course is open: a configuration
  can be drawn in on one course and come back on another. What every course draws in is what
  does not return; what some course draws in is what can lose itself. Lock-in holds along every
  course that enters.
- With branching, a merge does not by itself lose a possibility and a lost possibility does not
  need a merge. R6's "losing nothing is returning" is a law of determined change within finitely
  many configurations; under every process it holds along each run.
- Likeness is the unfolding's own identity of configurations. The theorems with determinacy that
  hold up to likeness are about how configurations relate; those that need equality depend on
  what is claimed: an intervention on one name among alike configurations, a past no claim tells
  apart, a description no claim tells apart. What no claim tells apart is neither fixed nor
  excluded (compare what couples into a formation in `Becoming.Testing`).
- Capture read as attraction: perturbation of the state alone is drawn back into what the rule holds,
  and the attractor moves only with the rule.

What is not derived: a run from every configuration that can move (choosing a continuation at
each step is a choice; the laws needing a run take one as given); that every run is drawn in
within a bound; which regions actual unfoldings enter; a measure on branching courses. A
configuration from which no run begins is necessarily drawn into every region not containing it,
vacuously, as the core's runs are unending. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w u'

namespace Branching

section Courses

variable {S : Type u} {A : Type v} {P : Process S A}

/-! ## Courses of a given length -/

/-- What lies ahead of `s`, from its next step on. -/
def Ahead (P : Process S A) (s : S) : S → Prop := fun z => ∃ a t, P.step s a t ∧ Reach P t z

/-- Every configuration of `R` can be had at the next step from within `R`. -/
def FedWithin (P : Process S A) (R : S → Prop) : Prop :=
  ∀ s, R s → ∃ x a, R x ∧ P.step x a s

/-- Where every configuration returns, every possibility is kept. -/
theorem keeps_of_returns (returns : ∀ s, Returns P s) : KeepsPossibilities P :=
  fun n s => (returns s).reachable n

/-- Where every configuration can be had at the next step, every configuration can be had at
every step. -/
theorem fed_keeps (fed : ∀ s, ∃ x a, P.step x a s) : ∀ n s, Reachable P n s
  | 0, s => ⟨s, [], rfl, .nil s⟩
  | n + 1, s => match fed_keeps fed n s with
    | ⟨y, as, len, path⟩ => match fed y with
      | ⟨z, a, step⟩ => ⟨z, a :: as, congrArg Nat.succ len, .cons step path⟩

/-- A configuration that can be had one step on is had at the next step from some
configuration. -/
theorem Reachable.one {s : S} : Reachable P 1 s → ∃ x a, P.step x a s
  | ⟨_, [], len, _⟩ => nomatch len
  | ⟨x, a :: as, len, .cons step rest⟩ => match as, rest, Nat.succ.inj len with
    | [], .nil _, _ => ⟨x, a, step⟩
    | _ :: _, _, len' => nomatch len'

/-- **Keeping every possibility is being had at the next step.** Every configuration can be had
at every step exactly where every configuration can be had at the next step. -/
theorem keeps_iff_fed : KeepsPossibilities P ↔ ∀ s, ∃ x a, P.step x a s :=
  ⟨fun keeps s => (keeps 1 s).one, fed_keeps⟩

/-- A configuration returns exactly where it lies ahead of itself. -/
theorem returns_iff_ahead {s : S} : Returns P s ↔ Ahead P s s := Iff.rfl

/-- What lies ahead of a configuration is a region the process never leaves. -/
theorem invariant_ahead (P : Process S A) (s : S) : Invariant P (Ahead P s) :=
  fun _ _ _ step ⟨a, t, first, reach⟩ => ⟨a, t, first, reach.trans (Reach.of_step step)⟩

/-- **A configuration returns exactly where its own course can have it at the next step.** -/
theorem returns_iff_fed_ahead {s : S} : Returns P s ↔ ∃ x a, Reach P s x ∧ P.step x a s :=
  ⟨fun ⟨a, _, step, _, path⟩ => match trace_last path with
    | .inl same => ⟨s, a, Reach.refl P s, Eq.subst (motive := fun z => P.step s a z) same step⟩
    | .inr ⟨y, b, reach, last⟩ => ⟨y, b, (Reach.of_step step).trans reach, last⟩,
   fun ⟨x, a, ⟨as, path⟩, step⟩ =>
    have cycle : Trace P s (as ++ [a]) s := trace_append_iff.mpr ⟨x, path, .cons step (.nil s)⟩
    match as, cycle with
    | [], .cons first rest => ⟨a, _, first, _, rest⟩
    | _ :: _, .cons first rest => ⟨_, _, first, _, rest⟩⟩

/-- **Every configuration returns exactly where every region the process never leaves has each
of its configurations at the next step from within it.** -/
theorem returns_iff_fedWithin : (∀ s, Returns P s) ↔ ∀ R, Invariant P R → FedWithin P R :=
  ⟨fun returns _ invariant s inside => match returns_iff_fed_ahead.mp (returns s) with
    | ⟨x, a, reach, step⟩ => ⟨x, a, invariant.reach reach inside, step⟩,
   fun fed s =>
    match fed (Reach P s) (fun _ _ _ step reach => reach.trans (Reach.of_step step)) s
        (Reach.refl P s) with
    | ⟨x, a, reach, step⟩ => returns_iff_fed_ahead.mpr ⟨x, a, reach, step⟩⟩

/-- Every configuration of `R` can be had at every step from within `R`: `R` keeps every
possibility of its own. -/
def KeepsWithin (P : Process S A) (R : S → Prop) : Prop :=
  ∀ n s, R s → ∃ x as, R x ∧ as.length = n ∧ Trace P x as s

/-- Had at the next step from within a region, its configurations can be had at every step from
within it. -/
theorem FedWithin.keeps {R : S → Prop} (fed : FedWithin P R) : KeepsWithin P R
  | 0, s, inside => ⟨s, [], inside, rfl, .nil s⟩
  | n + 1, s, inside => match FedWithin.keeps fed n s inside with
    | ⟨y, as, inside_y, len, path⟩ => match fed y inside_y with
      | ⟨z, a, inside_z, step⟩ =>
        ⟨z, a :: as, inside_z, congrArg Nat.succ len, .cons step path⟩

/-- **A region keeps every possibility of its own exactly where it has each of its
configurations at the next step from within it.** -/
theorem keepsWithin_iff_fedWithin {R : S → Prop} : KeepsWithin P R ↔ FedWithin P R :=
  ⟨fun keeps s inside => match keeps 1 s inside with
    | ⟨_, [], _, len, _⟩ => nomatch len
    | ⟨x, a :: as, inside_x, len, .cons step rest⟩ => match as, rest, Nat.succ.inj len with
      | [], .nil _, _ => ⟨x, a, inside_x, step⟩
      | _ :: _, _, len' => (nomatch len'),
   FedWithin.keeps⟩

/-- **Every configuration returns exactly where every region the process never leaves keeps
every possibility of its own.** Keeping every possibility (`KeepsPossibilities`, the region of
all configurations) is not enough (`Transit.keeps_not_returns`). -/
theorem returns_iff_keepsWithin : (∀ s, Returns P s) ↔ ∀ R, Invariant P R → KeepsWithin P R :=
  ⟨fun returns R invariant =>
    keepsWithin_iff_fedWithin.mpr (returns_iff_fedWithin.mp returns R invariant),
   fun keeps => returns_iff_fedWithin.mpr fun R invariant =>
    keepsWithin_iff_fedWithin.mp (keeps R invariant)⟩

/-! ## Within finitely many configurations -/

end Courses
end Branching

namespace Run

variable {S : Type u} {A : Type v} {P : Process S A}

open Branching

/-- **Within finitely many configurations, every run enters what returns.** -/
theorem enters_returning (r : Run P) {l : List S}
    (held : ∀ n, r.state n ∈ l) : ∃ n, Returns P (r.state n) :=
  match revisits_within l r.state (fun n _ => held n) with
  | ⟨i, _, lt, _, same⟩ => match gap_of_lt lt with
    | ⟨d, gap⟩ =>
      ⟨i, r.act i, r.state (i + 1), r.step i,
        Eq.subst (motive := fun z => Reach P (r.state (i + 1)) z)
          ((congrArg r.state (Nat.succ_add i d)).trans
            ((congrArg r.state gap.symm).trans same.symm)) (r.reach (i + 1) d)⟩

end Run

namespace Branching
section Courses
variable {S : Type u} {A : Type v} {P : Process S A}

/-! ## A configuration that returns has a run that never loses it -/

/-- The configurations and moves along a course, by position. -/
theorem trace_positions (default : A) {x y : S} {as : List A} (path : Trace P x as y) :
    ∃ g : Nat → S, ∃ m : Nat → A, g 0 = x ∧ g as.length = y ∧
      ∀ i, i < as.length → P.step (g i) (m i) (g (i + 1)) := by
  induction path with
  | nil s =>
    exact ⟨fun _ => s, fun _ => default, rfl, rfl, fun _ lt => absurd lt (Nat.not_lt_zero _)⟩
  | @cons s _ _ a _ step _ ih =>
    match ih with
    | ⟨g, m, start, finish, steps⟩ =>
      exact ⟨fun i => match i with
          | 0 => s
          | i + 1 => g i,
        fun i => match i with
          | 0 => a
          | i + 1 => m i,
        rfl, finish, fun i lt => match i, lt with
          | 0, _ => Eq.subst (motive := fun z => P.step s a z) start.symm step
          | i + 1, lt => steps i (Nat.lt_of_succ_lt_succ lt)⟩

/-- Along a course by position, every position leads to the last. -/
theorem positions_reach {g : Nat → S} {m : Nat → A} {L : Nat}
    (steps : ∀ i, i < L → P.step (g i) (m i) (g (i + 1))) :
    ∀ d i, i + d = L → Reach P (g i) (g L)
  | 0, i, same => Eq.subst (motive := fun k => Reach P (g i) (g k)) same (Reach.refl P (g i))
  | d + 1, i, same =>
    (Reach.of_step (steps i (Nat.lt_of_lt_of_le (Nat.lt_succ_of_le (Nat.le_add_right i d))
      (Nat.le_of_eq same)))).trans
      (positions_reach steps d (i + 1) ((Nat.succ_add i d).trans same))

/-- The position after `n` steps going round positions `0` to `p`, from the last back to the
first. -/
def lap (p : Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => cond (Nat.ble (lap p n + 1) p) (lap p n + 1) 0

theorem lap_succ (p n : Nat) :
    (lap p n + 1 ≤ p ∧ lap p (n + 1) = lap p n + 1) ∨
      (¬ lap p n + 1 ≤ p ∧ lap p (n + 1) = 0) :=
  match h : Nat.ble (lap p n + 1) p with
  | true => .inl ⟨Nat.le_of_ble_eq_true h, (congrArg (fun b => cond b (lap p n + 1) 0) h : _)⟩
  | false =>
    .inr ⟨fun le => Bool.noConfusion ((Nat.ble_eq_true_of_le le).symm.trans h),
      (congrArg (fun b => cond b (lap p n + 1) 0) h : _)⟩

theorem lap_le (p : Nat) : ∀ n, lap p n ≤ p
  | 0 => Nat.zero_le p
  | n + 1 => match lap_succ p n with
    | .inl ⟨le, same⟩ => Eq.subst (motive := fun k => k ≤ p) same.symm le
    | .inr ⟨_, same⟩ => Eq.subst (motive := fun k => k ≤ p) same.symm (Nat.zero_le p)

/-- **A configuration that returns has a run that never loses it.** Going round a course back
to it forever, the run begins at it and every configuration of the run leads back to it. -/
theorem Returns.run {s : S} (returns : Returns P s) :
    ∃ r : Run P, r.state 0 = s ∧ ∀ n, Reach P (r.state n) s :=
  match returns with
  | ⟨a, _, first, as, path⟩ =>
    match trace_positions a (Trace.cons first path) with
    | ⟨g, m, start, finish, steps⟩ =>
      have closes : g (as.length + 1) = g 0 := finish.trans start.symm
      ⟨⟨fun n => g (lap as.length n), fun n => m (lap as.length n), fun n =>
          match lap_succ as.length n with
          | .inl ⟨le, same⟩ =>
            Eq.subst (motive := fun k => P.step (g (lap as.length n)) (m (lap as.length n)) (g k))
              same.symm (steps _ (Nat.lt_succ_of_lt le))
          | .inr ⟨over, same⟩ =>
            have at_end : lap as.length n = as.length :=
              Nat.le_antisymm (lap_le as.length n)
                (match Nat.lt_or_ge (lap as.length n) as.length with
                  | .inl lt => absurd lt over
                  | .inr ge => ge)
            Eq.subst (motive := fun k => P.step (g k) (m k) (g (lap as.length (n + 1))))
              at_end.symm
              (Eq.subst (motive := fun k => P.step (g as.length) (m as.length) (g k))
                same.symm
                (Eq.subst (motive := fun z => P.step (g as.length) (m as.length) z) closes
                  (steps as.length (Nat.lt_succ_self _))))⟩,
        start, fun n =>
          match le_dest (lap_le as.length n) with
          | ⟨e, gap⟩ =>
            Eq.subst (motive := fun z => Reach P (g (lap as.length n)) z) finish
              (positions_reach steps (e + 1) (lap as.length n)
                (congrArg Nat.succ gap.symm))⟩

/-! ## Possibly and necessarily drawn -/

/-- `s` is possibly drawn into `R`: it lies outside `R` and some course from it enters `R`. -/
def PossiblyDrawnInto (P : Process S A) (R : S → Prop) (s : S) : Prop :=
  ¬ R s ∧ ∃ t, Reach P s t ∧ R t

/-- `s` is necessarily drawn into `R`: it lies outside `R` and every run from it enters `R`. -/
def NecessarilyDrawnInto (P : Process S A) (R : S → Prop) (s : S) : Prop :=
  ¬ R s ∧ ∀ r : Run P, r.state 0 = s → ∃ n, R (r.state n)

/-- `s` is possibly drawn: some region the process never leaves possibly draws it in. -/
def PossiblyDrawn (P : Process S A) (s : S) : Prop :=
  ∃ R : S → Prop, Invariant P R ∧ PossiblyDrawnInto P R s

/-- `s` is necessarily drawn: some region the process never leaves necessarily draws it in. -/
def NecessarilyDrawn (P : Process S A) (s : S) : Prop :=
  ∃ R : S → Prop, Invariant P R ∧ NecessarilyDrawnInto P R s

end Courses
end Branching

namespace Run

variable {S : Type u} {A : Type v} {P : Process S A}

open Branching

/-- A run from `s` that enters `R` makes `s` possibly drawn into `R`. -/
theorem possiblyDrawnInto {R : S → Prop} (r : Run P)
    (outside : ¬ R (r.state 0)) {n : Nat} (inside : R (r.state n)) :
    PossiblyDrawnInto P R (r.state 0) :=
  ⟨outside, r.state n, Eq.subst (motive := fun k => Reach P (r.state 0) (r.state k))
    (Nat.zero_add n) (r.reach 0 n), inside⟩

end Run

namespace Branching
section Courses
variable {S : Type u} {A : Type v} {P : Process S A}

/-- Necessarily drawn, with a run from it, a configuration is possibly drawn. -/
theorem NecessarilyDrawnInto.possibly {R : S → Prop} {s : S}
    (drawn : NecessarilyDrawnInto P R s) (r : Run P) (start : r.state 0 = s) :
    PossiblyDrawnInto P R s :=
  match drawn.2 r start with
  | ⟨_, inside⟩ => start ▸ r.possiblyDrawnInto (start ▸ drawn.1) inside

/-- **Possibly drawn is losing oneself on some course.** A configuration is possibly drawn into
some region the process never leaves exactly where some course from it leads where it cannot be
had again. -/
theorem possiblyDrawn_iff {s : S} : PossiblyDrawn P s ↔ ∃ t, Reach P s t ∧ ¬ Reach P t s :=
  ⟨fun ⟨_, invariant, outside, t, reach, inside⟩ =>
    ⟨t, reach, invariant.locks_out inside outside⟩,
   fun ⟨t, reach, lost⟩ =>
    ⟨Reach P t, fun _ _ _ step r => r.trans (Reach.of_step step), lost, t, reach,
      Reach.refl P t⟩⟩

/-- **What does not return is necessarily drawn into what lies ahead of it**, every run entering
at its first step. -/
theorem necessarilyDrawnInto_ahead {s : S} (never : ¬ Returns P s) :
    NecessarilyDrawnInto P (Ahead P s) s :=
  ⟨never, fun r start => ⟨1, r.act 0, r.state 1,
    Eq.subst (motive := fun z => P.step z (r.act 0) (r.state 1)) start (r.step 0),
    Reach.refl P _⟩⟩

/-- **What is necessarily drawn never returns.** -/
theorem NecessarilyDrawnInto.not_returns {R : S → Prop} (invariant : Invariant P R) {s : S}
    (drawn : NecessarilyDrawnInto P R s) : ¬ Returns P s :=
  fun returns => match returns.run with
  | ⟨r, start, back⟩ => match drawn.2 r start with
    | ⟨n, inside⟩ => drawn.1 (invariant.reach (back n) inside)

/-- **Every process necessarily draws exactly what does not return**, with no premise: the
form for every process of `Law.drawn_iff_not_returns`. -/
theorem necessarilyDrawn_iff_not_returns {s : S} : NecessarilyDrawn P s ↔ ¬ Returns P s :=
  ⟨fun ⟨_, invariant, drawn⟩ => drawn.not_returns invariant,
   fun never => ⟨Ahead P s, invariant_ahead P s, necessarilyDrawnInto_ahead never⟩⟩

/-- What does not return and can move is possibly drawn into what lies ahead of it. -/
theorem possiblyDrawnInto_ahead {s : S} (never : ¬ Returns P s) {a : A} {t : S}
    (step : P.step s a t) : PossiblyDrawnInto P (Ahead P s) s :=
  ⟨never, t, Reach.of_step step, a, t, step, Reach.refl P t⟩

/-! ## The future narrows -/

theorem length_append_one (a : A) : ∀ as : List A, (as ++ [a]).length = as.length + 1
  | [] => rfl
  | _ :: as => congrArg Nat.succ (length_append_one a as)

/-- **What can be had `n` steps on is a region the process never leaves.** -/
theorem reachable_invariant (P : Process S A) (n : Nat) : Invariant P (Reachable P n) :=
  fun _ a t step ⟨x, as, len, path⟩ =>
    Reachable.earlier ⟨x, as ++ [a], (length_append_one a as).trans (congrArg Nat.succ len),
      trace_append_iff.mpr ⟨_, path, .cons step (.nil t)⟩⟩

end Courses
end Branching

namespace Run

variable {S : Type u} {A : Type v} {P : Process S A}

open Branching

theorem window_length (r : Run P) : ∀ k m, (r.window m k).length = k
  | 0, _ => rfl
  | k + 1, m => congrArg Nat.succ (Run.window_length r k (m + 1))

end Run

namespace Branching
section Courses
variable {S : Type u} {A : Type v} {P : Process S A}

/-- **A lost possibility is necessarily drawn in.** A configuration that cannot be had `n`
steps on is necessarily drawn into what can be had `n` steps on, every run entering at step
`n`. -/
theorem lost_necessarily_drawn {n : Nat} {s : S} (lost : ¬ Reachable P n s) :
    NecessarilyDrawnInto P (Reachable P n) s :=
  ⟨lost, fun r _ => ⟨n, r.state 0, r.window 0 n, r.window_length n 0,
    Eq.subst (motive := fun k => Trace P (r.state 0) (r.window 0 n) (r.state k))
      (Nat.zero_add n) (r.window_trace n 0)⟩⟩

/-- A configuration lost at some step is necessarily drawn. -/
theorem necessarilyDrawn_of_lost {n : Nat} {s : S} (lost : ¬ Reachable P n s) :
    NecessarilyDrawn P s :=
  ⟨Reachable P n, reachable_invariant P n, lost_necessarily_drawn lost⟩

/-- **Within finitely many configurations, what is necessarily drawn with a run means a
merge.** -/
theorem NecessarilyDrawn.not_lossless {s : S} (drawn : NecessarilyDrawn P s) {all : List S}
    (every : ∀ x, x ∈ all) (r : Run P) (start : r.state 0 = s) : ¬ Lossless P :=
  fun lossless => (necessarilyDrawn_iff_not_returns.mp drawn) (start ▸ lossless.returns every r)

/-! ## Under a determined process, the moves decide -/

/-- **Under a determined process, whether a run is drawn in is decided by its moves.** Two runs
from one configuration of a determined process, one entering a region and the other never,
differ in some move. -/
theorem Determined.moves_decide (determined : Determined P) (r r' : Run P)
    (start : r.state 0 = r'.state 0) {R : S → Prop} (enters : ∃ n, R (r.state n))
    (never : ∀ n, ¬ R (r'.state n)) : ¬ ∀ n, r.act n = r'.act n :=
  fun moves => match enters with
  | ⟨n, inside⟩ =>
    never n (Eq.subst (motive := R)
      (GoAlike.runs_agree (π := id) (goAlike_id_iff.mpr determined) r r' moves start n) inside)

/-- **Under a determined process, runs that meet stay together while they take the same
moves**: configurations merged stay merged. -/
theorem Determined.stays_merged (determined : Determined P) (r r' : Run P) {n : Nat}
    (meet : r.state n = r'.state n) (moves : ∀ k, r.act (n + k) = r'.act (n + k)) :
    ∀ k, r.state (n + k) = r'.state (n + k) :=
  GoAlike.runs_agree (π := id) (goAlike_id_iff.mpr determined) (r.onward n) (r'.onward n) moves
    meet

end Courses

/-! ## Determined laws are the instance

R6's notions are these at `Law.process next` by definition, so each bridge is `Iff.rfl`. -/

section Laws

variable {S : Type u}

/-- Under a determined law, what can be had `n` steps on is R6's. -/
theorem law_reachable_iff {next : S → S} {n : Nat} {s : S} :
    Reachable (Law.process next) n s ↔ Law.Reachable next n s :=
  Iff.rfl

theorem law_keeps_iff {next : S → S} :
    KeepsPossibilities (Law.process next) ↔ Law.KeepsPossibilities next :=
  Iff.rfl

/-- Under a determined law, returning is R6's. -/
theorem law_returns_iff {next : S → S} {s : S} :
    Returns (Law.process next) s ↔ Law.Returns next s :=
  Iff.rfl

/-- Under a determined law, merging nothing is R6's. -/
theorem law_lossless_iff {next : S → S} : Lossless (Law.process next) ↔ Law.Lossless next :=
  Iff.rfl

theorem law_merges_iff {next : S → S} : Merges (Law.process next) ↔ Law.Merges next :=
  Iff.rfl

/-- A run of a determined law is its orbit. -/
theorem law_run_state {next : S → S} (r : Run (Law.process next)) :
    ∀ n, r.state n = Law.orbit next (r.state 0) n
  | 0 => rfl
  | n + 1 => (r.step n).trans (congrArg next (law_run_state r n))

/-- **Under a determined law, possibly drawn is drawn.** -/
theorem law_possibly_iff {next : S → S} {R : S → Prop} {s : S} :
    PossiblyDrawnInto (Law.process next) R s ↔ Law.DrawnInto next R s :=
  ⟨fun ⟨outside, _, reach, inside⟩ => match law_reach_iff.mp reach with
    | ⟨n, to⟩ => ⟨outside, n, Eq.subst (motive := R) to.symm inside⟩,
   fun ⟨outside, n, inside⟩ => ⟨outside, _, law_reach_iff.mpr ⟨n, rfl⟩, inside⟩⟩

/-- **Under a determined law, necessarily drawn is drawn.** -/
theorem law_necessarily_iff {next : S → S} {R : S → Prop} {s : S} :
    NecessarilyDrawnInto (Law.process next) R s ↔ Law.DrawnInto next R s :=
  ⟨fun ⟨outside, every⟩ => ⟨outside, every (Law.run next s) rfl⟩,
   fun ⟨outside, n, inside⟩ => ⟨outside, fun r start => ⟨n,
     Eq.subst (motive := R) ((congrArg (fun z => Law.orbit next z n) start.symm).trans
       (law_run_state r n).symm) inside⟩⟩⟩

/-- Under a determined law, necessarily drawn is P67's drawn. -/
theorem law_drawn_iff {next : S → S} {s : S} :
    NecessarilyDrawn (Law.process next) s ↔ Law.Drawn next s :=
  ⟨fun ⟨R, invariant, drawn⟩ =>
    ⟨R, Law.absorbing_iff_invariant.mpr invariant, law_necessarily_iff.mp drawn⟩,
   fun ⟨R, absorbing, drawn⟩ =>
    ⟨R, Law.absorbing_iff_invariant.mp absorbing, law_necessarily_iff.mpr drawn⟩⟩

end Laws

/-! ## A one-way passage

A configuration is a bit and a move is a bit: the move `false` keeps the configuration, the
move `true` passes from `false` to `true`, and from `true` every move stays. -/

namespace OneWay

/-- From `s` by `a` to `s || a`. -/
def process : Process Bool Bool := ⟨fun s a t => t = (s || a)⟩

theorem determined : Determined process := fun _ _ _ _ step step' => step.trans step'.symm

/-- Every configuration returns. -/
theorem returns : ∀ s, Returns process s
  | false => ⟨false, false, rfl, Reach.refl _ _⟩
  | true => ⟨false, true, rfl, Reach.refl _ _⟩

/-- `false` and `true` go to one configuration. -/
theorem merges : Merges process :=
  ⟨false, true, true, false, true, fun same => Bool.noConfusion same, rfl, rfl⟩

/-- The region `{true}`. -/
def atTrue (s : Bool) : Prop := s = true

theorem atTrue_invariant : Invariant process atTrue :=
  fun _ a _ step inside =>
    step.trans (Eq.subst (motive := fun z => (z || a) = true) inside.symm rfl)

/-- The run that keeps `false`. -/
def staying : Run process := ⟨fun _ => false, fun _ => false, fun _ => rfl⟩

/-- The configurations of the run that passes: `false`, then `true`. -/
def passed : Nat → Bool
  | 0 => false
  | _ + 1 => true

/-- The run that passes at once. -/
def passing : Run process :=
  ⟨passed, fun _ => true, fun n => match n with
    | 0 => rfl
    | _ + 1 => rfl⟩

/-- **Possibly drawn, not necessarily, and returning.** `false` is possibly drawn into `{true}`,
which the process never leaves; the run that keeps `false` is never drawn in, and `false`
returns. -/
theorem possibly_not_necessarily :
    PossiblyDrawnInto process atTrue false ∧ ¬ NecessarilyDrawnInto process atTrue false ∧
      Returns process false :=
  ⟨passing.possiblyDrawnInto (n := 1) (fun same => Bool.noConfusion same) rfl,
   fun ⟨_, every⟩ => match every staying rfl with
    | ⟨_, inside⟩ => Bool.noConfusion inside,
   returns false⟩

/-- **A merge with every configuration returning and no possibility lost.** Within two
configurations, the process merges `false` and `true`, both return, and every configuration can
be had at every step: R6's `Law.Merges.loses` and P67's `Law.Merges.not_both_return` need a
determined law. -/
theorem merge_keeps :
    Merges process ∧ Returns process false ∧ Returns process true ∧
      KeepsPossibilities process ∧ ∀ s, s ∈ [false, true] :=
  ⟨merges, returns false, returns true, keeps_of_returns returns, fun s => match s with
    | false => .head _
    | true => .tail _ (.head _)⟩

/-- **The moves decide.** From `false`, the determined process has a run drawn into `{true}` and
a run never drawn in, and they differ in a move. -/
theorem moves_decide : ¬ ∀ n, passing.act n = staying.act n :=
  Determined.moves_decide determined passing staying rfl ⟨1, rfl⟩
    (fun _ inside => Bool.noConfusion inside)

end OneWay

/-! ## A passage

From `before` the move `false` stays and the move `true` passes to `between`; from `between`
every move goes on to `after`, and from `after` every move stays. -/

namespace Transit

/-- Three stages of a passage. -/
inductive Stage where
  | before
  | between
  | after

/-- The stage after a move. -/
def move : Stage → Bool → Stage
  | .before, false => .before
  | .before, true => .between
  | .between, _ => .after
  | .after, _ => .after

/-- From `s` by `a` to `move s a`. -/
def process : Process Stage Bool := ⟨fun s a t => t = move s a⟩

theorem determined : Determined process := fun _ _ _ _ step step' => step.trans step'.symm

/-- The three stages are all the configurations. -/
theorem every : ∀ s, s ∈ [Stage.before, .between, .after]
  | .before => .head _
  | .between => .tail _ (.head _)
  | .after => .tail _ (.tail _ (.head _))

/-- Every stage can move. -/
theorem total : ∀ s, ∃ a t, process.step s a t := fun s => ⟨false, move s false, rfl⟩

/-- Every stage can be had at the next step. -/
theorem fed : ∀ s, ∃ x a, process.step x a s
  | .before => ⟨.before, false, rfl⟩
  | .between => ⟨.before, true, rfl⟩
  | .after => ⟨.between, false, rfl⟩

/-- The region `{after}`. -/
def atAfter (s : Stage) : Prop := s = .after

theorem atAfter_invariant : Invariant process atAfter :=
  fun _ a _ step inside =>
    step.trans (Eq.subst (motive := fun z => move z a = .after) inside.symm rfl)

/-- `between` never returns. -/
theorem between_never : ¬ Returns process .between :=
  fun ⟨_, _, step, reach⟩ =>
    atAfter_invariant.locks_out (R := atAfter) step (fun same => Stage.noConfusion same) reach

/-- `before` returns. -/
theorem before_returns : Returns process .before := ⟨false, .before, rfl, Reach.refl _ _⟩

/-- **Every possibility kept, and a configuration that never returns.** Within three
configurations, every one of which can move, every configuration can be had at every step, yet
`between` never returns: it is necessarily drawn into `{after}`, entering at the first step, and
is never lost. So for processes, keeping every possibility does not give returning (R6's
`Law.returns_iff_keeps`), and P67's `Law.drawn_iff_lost` and `Law.returns_iff_always_reachable`
hold one way only. -/
theorem keeps_not_returns :
    (∀ s, s ∈ [Stage.before, .between, .after]) ∧ (∀ s, ∃ a t, process.step s a t) ∧
      KeepsPossibilities process ∧ ¬ Returns process .between ∧
        NecessarilyDrawnInto process atAfter .between :=
  ⟨every, total, keeps_iff_fed.mpr fed, between_never,
   fun same => Stage.noConfusion same, fun r start => ⟨1,
     (r.step 0).trans (congrArg (fun z => move z (r.act 0)) start)⟩⟩

/-- **What returns is not a region the process never leaves.** `before` returns and moves to
`between`, which does not: P67's `Law.returning_absorbing` needs a determined law. -/
theorem returning_not_invariant : ¬ Invariant process (Returns process) :=
  fun invariant => between_never (invariant .before true .between rfl before_returns)

end Transit

/-! ## The fork merges nothing and does not return -/

end Branching

namespace Reach

/-- A configuration with no step leads only to itself. -/
theorem of_dead_end {S : Type u} {A : Type v} {P : Process S A} {t u : S}
    (dead : ∀ a v, ¬ P.step t a v) : Reach P t u → t = u :=
  fun ⟨as, path⟩ => match as, path with
  | [], .nil _ => rfl
  | _ :: _, .cons step _ => absurd step (dead _ _)

end Reach

namespace Branching

/-- Every step of the fork leaves the origin. -/
theorem fork_source {s : Fork.Pos} {a : Fork.Way} {t : Fork.Pos} :
    Fork.Steps s a t → s = .origin
  | .toLeft => rfl
  | .toRight => rfl

/-- No step of the fork enters the origin. -/
theorem fork_target {s : Fork.Pos} {a : Fork.Way} {t : Fork.Pos} :
    Fork.Steps s a t → t ≠ .origin
  | .toLeft => fun same => nomatch same
  | .toRight => fun same => nomatch same

/-- The fork merges nothing. -/
theorem fork_lossless : Lossless Fork.law :=
  fun _ _ _ _ _ step step' => match (step : Fork.Steps _ _ _), (step' : Fork.Steps _ _ _) with
  | .toLeft, .toLeft => rfl
  | .toRight, .toRight => rfl

/-- The fork's origin never returns. -/
theorem fork_origin_never : ¬ Returns Fork.law .origin :=
  fun ⟨_, _, step, reach⟩ =>
    fork_target step (Reach.of_dead_end
      (fun _ _ step' => fork_target step (fork_source step')) reach)

/-- `{left}` is a region the fork never leaves. -/
theorem fork_left_invariant : Invariant Fork.law (fun s => s = .left) :=
  fun _ _ _ step inside =>
    absurd (inside.symm.trans (fork_source step)) (fun same => nomatch same)

/-- **Merging nothing within finitely many configurations, without a run, a configuration need
not return.** The fork (`Fork` of `Becoming.Unfolding`) merges nothing, has three
configurations, and its origin never returns and is possibly drawn into `{left}`: the run in
`Lossless.returns` is needed, and possibly drawn does not need a merge. -/
theorem fork_lossless_not_returns :
    Lossless Fork.law ∧ (∀ s, s ∈ [Fork.Pos.origin, .left, .right]) ∧
      ¬ Returns Fork.law .origin ∧ PossiblyDrawn Fork.law .origin :=
  ⟨fork_lossless, fun s => match s with
    | .origin => .head _
    | .left => .tail _ (.head _)
    | .right => .tail _ (.tail _ (.head _)),
   fork_origin_never,
   ⟨fun s => s = .left, fork_left_invariant,
    ⟨fun same => (nomatch same), Fork.Pos.left, Reach.of_step Fork.Steps.toLeft, rfl⟩⟩⟩

end Branching


/-! ## Determinacy up to likeness -/

section Likeness

variable {S : Type u} {A : Type v} {C : Type w}

/-- **Equality is likeness where the claims name the configurations.** -/
theorem alike_configurations {S : Type} {P : Process S A} {s s' : S}
    (alike : Alike (Frame.configurations P) (Frame.configurations P) s s') : s = s' :=
  ((alike.realized s).mp rfl).symm

/-- **Determinacy is determinacy up to likeness where the claims name the configurations.**
Every theorem stated with `Determined` is the instance, with configurations named, of one
stated with `DeterminedAt`. -/
theorem determined_iff_named {S : Type} {P : Process S A} :
    Determined P ↔ ∀ s, DeterminedAt (Frame.configurations P) s :=
  ⟨fun determined => Determined.at (F := Frame.configurations P) determined,
   fun determined s a t t' step step' => alike_configurations (determined s a t t' step step')⟩

/-- Configurations alike go alike in the frame: the same move takes alike configurations to
alike ones. -/
def GoesAlike (F : Frame S A C) : Prop :=
  ∀ s s' a t t', Alike F F s s' → F.P.step s a t → F.P.step s' a t' → Alike F F t t'

/-- **Through likeness, going alike is determinacy up to likeness**, as through the identity
going alike is determinacy (`goAlike_id_iff`). -/
theorem goesAlike_iff {F : Frame S A C} : GoesAlike F ↔ ∀ s, DeterminedAt F s :=
  ⟨fun alike s a t t' step step' => alike s s a t t' (Alike.refl F s) step step',
   fun determined _ s' _ _ _ alike step step' =>
    DeterminedAt.goAlike alike (determined s') step step'⟩

/-- **Runs alike stay alike.** Where the frame is determined up to likeness, two runs taking the
same moves from alike configurations are alike at every later step: `GoAlike.runs_agree` and
`Determined.stays_merged` up to likeness. -/
theorem DeterminedAt.stays_alike {F : Frame S A C} (determined : ∀ s, DeterminedAt F s)
    (r r' : Run F.P) {n : Nat} (meet : Alike F F (r.state n) (r'.state n))
    (moves : ∀ k, r.act (n + k) = r'.act (n + k)) :
    ∀ k, Alike F F (r.state (n + k)) (r'.state (n + k))
  | 0 => meet
  | k + 1 =>
    DeterminedAt.goAlike (DeterminedAt.stays_alike determined r r' meet moves k) (determined _)
      (r.step (n + k))
      (Eq.subst (motive := fun a => F.P.step (r'.state (n + k)) a (r'.state (n + k + 1)))
        (moves k).symm (r'.step (n + k)))

/-- Up to likeness, the next configuration depends only on `π`: wherever two configurations
project alike, the same move takes them to alike configurations. -/
def DependsOnlyOnAlike {K : Type u'} (F : Frame S A C) (π : S → K) : Prop :=
  ∀ s s' a u u', π s = π s' → F.P.step s a u → F.P.step s' a u' → Alike F F u u'

/-- Depending only on `π` up to likeness, the frame is determined up to likeness. -/
theorem DependsOnlyOnAlike.determinedAt {K : Type u'} {F : Frame S A C} {π : S → K}
    (only : DependsOnlyOnAlike F π) : ∀ s, DeterminedAt F s :=
  fun s a u u' step step' => only s s a u u' rfl step step'

/-- Depending only on `π`, up to likeness for every claims. -/
theorem DependsOnlyOn.alike {K : Type u'} {F : Frame S A C} {π : S → K}
    (only : DependsOnlyOn F.P π) : DependsOnlyOnAlike F π :=
  fun s s' a u u' same step step' =>
    Eq.subst (motive := fun z => Alike F F u z) (only s s' a u u' same step step') (Alike.refl F u)

/-- **What the step does not depend on is re-absorbed in one step, up to likeness**:
`DependsOnlyOn.reabsorbed` of `Becoming.Mechanism` with the conclusion read up to likeness. -/
theorem DependsOnlyOnAlike.reabsorbed {K : Type u'} {F : Frame S A C} {π : S → K}
    (only : DependsOnlyOnAlike F π) (r r' : Run F.P) (moves : ∀ n, r.act n = r'.act n)
    (start : π (r.state 0) = π (r'.state 0)) (n : Nat) :
    Alike F F (r.state (n + 1)) (r'.state (n + 1)) :=
  have first : Alike F F (r.state 1) (r'.state 1) :=
    only _ _ _ _ _ start (r.step 0)
      (Eq.subst (motive := fun a => F.P.step (r'.state 0) a (r'.state 1)) (moves 0).symm
        (r'.step 0))
  Eq.subst (motive := fun k => Alike F F (r.state k) (r'.state k)) (Nat.add_comm 1 n)
    (DeterminedAt.stays_alike only.determinedAt r r' first (fun k => moves (1 + k)) n)

/-- **Noise is a move not represented, up to likeness.** With the noise forgotten, the standard
model is determined up to likeness exactly where the noise makes no difference up to likeness:
`forget_inputs_determined_iff` of `Becoming.Mechanism` with its equality read as likeness. -/
theorem forget_inputs_determinedAt_iff {X : Type u} {U : Type v} {E : Type w} {D : Type u'}
    {F : X → U → E → X} {claims : X → D → Prop} :
    (∀ x, DeterminedAt (⟨forget (inputs F), claims⟩ : Frame X U D) x) ↔
      ∀ x u e e', Alike (⟨forget (inputs F), claims⟩ : Frame X U D)
        ⟨forget (inputs F), claims⟩ (F x u e) (F x u e') :=
  ⟨fun determined x u e e' => determined x u _ _ ⟨e, rfl⟩ ⟨e', rfl⟩,
   fun every x u t _ ⟨e, step⟩ ⟨e', step'⟩ =>
    Eq.subst (motive := fun z => Alike (⟨forget (inputs F), claims⟩ : Frame X U D)
        ⟨forget (inputs F), claims⟩ t z) step'.symm
      (Eq.subst (motive := fun z => Alike (⟨forget (inputs F), claims⟩ : Frame X U D)
        ⟨forget (inputs F), claims⟩ z (F x u e')) step.symm (every x u e e'))⟩

/-! ### What the record fixes, up to likeness -/

namespace Run

variable {P : Process S A}

/-- Up to likeness under `claims`, the record up to step `t` fixes the outcome of `a` at `s` to
`u`: every process admitting each step of the run before `t` and determined up to likeness at
`s` under those claims sends `a` at `s` to configurations alike to `u`. -/
def FixesAlike (r : Run P) (claims : S → C → Prop) (t : Nat) (s : S) (a : A) (u : S) : Prop :=
  ∀ Q : Process S A, DeterminedAt (⟨Q, claims⟩ : Frame S A C) s → r.StepsOf Q t →
    ∀ u', Q.step s a u' → Alike (⟨Q, claims⟩ : Frame S A C) ⟨Q, claims⟩ u' u

/-- **A move taken is fixed up to likeness**: `Run.fixes_of_takes` up to likeness. -/
theorem fixesAlike_of_takes (r : Run P) (claims : S → C → Prop) {n t : Nat} (before : n < t) :
    r.FixesAlike claims t (r.state n) (r.act n) (r.state (n + 1)) :=
  fun _ determined steps _ step => determined _ _ _ step (steps n before)

/-- Before step `t` the run takes `a` at a configuration alike in `F` to `s`. -/
def TakesAlike (F : Frame S A C) (r : Run P) (t : Nat) (s : S) (a : A) : Prop :=
  ∃ n, n < t ∧ Alike F F (r.state n) s ∧ r.act n = a

end Run

/-- The frame with move `b` sent to `u₀` at every configuration alike to `s`, and every other step
as in `F`: an intervention on a whole likeness class. -/
def retargetAlike (F : Frame S A C) (s : S) (b : A) (u₀ : S) : Frame S A C :=
  ⟨⟨fun x a u =>
      (¬ (Alike F F x s ∧ a = b) ∧ F.P.step x a u) ∨
        (Alike F F x s ∧ a = b ∧ u = u₀)⟩,
    F.realized⟩

/-- Likeness in `F` is a bisimulation of the frame retargeted on a likeness class. -/
theorem retargetAlike_bisimulation (F : Frame S A C) (s : S) (b : A) (u₀ : S) :
    Bisimulation (retargetAlike F s b u₀) (retargetAlike F s b u₀) (Alike F F) :=
  fun _ _ alike =>
    ⟨alike.realized,
     fun _ _ step => match step with
       | .inl ⟨other, step⟩ => match alike.step step with
         | ⟨u', step', joined⟩ =>
           ⟨u', .inl ⟨fun ⟨like, same⟩ => other ⟨alike.trans like, same⟩, step'⟩,
             joined⟩
       | .inr ⟨like, same, to⟩ =>
         ⟨u₀, .inr ⟨alike.symm.trans like, same, rfl⟩,
          Eq.subst (motive := fun z => Alike F F z u₀) to.symm (Alike.refl F u₀)⟩,
     fun _ _ step => match step with
       | .inl ⟨other, step⟩ => match alike.symm.step step with
         | ⟨u, step', joined⟩ =>
           ⟨u, .inl ⟨fun ⟨like, same⟩ => other ⟨alike.symm.trans like, same⟩, step'⟩,
             joined.symm⟩
       | .inr ⟨like, same, to⟩ =>
         ⟨u₀, .inr ⟨alike.trans like, same, rfl⟩,
          Eq.subst (motive := fun z => Alike F F u₀ z) to.symm (Alike.refl F u₀)⟩⟩

/-- **Retargeting a likeness class keeps determinacy up to likeness**: `retarget_determined` up
to likeness, where the intervention acts on every configuration alike to the one it names. -/
theorem retargetAlike_determinedAt {F : Frame S A C} (determined : ∀ x, DeterminedAt F x)
    (s : S) (b : A) (u₀ : S) : ∀ x, DeterminedAt (retargetAlike F s b u₀) x :=
  fun x a u u' step step' => ⟨Alike F F, retargetAlike_bisimulation F s b u₀,
    match step, step' with
    | .inl ⟨_, step⟩, .inl ⟨_, step'⟩ => determined x a u u' step step'
    | .inl ⟨other, _⟩, .inr ⟨like, same, _⟩ => absurd ⟨like, same⟩ other
    | .inr ⟨like, same, _⟩, .inl ⟨other, _⟩ => absurd ⟨like, same⟩ other
    | .inr ⟨_, _, to⟩, .inr ⟨_, _, to'⟩ =>
      Eq.subst (motive := fun z => Alike F F z u') (to.trans to'.symm).symm (Alike.refl F u')⟩

/-- The frame retargeted on a likeness class sends the move there. -/
theorem retargetAlike_step (F : Frame S A C) (s : S) (b : A) (u₀ : S) :
    (retargetAlike F s b u₀).P.step s b u₀ :=
  .inr ⟨Alike.refl F s, rfl, rfl⟩

/-- **A move not taken is not fixed, up to likeness.** Where the frame is determined up to
likeness and the run has not taken `b` at any configuration alike to `s` before `t`, the record
up to `t` fixes no outcome of `b` at `s` up to likeness, for any two configurations that differ in
a claim: `Run.not_fixes_of_untaken` up to likeness. -/
theorem Run.not_fixesAlike_of_untaken {F : Frame S A C} (determined : ∀ x, DeterminedAt F x)
    (r : Run F.P) {t : Nat} {s : S} {b : A} (untaken : ¬ r.TakesAlike F t s b) {x y : S} {c : C}
    (here : F.realized x c) (not_here : ¬ F.realized y c) :
    ¬ ∃ u, r.FixesAlike F.realized t s b u :=
  fun ⟨_, fixes⟩ =>
    have steps : ∀ u₀, r.StepsOf (retargetAlike F s b u₀).P t := fun _ n before =>
      .inl ⟨fun ⟨like, same⟩ => untaken ⟨n, before, like, same⟩, r.step n⟩
    have to_x := fixes (retargetAlike F s b x).P (retargetAlike_determinedAt determined s b x s)
      (steps x) x (retargetAlike_step F s b x)
    have to_y := fixes (retargetAlike F s b y).P (retargetAlike_determinedAt determined s b y s)
      (steps y) y (retargetAlike_step F s b y)
    not_here ((to_y.realized c).mpr ((to_x.realized c).mp here))

/-! ### A kept history, up to likeness -/

/-- A process with its history kept, read through what is realized at its present. -/
def keepFrame (F : Frame S A C) : Frame (S × List (S × A)) A C :=
  ⟨keepHistory F.P, fun h c => F.realized h.1 c⟩

/-- Alike presents make alike kept configurations. -/
theorem keepFrame_bisimulation (F : Frame S A C) :
    Bisimulation (keepFrame F) (keepFrame F) fun h h' => Alike F F h.1 h'.1 :=
  fun h h' alike => ⟨alike.realized,
    fun a _ ⟨step, _⟩ => match alike.step step with
      | ⟨t', step', joined⟩ => ⟨(t', (h'.1, a) :: h'.2), ⟨step', rfl⟩, joined⟩,
    fun a _ ⟨step, _⟩ => match alike.symm.step step with
      | ⟨t, step', joined⟩ => ⟨(t, (h.1, a) :: h.2), ⟨step', rfl⟩, joined.symm⟩⟩

/-- Alike kept configurations have alike presents. -/
theorem keepFrame_present (F : Frame S A C) :
    Bisimulation F F fun x y => ∃ p p', Alike (keepFrame F) (keepFrame F) (x, p) (y, p') :=
  fun x y ⟨p, p', alike⟩ => ⟨alike.realized,
    fun a t step => match alike.step (a := a) (t := (t, (x, a) :: p)) ⟨step, rfl⟩ with
      | ⟨u', ⟨step', _⟩, joined⟩ => ⟨u'.1, step', (x, a) :: p, u'.2, joined⟩,
    fun a t' step => match alike.symm.step (a := a) (t := (t', (y, a) :: p')) ⟨step, rfl⟩ with
      | ⟨u, ⟨step', _⟩, joined⟩ => ⟨u.1, step', u.2, (y, a) :: p', joined.symm⟩⟩

/-- **Where no claim tells the past apart, kept configurations are alike exactly where their
presents are.** -/
theorem keepFrame_alike_iff {F : Frame S A C} {h h' : S × List (S × A)} :
    Alike (keepFrame F) (keepFrame F) h h' ↔ Alike F F h.1 h'.1 :=
  ⟨fun alike => ⟨_, keepFrame_present F, h.2, h'.2, alike⟩,
   fun alike => ⟨_, keepFrame_bisimulation F, alike⟩⟩

/-- **A kept history returns up to likeness where its present does and no claim tells the
past apart.** Along a run keeping its history, two steps whose presents are alike have kept
configurations that are distinct (`keepHistory_new`) and alike: `keepHistory_new` needs
equality, or claims that tell the past apart. -/
theorem keepHistory_returns_alike {F : Frame S A C} (r : Run (keepFrame F).P) {i j : Nat}
    (lt : i < j) (back : Alike F F (r.state i).1 (r.state j).1) :
    r.state i ≠ r.state j ∧ Alike (keepFrame F) (keepFrame F) (r.state i) (r.state j) :=
  ⟨keepHistory_new (P := F.P) r i j lt, keepFrame_alike_iff.mpr back⟩

/-- Where the claims name the kept configurations, a kept history is not alike to itself at
two steps. -/
theorem keepHistory_new_named {S A : Type} {P : Process S A} (r : Run (keepHistory P)) {i j : Nat}
    (lt : i < j) :
    ¬ Alike (Frame.configurations (keepHistory P)) (Frame.configurations (keepHistory P))
      (r.state i) (r.state j) :=
  fun alike => keepHistory_new r i j lt (alike_configurations alike)

/-! ### What no claim tells apart is not excluded -/

/-- The process admitting every step, with nothing claimed. -/
def anything (S : Type u) (A : Type v) : Frame S A Unit :=
  ⟨⟨fun _ _ _ => True⟩, fun _ _ => True⟩

/-- Under the process admitting every step with nothing claimed, every two configurations are
alike. -/
theorem anything_alike (S : Type u) (A : Type v) (s s' : S) :
    Alike (anything S A) (anything S A) s s' :=
  ⟨fun _ _ => True, fun _ _ _ =>
    ⟨fun _ => Iff.rfl, fun _ t _ => ⟨t, trivial, trivial⟩,
      fun _ t _ => ⟨t, trivial, trivial⟩⟩,
    trivial⟩

/-- Read through `π`, up to likeness under claims `claims` on the description, the record up to
`t` fixes the outcome of `a` at `k` to `κ`: every process on the description admitting the run's
steps so read and determined up to likeness at `k` sends `a` at `k` to configurations alike to
`κ`. -/
def Run.FixesThroughAlike {K : Type u'} {D : Type w} {P : Process S A} (r : Run P) (π : S → K)
    (claims : K → D → Prop) (t : Nat) (k : K) (a : A) (κ : K) : Prop :=
  ∀ Q : Process K A, DeterminedAt (⟨Q, claims⟩ : Frame K A D) k → r.StepsThrough π Q t →
    ∀ κ', Q.step k a κ' → Alike (⟨Q, claims⟩ : Frame K A D) ⟨Q, claims⟩ κ' κ

/-- **One occasion stands for every configuration in its class, up to likeness**:
`Run.generalizes` of `Becoming.Experiment` with determinacy and the conclusion read up to
likeness. Where the step factors through `π` into a process determined up to likeness at `k`, an
outcome the record fixes up to likeness for `a` at `k` is, up to likeness, the outcome read
through `π` of `a` at every configuration projecting to `k`. -/
theorem Run.generalizesAlike {K : Type u'} {D : Type w} {P : Process S A} (r : Run P)
    {π : S → K} {claims : K → D → Prop} {Q : Process K A}
    {k : K} (determined : DeterminedAt (⟨Q, claims⟩ : Frame K A D) k)
    (factors : FactorsThrough P π Q) {t : Nat} {a : A} {κ : K}
    (fixes : r.FixesThroughAlike π claims t k a κ) {s u : S} (at_k : π s = k)
    (step : P.step s a u) : Alike (⟨Q, claims⟩ : Frame K A D) ⟨Q, claims⟩ (π u) κ :=
  fixes Q determined (r.stepsThrough_of_factors factors t) (π u)
    (Eq.subst (motive := fun x => Q.step x a (π u)) at_k (factors _ _ _ step))

/-- **With nothing claimed, every description carries a law up to likeness**: the process
admitting every step is determined up to likeness and every step factors through every
description into it. So `carries_law_iff` of `Becoming.Mechanism` needs equality on the
description, or claims that tell it apart; with the description named by the claims it is
`carries_law_iff` itself (`determined_iff_named`). -/
theorem carries_unregistered {K : Type u'} (P : Process S A) (π : S → K) :
    ∃ Q : Process K A, (∀ k, DeterminedAt (⟨Q, fun _ _ => True⟩ : Frame K A Unit) k) ∧
      FactorsThrough P π Q :=
  ⟨(anything K A).P, fun _ _ _ _ _ _ => anything_alike K A _ _, fun _ _ _ _ => trivial⟩

end Likeness

/-! ### The twins: retargeting one of two alike configurations -/

namespace Twins

/-- The twins are determined up to likeness everywhere. -/
theorem determinedAt : ∀ x, DeterminedAt frame x
  | .start => alike_one.2.2.2
  | .left => fun _ _ _ step => nomatch step.1
  | .right => fun _ _ _ step => nomatch step.1

/-- The twins with the step from `left` alone retargeted to `start`. -/
def retargeted : Frame Config Unit Unit := ⟨retarget frame.P .left () .start, frame.realized⟩

/-- **Retargeting one of two alike configurations breaks determinacy up to likeness.** The twins
are determined up to likeness everywhere; with the step from `left` alone sent back to the start,
the two outcomes of the start's move are no longer alike, and the frame is not determined up to
likeness at the start. Retargeting their likeness class keeps it everywhere: `retarget_determined`
needs equality, `retargetAlike_determinedAt` does not. -/
theorem retarget_breaks :
    (∀ x, DeterminedAt frame x) ∧ ¬ DeterminedAt retargeted .start ∧
      ∀ x, DeterminedAt (retargetAlike frame .left () .start) x :=
  ⟨determinedAt,
   fun determined =>
    match (determined () .left .right
        (.inl ⟨fun ⟨same, _⟩ => (nomatch same), rfl, .inl rfl⟩)
        (.inl ⟨fun ⟨same, _⟩ => (nomatch same), rfl, .inr rfl⟩)).step
        (a := ()) (t := .start) (.inr ⟨rfl, rfl, rfl⟩) with
    | ⟨_, .inl ⟨_, step⟩, _⟩ => nomatch step.1
    | ⟨_, .inr ⟨same, _, _⟩, _⟩ => (nomatch same),
   retargetAlike_determinedAt determinedAt .left () .start⟩

end Twins

/-! ### Runs that meet and part -/

namespace Coarse

/-- The first part after `n` flips from `false`. -/
def flips : Nat → Bool
  | 0 => false
  | n + 1 => !flips n

/-- The run keeping its second part `false`. -/
def still : Run process := ⟨fun n => (flips n, false), fun _ => (), fun _ => rfl⟩

/-- The second part of the run that turns: `false`, then `true`. -/
def turnedPart : Nat → Bool
  | 0 => false
  | _ + 1 => true

/-- The run turning its second part to `true` at the first step. -/
def turned : Run process := ⟨fun n => (flips n, turnedPart n), fun _ => (), fun _ => rfl⟩

/-- The process read through its first part. -/
def firstFrame : Frame (Bool × Bool) Unit Bool := ⟨process, fun s c => s.1 = c⟩

theorem first_bisimulation : Bisimulation firstFrame firstFrame fun s s' => s.1 = s'.1 :=
  fun _ _ same =>
    ⟨fun _ => ⟨fun h => same.symm.trans h, fun h => same.trans h⟩,
     fun _ t step => ⟨t, step.trans (congrArg not same), rfl⟩,
     fun _ t step => ⟨t, step.trans (congrArg not same.symm), rfl⟩⟩

/-- Read through its first part, the process is determined up to likeness. -/
theorem first_determinedAt : ∀ s, DeterminedAt firstFrame s :=
  fun _ _ _ _ step step' => ⟨_, first_bisimulation, step.trans step'.symm⟩

/-- **Runs that meet part, where the process is not determined; up to what is claimed they stay
alike.** Two runs from one configuration taking the same moves differ at the first step, so
merged does not stay merged (`Determined.stays_merged` needs a determined process); read through
the first part, the process is determined up to likeness and the runs stay alike
(`DeterminedAt.stays_alike`). -/
theorem meet_and_part :
    still.state 0 = turned.state 0 ∧ (∀ n, still.act n = turned.act n) ∧
      still.state 1 ≠ turned.state 1 ∧ (∀ s, DeterminedAt firstFrame s) ∧
        ∀ n, Alike firstFrame firstFrame (still.state n) (turned.state n) :=
  ⟨rfl, fun _ => rfl, fun same => Bool.noConfusion (congrArg Prod.snd same), first_determinedAt,
   fun _ => ⟨_, first_bisimulation, rfl⟩⟩

end Coarse

/-! ### A confound not claimed is not excluded -/

namespace Confound

/-- **Excluding a model needs the outcome claimed.** With nothing claimed, the process
admitting every step is determined up to likeness and admits every step of the varied run read
through the outcome, so `varied_refutes` fails up to likeness; with the outcome named by the
claims, determinacy up to likeness is determinacy and the exclusion stands. -/
theorem refutes_registered :
    (∃ Q : Process Bool Move,
      (∀ k, DeterminedAt (⟨Q, fun _ _ => True⟩ : Frame Bool Move Unit) k) ∧
        (run varied).StepsThrough outcome Q 4) ∧
    ¬ ∃ Q : Process Bool Move, (∀ k, DeterminedAt (Frame.configurations Q) k) ∧
      (run varied).StepsThrough outcome Q 4 :=
  ⟨⟨(anything Bool Move).P, fun _ _ _ _ _ _ => anything_alike Bool Move _ _,
      fun _ _ => trivial⟩,
   fun ⟨Q, determined, steps⟩ =>
    varied_refutes ⟨Q, determined_iff_named.mpr determined, steps⟩⟩

end Confound

/-! ## Capture's rule region -/

namespace Law

variable {S : Type u} {R : Type v}

/-- **Where the rule keeps itself, the configurations with a given rule are a region the law
never leaves.** -/
theorem rule_absorbing {next : S × R → S × R} (keeps : ∀ s, (next s).2 = s.2) (g : R) :
    Absorbing next (fun s => s.2 = g) :=
  fun s inside => (keeps s).trans inside

/-- **The configuration a rule holds is fixed**, where the next configuration depends on the rule
and not on the state and the rule keeps itself. -/
theorem held_absorbing {next : S × R → S × R} (byRule : ∀ x x' g, next (x, g) = next (x', g))
    (keeps : ∀ s, (next s).2 = s.2) (x : S) (g : R) :
    Absorbing next (fun s => s = next (x, g)) :=
  fun _ same => (congrArg next same).trans
    ((congrArg (fun h => next ((next (x, g)).1, h)) (keeps (x, g))).trans (byRule _ x g))

/-- **A perturbed state is drawn into the configuration the rule holds**, entering at the first
step, where the next configuration depends on the rule and not on the state. -/
theorem perturbation_drawnInto {next : S × R → S × R}
    (byRule : ∀ x x' g, next (x, g) = next (x', g))
    {x x' : S} {g : R} (apart : (x', g) ≠ next (x, g)) :
    DrawnInto next (fun s => s = next (x, g)) (x', g) :=
  ⟨apart, 1, byRule x' x g⟩

end Law

namespace Captured

/-- The rule keeps itself. -/
theorem keeps (s : Bool × Bool) : (next s).2 = s.2 := rfl

/-- **The configurations with a given rule are a region the law never leaves**: an instance of
`Law.Absorbing`. -/
theorem rule_region_absorbing (g : Bool) : Law.Absorbing next (fun s => s.2 = g) :=
  Law.rule_absorbing keeps g

/-- The configuration the rule holds is absorbing. -/
theorem held_absorbing (g : Bool) : Law.Absorbing next (fun s => s = (g, g)) :=
  Law.held_absorbing byRule keeps g g

/-- **A perturbed state is drawn into the configuration the rule holds and never returns**: an
instance of `Law.DrawnInto` and of `Law.Drawn.not_returns`. -/
theorem state_perturbation_drawn (g : Bool) :
    Law.DrawnInto next (fun s => s = (g, g)) (!g, g) ∧ ¬ Law.Returns next (!g, g) :=
  have drawn : Law.DrawnInto next (fun s => s = (g, g)) (!g, g) :=
    Law.perturbation_drawnInto byRule (x := g) fun same => ListTests.not_ne_self g (congrArg Prod.fst same)
  ⟨drawn, Law.Drawn.not_returns ⟨_, held_absorbing g, drawn⟩⟩

/-- **A perturbed rule draws the state into the configuration the new rule holds**, and the
perturbed configuration never returns. -/
theorem rule_perturbation_drawn (g : Bool) :
    Law.DrawnInto next (fun s => s = (!g, !g)) (g, !g) ∧ ¬ Law.Returns next (g, !g) :=
  have drawn : Law.DrawnInto next (fun s => s = (!g, !g)) (g, !g) :=
    Law.perturbation_drawnInto byRule (x := !g) fun same => ListTests.not_ne_self g (congrArg Prod.fst same).symm
  ⟨drawn, Law.Drawn.not_returns ⟨_, held_absorbing (!g), drawn⟩⟩

end Captured

end Becoming

section RecurrenceRuns

/-!
## Recurrence on the process of a determined law: merging, returning and the kept history

`Becoming.Recurrence` states what every determined law `next` keeps, loses and returns to, on
its orbits. A determined law is a process of the spine (`Law.process next`), every run of it is
its orbit from where the run begins (`Branching.law_run_state`), and its reachability, returning
and merging are those of `Becoming.Branching` (`law_reachable_iff`, `law_returns_iff`,
`law_lossless_iff`, `law_merges_iff`). This section states the laws of `Becoming.Recurrence` that
hold for determined change and fail for branching processes as laws of the process of the law,
and the kept history as a process whose runs carry the run of the law in their present.

* **Within finitely many configurations, losing nothing is returning.** Where a list holds every
  configuration, the process of a determined law merges nothing exactly where every configuration
  returns (`lossless_iff_returns`), and a merge loses a possibility for good: some configuration
  cannot be had as many steps on as there are configurations (`merges_loses`). Under a branching
  process neither holds (`Branching.OneWay.merge_keeps`).
* **The history kept along a run.** Keeping its history, the process of every law merges nothing
  (`kept_lossless`), no configuration of it returns (`kept_never_returns`), its beginning cannot be
  had after the first step (`kept_loses_beginning`), and no list holds the configurations of any
  of its runs (`kept_unlisted`). The history kept along a run of the law (`keptRun`) has the run's
  configuration as its present at every step (`keptRun_present`); where the run comes back to where
  it began, the present comes back with another history (`return_keeps_history`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u

namespace RecurrenceRuns

variable {S : Type u} {next : S → S}

/-! ### Within finitely many configurations -/

/-- **Within finitely many configurations, the process of a determined law merges nothing exactly
where every configuration returns.** -/
theorem lossless_iff_returns {all : List S} (every : ∀ s, s ∈ all) :
    Branching.Lossless (Law.process next) ↔ ∀ s, Branching.Returns (Law.process next) s :=
  Branching.law_lossless_iff.trans ((Law.lossless_iff_returns every).trans
    ⟨fun returns s => Branching.law_returns_iff.mpr (returns s),
     fun returns s => Branching.law_returns_iff.mp (returns s)⟩)

/-- **Within finitely many configurations, a merge of a determined law's process loses a
possibility for good**: some configuration cannot be had as many steps on as there are
configurations, nor later (`Branching.lost_stays`). -/
theorem merges_loses (merges : Branching.Merges (Law.process next)) {all : List S}
    (every : ∀ s, s ∈ all) : ¬ ∀ s, Branching.Reachable (Law.process next) all.length s :=
  fun reach => Law.Merges.loses (Branching.law_merges_iff.mp merges) every
    (fun s => Branching.law_reachable_iff.mp (reach s))

/-! ### The history kept -/

/-- **Keeping its history, the process of every law merges nothing.** -/
theorem kept_lossless (next : S → S) :
    Branching.Lossless (Law.process (Law.withHistory next)) :=
  Branching.law_lossless_iff.mpr (Law.withHistory_lossless next)

/-- **Keeping its history, no configuration of the process returns.** -/
theorem kept_never_returns (next : S → S) (h : S × List S) :
    ¬ Branching.Returns (Law.process (Law.withHistory next)) h :=
  fun returns => Law.withHistory_never_returns next h (Branching.law_returns_iff.mp returns)

/-- **Keeping its history, the beginning is lost at the first step**: no kept history with
nothing past can be had one or more steps on. -/
theorem kept_loses_beginning (next : S → S) (s : S) (n : Nat) :
    ¬ Branching.Reachable (Law.process (Law.withHistory next)) (n + 1) (s, []) :=
  fun reach => Law.withHistory_loses_beginning next s n (Branching.law_reachable_iff.mp reach)

/-- **Keeping its history needs openness**: no list holds the configurations of a run of the
kept history. -/
theorem kept_unlisted (h : Run (Law.process (Law.withHistory next))) :
    ¬ ∃ l : List (S × List S), ∀ n, h.state n ∈ l :=
  fun ⟨l, held⟩ => Law.withHistory_unlisted next (h.state 0)
    ⟨l, fun n => Eq.subst (motive := fun x => x ∈ l) (Branching.law_run_state h n) (held n)⟩

/-- The history kept along a run of a determined law, from a given past: the run of the kept
history from the run's first configuration. -/
def keptRun (r : Run (Law.process next)) (past : List S) :
    Run (Law.process (Law.withHistory next)) :=
  Law.run (Law.withHistory next) (r.state 0, past)

/-- **The present of the history kept along a run is the run's configuration**, at every step. -/
theorem keptRun_present (r : Run (Law.process next)) (past : List S) (n : Nat) :
    ((keptRun r past).state n).1 = r.state n :=
  (Law.present_orbit next (r.state 0, past) n).trans (Branching.law_run_state r n).symm

/-- **The present comes back; the history does not.** Where a run of a determined law is, after
`p > 0` steps, where it began, the history kept along it has its first configuration as present
again and differs from where it began. -/
theorem return_keeps_history (r : Run (Law.process next)) {p : Nat} (pos : 0 < p)
    (back : r.state p = r.state 0) (past : List S) :
    ((keptRun r past).state p).1 = r.state 0 ∧ (keptRun r past).state p ≠ (keptRun r past).state 0 :=
  Law.return_keeps_history pos ((Branching.law_run_state r p).symm.trans back) past

end RecurrenceRuns

end Becoming

end RecurrenceRuns
