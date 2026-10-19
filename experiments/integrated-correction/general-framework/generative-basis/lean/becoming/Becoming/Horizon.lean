import Becoming.Labelled
import Becoming.Return

/-!
# What a finite history decides

`Becoming.Renewal` shows that the class of a formation belongs to the run, not to a
configuration: from one configuration, one run renews and another consumes. Here the
same holds for every finite stretch of a run. For every horizon `h`, two runs of
`Renewable` agree on their configurations and actions up to `h`, the focal formation
drawing beyond renewal at each of those steps, while the condition still meets the
dependence on it. Afterwards one run draws within renewal and the focal formation
renews; the other keeps drawing beyond it, and the focal formation consumes. Every
event of the focal formation before `h` is within renewal in both runs, so it is
neither breaking nor undermining.

So a reading decided by the first `h` steps of a run either excludes a
run that the whole-run reading classifies as renewing, or includes one it classifies as
consuming. The work is done by including every renewing run: the renewing run itself
draws beyond renewal before `h`, from a stock that absorbs it, and the whole-run reading
includes those draws (`whole_run_includes_overdraw`). The result holds unchanged in the
support-gated law, whose renewal stops below support (`Feedback.prefix_does_not_decide`),
so it does not rest on the absence of feedback.

What a finite history decides depends on the reading:
* The event-level stepwise and cycle readings are fixed by the history up to the step
  after the event, or `p` steps after it. They include depletion for as long as the
  condition still meets the dependence.
* The formation-level readings over cycles are not fixed by any finite prefix
  (`cycle_reading_not_finite`), nor is the whole-run classification.
* A reading of amounts, "draws no more than is renewed at this step", is fixed by the
  history through the step, includes every event of `withinRenewal` and withholds every draw
  beyond renewal before `h` in both runs (`amount_reading`). It escapes the theorem only
  by not including every run the whole-run reading classifies as renewing. It cannot be
  stated on `Web`, whose `draws` carries no amount and which has no renewal rate.

Classifying a stretch of drawing as the whole-run reading does requires knowing where
the run goes, an account of its continuation, not only its past. In `Renewable` the
dynamics are fixed by the actions, so what no prefix decides is the action still to be
taken.

**What a finite history refutes, for every process.** A reading of runs is refutable where
every run outside it has a horizon beyond which no agreeing run is inside (`Refutable`), and a
run adheres to a reading where every finite stretch of it is a stretch of a run inside
(`Adheres`). With no premise:
* a refutable reading holds, up to double negation, at every run adhering to it
  (`Refutable.not_not`), and a refutable superset holds so at every run adhering to the subset
  (`Refutable.adheres_least`); for a stable reading, adhering is holding (`Refutable.adheres_iff`);
* a run adhering to a reading it lies outside shows the reading is not refutable
  (`not_refutable_of_adheres`), and dually not verifiable (`not_verifiable_of_adheres`); in the
  process whose runs are all sequences, recurrence and eventual occurrence are not refutable
  (`Sequences.recurs_not_refutable`, `Sequences.eventually_not_refutable`), and never occurring
  is not verifiable (`Sequences.never_not_verifiable`);
* what adheres to a reading is closed: where no run inside agrees with a run up to some step, no
  run agreeing with it there adheres (`Adheres.closed`). So adhering is refutable exactly where
  every run not adhering has such a step (`refutable_adheres_iff`), which excluded middle gives
  (`refutable_adheres_of_em`); with no premise it is not stated;
* a reading made of tests, each fixed by the history through its step, holds at every run
  adhering to it (`adheres_passes`). It is refutable given Markov's principle
  (`refutable_passes`), and asked of every process exactly then
  (`refutable_passes_iff_markov`): what a refuting history must find is a failed test it is
  only known not to miss.

No ethical predicate, ranking or axiom occurs. Whether an actual history continues
one way or the other is a question for inquiry into it.

**Classical sources.** Refutable readings are the safety properties and verifiable readings their
duals; a reading every finite stretch can still meet, as recurrence, is a liveness property
(Alpern and Schneider 1985: safety is closedness, liveness is density, in the topology of runs).
Refutation and verification by finite histories are the formal learning-theoretic notions of
Kelly (1996). `Adheres K` is the closure of `K`; that the closure is refutable is classical, and
constructively it is the step from a failure to adhere to a horizon that witnesses it.

The support-gated law (`Feedback`) is in `Becoming.HorizonWebs`, which states the horizon on its
webs, so that module does not import the frame (board item W).
-/

namespace Becoming

open Generative

universe u v

variable {S : Type u} {A : Type v}

/-- A run preceded by one admissible step into its start. -/
def Run.cons {P : Process S A} (s : S) (a : A) (r : Run P) (into : P.step s a (r.state 0)) :
    Run P :=
  ⟨fun | 0 => s | t + 1 => r.state t, fun | 0 => a | t + 1 => r.act t,
    fun | 0 => into | t + 1 => r.step t⟩

/-- Two runs agree up to `h`: the same configurations up to `h` and the same actions
before it. -/
def Run.AgreeUpTo {P : Process S A} (h : Nat) (r r' : Run P) : Prop :=
  (∀ t, t ≤ h → r.state t = r'.state t) ∧ ∀ t, t < h → r.act t = r'.act t

namespace Renewable

/-- For every horizon `h`, two runs agree up to `h`, drawing beyond renewal at every
step before it, with every event of the focal formation there within renewal. Then one
renews and the other consumes. -/
theorem prefix_does_not_decide : ∀ h : Nat, ∃ renewing consuming : Run process,
    renewing.AgreeUpTo h consuming ∧ (∀ t, t < h → consuming.act t = 2) ∧
    (∀ t, t < h → (conditions.dependence.along renewing).RenewingAt t .focal ∧
      (conditions.dependence.along consuming).RenewingAt t .focal) ∧
    (conditions.dependence.along renewing).RenewingIn .focal ∧
    (conditions.dependence.along consuming).ConsumingIn .focal
  | 0 => ⟨withinRenewal, beyondRenewal,
      ⟨fun | 0, _ => rfl, fun _ before => absurd before (Nat.not_lt_zero _)⟩,
      fun _ before => absurd before (Nat.not_lt_zero _),
      fun _ before => absurd before (Nat.not_lt_zero _),
      fun _ _ _ _ g depends => match g, depends with
        | .sustaining, _ => ⟨Nat.le_refl 1, Nat.le_refl 1⟩,
      ⟨0, (), trivial, .sustaining, 1, trivial, fun | _ + 2, _ => Nat.zero_lt_one⟩⟩
  | h + 1 =>
    match prefix_does_not_decide h with
    | ⟨r, c, ⟨states, acts⟩, over, within, renews, consumes⟩ =>
      have supported : 1 ≤ r.state 0 := (renews 0 () (Or.inr trivial) 0 .sustaining trivial).1
      have first : ∀ q : Run process, q.state 0 = r.state 0 → ∀ into,
          (conditions.dependence.along (Run.cons (r.state 0 + 1) 2 q into)).RenewingAt 0 .focal :=
        fun _ start _ => ⟨trivial, fun _ _ g depends => match g, depends with
          | .sustaining, _ => ⟨Nat.succ_le_succ (Nat.zero_le _),
              Nat.le_trans supported (Nat.le_of_eq start.symm)⟩⟩
      have start : c.state 0 = r.state 0 := (states 0 (Nat.zero_le h)).symm
      ⟨Run.cons (r.state 0 + 1) 2 r rfl, Run.cons (r.state 0 + 1) 2 c (start ▸ rfl),
       ⟨fun | 0, _ => rfl | t + 1, upTo => states t (Nat.le_of_succ_le_succ upTo),
        fun | 0, _ => rfl | t + 1, before => acts t (Nat.lt_of_succ_lt_succ before)⟩,
       fun | 0, _ => rfl | t + 1, before => over t (Nat.lt_of_succ_lt_succ before),
       fun | 0, _ => ⟨first r rfl rfl, first c start _⟩
           | t + 1, before => within t (Nat.lt_of_succ_lt_succ before),
       fun _ _ _ t g depends => match t, g, depends with
         | 0, .sustaining, _ => ⟨Nat.succ_le_succ (Nat.zero_le _), supported⟩
         | t + 1, .sustaining, _ => renews 0 () (Or.inr trivial) t .sustaining trivial,
       match consumes with
       | ⟨_, _, _, g, T, depends, below⟩ =>
         ⟨0, (), trivial, g, T + 1, depends, fun
           | t + 1, later => below t (Nat.lt_of_succ_lt_succ later)⟩⟩

/-- A reading decided by the first `h` steps of a run, including every run in which the
focal formation renews, includes a run in which it consumes. -/
theorem finite_reading_includes_consumption (h : Nat) (reading : Run process → Prop)
    (decided : ∀ r r', r.AgreeUpTo h r' → reading r → reading r')
    (includes : ∀ r, (conditions.dependence.along r).RenewingIn .focal → reading r) :
    ∃ r, (conditions.dependence.along r).ConsumingIn .focal ∧ reading r :=
  match prefix_does_not_decide h with
  | ⟨renewing, consuming, agree, _, _, renews, consumes⟩ =>
    ⟨consuming, consumes, decided renewing consuming agree (includes renewing renews)⟩

/-- The whole-run reading includes drawing beyond renewal. For every horizon, the
renewing run above draws two units, one beyond renewal, at every step before it, and
every event of its focal formation is active and not consuming. -/
theorem whole_run_includes_overdraw (h : Nat) : ∃ r : Run process,
    (∀ t, t < h → r.act t = 2) ∧ (conditions.dependence.along r).RenewingIn .focal ∧
      ∀ t, (conditions.along r).active t .focal ∧
        ¬ RelationalRenewal.ConsumingIn (conditions.along r) .focal :=
  match prefix_does_not_decide h with
  | ⟨r, _, ⟨_, acts⟩, over, _, renews, _⟩ =>
    ⟨r, fun t before => (acts t before).trans (over t before), renews, fun _ => ⟨trivial,
      RelationalRenewal.renewing_not_consuming ((Web.static_renewingIn _ _).mp renews)⟩⟩

/-- A reading of amounts escapes the horizon. "Draws no more than is renewed", at a step,
is fixed by the history through that step, includes every event of `withinRenewal`, and
withholds every draw before the horizon in both runs above. -/
theorem amount_reading (h : Nat) :
    (∀ t (r r' : Run process), r.AgreeUpTo (t + 1) r' → (r.act t ≤ 1 ↔ r'.act t ≤ 1)) ∧
    (∀ t, withinRenewal.act t ≤ 1) ∧
    ∃ r c : Run process, (conditions.dependence.along r).RenewingIn .focal ∧
      (conditions.dependence.along c).ConsumingIn .focal ∧
      ∀ t, t < h → ¬ r.act t ≤ 1 ∧ ¬ c.act t ≤ 1 :=
  ⟨fun t _ _ ⟨_, acts⟩ => acts t (Nat.lt_succ_self t) ▸ Iff.rfl, fun _ => Nat.le_refl 1,
   match prefix_does_not_decide h with
   | ⟨r, c, ⟨_, acts⟩, over, _, renews, consumes⟩ =>
     ⟨r, c, renews, consumes, fun t before =>
       ⟨fun le => Nat.not_succ_le_self 1
          (Nat.le_trans (Nat.le_of_eq ((acts t before).trans (over t before)).symm) le),
        fun le => Nat.not_succ_le_self 1 (Nat.le_trans (Nat.le_of_eq (over t before).symm) le)⟩⟩⟩

/-- The formation-level reading over cycles of any positive length is not fixed by any
finite prefix. -/
theorem cycle_reading_not_finite (h p : Nat) (positive : 0 < p) :
    ¬ ∀ r r' : Run process, r.AgreeUpTo h r' →
      (conditions.dependence.along r).RenewingInWithin p .focal →
      (conditions.dependence.along r').RenewingInWithin p .focal :=
  fun decided =>
    match finite_reading_includes_consumption h _ decided
      (fun _ renews => (Web.RenewingIn.within_one renews).mono positive) with
    | ⟨_, consumes, renews⟩ => renews.not_consuming consumes

end Renewable

/-! ## The horizon in the support-gated law -/

/-! ## What a finite history refutes -/

theorem Run.AgreeUpTo.refl {P : Process S A} (r : Run P) (h : Nat) : r.AgreeUpTo h r :=
  ⟨fun _ _ => rfl, fun _ _ => rfl⟩

theorem Run.AgreeUpTo.symm {P : Process S A} {h : Nat} {r r' : Run P} (agree : r.AgreeUpTo h r') :
    r'.AgreeUpTo h r :=
  ⟨fun t upTo => (agree.1 t upTo).symm, fun t before => (agree.2 t before).symm⟩

theorem Run.AgreeUpTo.trans {P : Process S A} {h : Nat} {r r' r'' : Run P}
    (agree : r.AgreeUpTo h r') (agree' : r'.AgreeUpTo h r'') : r.AgreeUpTo h r'' :=
  ⟨fun t upTo => (agree.1 t upTo).trans (agree'.1 t upTo),
   fun t before => (agree.2 t before).trans (agree'.2 t before)⟩

theorem Run.AgreeUpTo.mono {P : Process S A} {h h' : Nat} {r r' : Run P} (le : h' ≤ h)
    (agree : r.AgreeUpTo h r') : r.AgreeUpTo h' r' :=
  ⟨fun t upTo => agree.1 t (Nat.le_trans upTo le),
   fun t before => agree.2 t (Nat.lt_of_lt_of_le before le)⟩

/-- A reading of runs is refutable where every run outside it has a horizon beyond which no
run agreeing with it up to there is inside. -/
def Refutable {P : Process S A} (K : Run P → Prop) : Prop :=
  ∀ r, ¬ K r → ∃ h, ∀ r', r.AgreeUpTo h r' → ¬ K r'

/-- A reading of runs is verifiable where every run inside it has a horizon up to which every
agreeing run is inside. -/
def Verifiable {P : Process S A} (K : Run P → Prop) : Prop :=
  ∀ r, K r → ∃ h, ∀ r', r.AgreeUpTo h r' → K r'

/-- A run adheres to a reading where every finite stretch of it is a stretch of a run inside the
reading. -/
def Adheres {P : Process S A} (K : Run P → Prop) (r : Run P) : Prop :=
  ∀ h, ∃ r', K r' ∧ r.AgreeUpTo h r'

theorem Adheres.of {P : Process S A} {K : Run P → Prop} {r : Run P} (inside : K r) : Adheres K r :=
  fun h => ⟨r, inside, .refl r h⟩

theorem Adheres.mono {P : Process S A} {K L : Run P → Prop} {r : Run P} (sub : ∀ r, K r → L r)
    (adheres : Adheres K r) : Adheres L r :=
  fun h => match adheres h with
    | ⟨r', inside, agree⟩ => ⟨r', sub r' inside, agree⟩

/-- Adhering to what adheres is adhering. -/
theorem Adheres.adheres {P : Process S A} {K : Run P → Prop} {r : Run P}
    (adheres : Adheres (Adheres K) r) : Adheres K r :=
  fun h => match adheres h with
    | ⟨_, adheres', agree⟩ => match adheres' h with
      | ⟨r'', inside, agree'⟩ => ⟨r'', inside, agree.trans agree'⟩

/-- **A refutable reading holds, up to double negation, at every run adhering to it.** -/
theorem Refutable.not_not {P : Process S A} {K : Run P → Prop} {r : Run P} (refutable : Refutable K)
    (adheres : Adheres K r) : ¬ ¬ K r :=
  fun outside => match refutable r outside with
    | ⟨h, blocked⟩ => match adheres h with
      | ⟨r', inside, agree⟩ => blocked r' agree inside

/-- **Refutable supersets hold where the subset is adhered to.** A refutable reading containing
`K` holds, up to double negation, at every run adhering to `K`. -/
theorem Refutable.adheres_least {P : Process S A} {K L : Run P → Prop} {r : Run P}
    (refutable : Refutable L) (sub : ∀ r, K r → L r) (adheres : Adheres K r) : ¬ ¬ L r :=
  refutable.not_not (adheres.mono sub)

/-- **For a stable refutable reading, adhering is holding.** -/
theorem Refutable.adheres_iff {P : Process S A} {K : Run P → Prop} {r : Run P}
    (refutable : Refutable K) (stable : ∀ r, ¬ ¬ K r → K r) : Adheres K r ↔ K r :=
  ⟨fun adheres => stable r (refutable.not_not adheres), Adheres.of⟩

/-- **A run adhering to a reading it lies outside shows the reading is not refutable.** -/
theorem not_refutable_of_adheres {P : Process S A} {K : Run P → Prop} {r : Run P}
    (adheres : Adheres K r) (outside : ¬ K r) : ¬ Refutable K :=
  fun refutable => refutable.not_not adheres outside

/-- **A run inside a reading and adhering to its complement shows it is not verifiable.** -/
theorem not_verifiable_of_adheres {P : Process S A} {K : Run P → Prop} {r : Run P}
    (adheres : Adheres (fun r => ¬ K r) r) (inside : K r) : ¬ Verifiable K :=
  fun verifiable => match verifiable r inside with
    | ⟨h, all⟩ => match adheres h with
      | ⟨r', outside, agree⟩ => outside (all r' agree)

/-- **What adheres to a reading is closed.** Where no run inside `K` agrees with `r` up to `h`, no
run agreeing with `r` up to `h` adheres to `K`. -/
theorem Adheres.closed {P : Process S A} {K : Run P → Prop} {r : Run P} {h : Nat}
    (none_ : ¬ ∃ r', K r' ∧ r.AgreeUpTo h r') : ∀ r', r.AgreeUpTo h r' → ¬ Adheres K r' :=
  fun _ agree adheres => match adheres h with
    | ⟨r'', inside, agree'⟩ => none_ ⟨r'', inside, agree.trans agree'⟩

/-- **Adhering is refutable exactly where every failure to adhere has a horizon** at which no run
inside the reading agrees. -/
theorem refutable_adheres_iff {P : Process S A} {K : Run P → Prop} :
    Refutable (Adheres K) ↔ ∀ r, ¬ Adheres K r → ∃ h, ¬ ∃ r', K r' ∧ r.AgreeUpTo h r' :=
  ⟨fun refutable r outside => match refutable r outside with
    | ⟨h, blocked⟩ => ⟨h, fun ⟨r', inside, agree⟩ => blocked r' agree (Adheres.of inside)⟩,
   fun witnessed r outside => match witnessed r outside with
    | ⟨_, none_⟩ => ⟨_, Adheres.closed none_⟩⟩

/-- **Excluded middle makes adhering refutable**, for every reading of every process. -/
theorem refutable_adheres_of_em {P : Process S A} (em : ∀ p : Prop, p ∨ ¬ p) (K : Run P → Prop) :
    Refutable (Adheres K) :=
  refutable_adheres_iff.mpr fun r outside =>
    match em (∃ h, ¬ ∃ r', K r' ∧ r.AgreeUpTo h r') with
    | .inl found => found
    | .inr absent => False.elim (outside fun h =>
        match em (∃ r', K r' ∧ r.AgreeUpTo h r') with
        | .inl found => found
        | .inr none_ => False.elim (absent ⟨h, none_⟩))

/-- The reading of passing every test: no test fails. -/
def Passes {P : Process S A} (fails : Nat → Run P → Bool) (r : Run P) : Prop :=
  ∀ n, fails n r = false

/-- Each test is fixed by the history through its step. -/
def ByPrefixes {P : Process S A} (fails : Nat → Run P → Bool) : Prop :=
  ∀ n r r', r.AgreeUpTo (n + 1) r' → fails n r = fails n r'

/-- **A run adhering to the reading of tests passes them.** -/
theorem adheres_passes {P : Process S A} {fails : Nat → Run P → Bool} {r : Run P}
    (byPrefixes : ByPrefixes fails) (adheres : Adheres (Passes fails) r) : Passes fails r :=
  fun n => match adheres (n + 1) with
    | ⟨r', passes, agree⟩ => (byPrefixes n r r' agree).trans (passes n)

/-- Markov's principle: a sequence of Booleans that is not false throughout is true somewhere. -/
def Markov : Prop :=
  ∀ s : Nat → Bool, ¬ (∀ n, s n = false) → ∃ n, s n = true

/-- **Given Markov's principle, the reading of tests is refutable.** -/
theorem refutable_passes {P : Process S A} {fails : Nat → Run P → Bool} (markov : Markov)
    (byPrefixes : ByPrefixes fails) : Refutable (Passes fails) :=
  fun r outside => match markov (fun n => fails n r) outside with
    | ⟨n, failed⟩ => ⟨n + 1, fun r' agree passes =>
        nomatch failed.symm.trans ((byPrefixes n r r' agree).trans (passes n))⟩

/-- A sequence of Booleans is false before `h`, or true somewhere. -/
theorem false_below_or_true (s : Nat → Bool) : ∀ h, (∀ t, t < h → s t = false) ∨ ∃ t, s t = true
  | 0 => .inl fun _ before => absurd before (Nat.not_lt_zero _)
  | h + 1 =>
    match false_below_or_true s h with
    | .inr found => .inr found
    | .inl below =>
      match e : s h with
      | true => .inr ⟨h, e⟩
      | false => .inl fun t before =>
        match Nat.lt_or_eq_of_le (Nat.le_of_lt_succ before) with
        | .inl lt => below t lt
        | .inr eq => eq ▸ e

namespace Sequences

/-- The process whose runs are all sequences of moves. -/
def process (A : Type v) : Process Unit A := ⟨fun _ _ _ => True⟩

/-- The run taking the moves `s`. -/
def run {A : Type v} (s : Nat → A) : Run (process A) := ⟨fun _ => (), s, fun _ => trivial⟩

/-- Runs of the sequences agree up to `h` exactly where their moves agree before `h`. -/
theorem agree_iff {A : Type v} {h : Nat} {r r' : Run (process A)} :
    r.AgreeUpTo h r' ↔ ∀ t, t < h → r.act t = r'.act t :=
  ⟨fun agree => agree.2, fun acts => ⟨fun _ _ => rfl, acts⟩⟩

/-- The run that takes `s` before `h` and `c` from `h` on. -/
def splice {A : Type v} (s : Nat → A) (h : Nat) (c : A) : Run (process A) :=
  run fun t => if t < h then s t else c

theorem splice_agree {A : Type v} (s : Nat → A) (h : Nat) (c : A) :
    (run s).AgreeUpTo h (splice s h c) :=
  agree_iff.mpr fun _ before => (if_pos before).symm

theorem splice_after {A : Type v} (s : Nat → A) {h t : Nat} (c : A) (after : h ≤ t) :
    (splice s h c).act t = c :=
  if_neg (Nat.not_lt_of_le after)

/-- The moves recur: from every step on, some later move is `true`. This is `Becoming.Recurs` of
`Becoming.Change` for a family of one member (`Sequences.recurs_iff`, in `Becoming.Dissipation`,
the first module that sees both). -/
def Recurs (r : Run (process Bool)) : Prop := ∀ n, ∃ m, n ≤ m ∧ r.act m = true

/-- Some move is `true`. -/
def Eventually (r : Run (process Bool)) : Prop := ∃ m, r.act m = true

/-- **Recurrence is not refutable**: the run of `false` throughout adheres to it. -/
theorem recurs_not_refutable : ¬ Refutable Recurs :=
  not_refutable_of_adheres (r := run fun _ => false)
    (fun h => ⟨splice (fun _ => false) h true,
      fun n => ⟨n + h, Nat.le_add_right n h, splice_after _ true (Nat.le_add_left h n)⟩,
      splice_agree _ h true⟩)
    (fun recurs => match recurs 0 with
      | ⟨_, _, atTrue⟩ => nomatch atTrue)

/-- **Eventual occurrence is not refutable**: the run of `false` throughout adheres to it. -/
theorem eventually_not_refutable : ¬ Refutable Eventually :=
  not_refutable_of_adheres (r := run fun _ => false)
    (fun h => ⟨splice (fun _ => false) h true, ⟨h, splice_after _ true (Nat.le_refl h)⟩,
      splice_agree _ h true⟩)
    (fun ⟨_, atTrue⟩ => nomatch atTrue)

/-- **Never occurring is not verifiable**: the run of `false` throughout adheres to its
complement. -/
theorem never_not_verifiable : ¬ Verifiable (fun r : Run (process Bool) => ¬ Eventually r) :=
  not_verifiable_of_adheres (r := run fun _ => false)
    (fun h => ⟨splice (fun _ => false) h true, fun never =>
      never ⟨h, splice_after _ true (Nat.le_refl h)⟩, splice_agree _ h true⟩)
    (fun ⟨_, atTrue⟩ => nomatch atTrue)

end Sequences

/-- **Asked of every process, the reading of tests is refutable exactly under Markov's
principle.** The witness: the sequences, the test at `n` failing where the move is `true`; a
refuting horizon for a sequence not false throughout bounds a search for its `true`. -/
theorem refutable_passes_iff_markov :
    (∀ (S A : Type) (P : Process S A) (fails : Nat → Run P → Bool),
      ByPrefixes fails → Refutable (Passes fails)) ↔ Markov :=
  ⟨fun law s notFalse =>
    match law Unit Bool (Sequences.process Bool) (fun n r => r.act n)
        (fun n _ _ agree => agree.2 n (Nat.lt_succ_self n)) (Sequences.run s) notFalse with
    | ⟨h, blocked⟩ =>
      match false_below_or_true s h with
      | .inr found => found
      | .inl below => absurd (fun t =>
          match Nat.lt_or_ge t h with
          | .inl before => (if_pos before).trans (below t before)
          | .inr after => Sequences.splice_after s false after)
          (blocked (Sequences.splice s h false) (Sequences.splice_agree s h false)),
   fun markov _ _ _ _ byPrefixes => refutable_passes markov byPrefixes⟩

end Becoming
