import Becoming.SecuredContent
import Becoming.RenewalBound
import Becoming.Witnesses

/-!
# A remaining-step certificate handed between revised rules along one history

Composition, not a new proof of renewal or of living significance: a remaining-step certificate
is handed between revised response rules along one actual history. Its rank measures the stated
realization bound, not ethical value or complexity. The realized form may vary. Actual step
occurrence, correspondence, permissible means and continuing historical requirements remain
supplied.

* **Handed-off progress.** Where each unfinished step lowers the current rule's certificate and
  the handoff to the next rule does not raise it, the handed certificate falls at every
  unfinished step (`handed_off_progress`), so a completion comes within the initial bound
  (`RenewalBound.renewal_within_rank_bound`), and with correspondence each admitted history forms,
  within the bound, living content absent before (`newContent_by_bound`); living significance
  makes it relevant, under `LivingSignificance`'s relevance parameter, which carries no valence
  (`securesNewContent_by_bound`), and so does the continuation
  condition (`securesNewContent_by_bound_of_unrestricted`,
  `revised_newContent_by_bound_of_unrestricted`), on runs of any process
  (`newContent_by_bound_on_runs`) and on a run of a frame (`Run.novel_by_handoff`,
  `Run.relevance_by_handoff_of_unrestricted`).
* **Revised rules can fail for ever.** In a local arrangement, every rule the revising run
  executes finishes when retained and lowers its own remaining count, yet no outcome ever forms
  (`revised_rules_can_fail_forever`, `fails_forever`): each revision resets the count from 1 to 2
  (`revision_resets_remaining`). The handoff condition is what excludes this.
* **A real revision changes the formed outcome** and still meets the handoff bound
  (`changed_form_with_valid_handoff`, `changed_form`); the formed outcome is not fixed
  (`realized_form_need_not_be_fixed`, `outcome_not_fixed`). This is not permission to replace a
  specifically owed outcome.

Ported from `OpenFutureRevision`, with the bridge's open-form revision section and the joins
`RuleRevisionTraces` and `RuleRevisionTracesInherited` (F3J, 18 October 2026). The periphery's
`boundedInventory` is the frame with no moves realizing the occurrences within the bound
(`boundedFrame`), with `living` its generative claims. Rules act through one process
(`process`), and the revising sequence is its run (`revising`). The periphery's `simp`,
`DecidableEq` and `decide` proofs are constructive here: `advance` and `remaining` are stated by
cases, with the same value at every argument. Every declaration has an empty axiom report.
-/

namespace Becoming

open Generative

namespace Handoff

/-! ## Handed-off progress -/

/-- **The handed certificate falls at every unfinished step.** -/
theorem handed_off_progress {S : Type} (states : Nat → S) (rank : Nat → S → Nat)
    (completed : Nat → Prop)
    (localStep : ∀ n, ¬ completed n → rank n (states (n + 1)) < rank n (states n))
    (handoff : ∀ n, ¬ completed n → rank (n + 1) (states (n + 1)) ≤ rank n (states (n + 1))) :
    ∀ n, ¬ completed n → rank (n + 1) (states (n + 1)) < rank n (states n) :=
  fun n open_ => Nat.lt_of_le_of_lt (handoff n open_) (localStep n open_)

/-- The occurrences formed within the bound, as a frame with no moves. An occurrence's meaning,
non-duplication and living interpretation are inputs. -/
def boundedFrame {H Q : Type} (appears : H → Nat → Q → Prop) (bound : Nat) : Frame H Unit Q :=
  ⟨Witnesses.halted _ _, fun h q => ∃ n, n ≤ bound ∧ appears h n q⟩

/-- **Generation by bound**: each admitted history forms, within the bound, living content absent
before it. -/
theorem newContent_by_bound {H S Q : Type} (admitted : H → Prop) (states : H → Nat → S)
    (rank : H → Nat → S → Nat) (completed : H → Nat → Prop)
    (decideEvent : ∀ h n, Decidable (completed h n)) (appears : H → Nat → Q → Prop)
    (living : Q → Prop) (before : H → Q → Prop) (bound : Nat)
    (initial : ∀ h, admitted h → rank h 0 (states h 0) ≤ bound)
    (localStep : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h n (states h (n + 1)) < rank h n (states h n))
    (handoff : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h (n + 1) (states h (n + 1)) ≤ rank h n (states h (n + 1)))
    (correspondence : ∀ h, admitted h → ∀ n, completed h n →
      ∃ q, living q ∧ appears h n q ∧ ¬ before h q) :
    ∀ h, admitted h → ∃ q, living q ∧ (boundedFrame appears bound).realized h q ∧ ¬ before h q :=
  fun h allowed =>
    match RenewalBound.renewal_within_rank_bound (fun n => rank h n (states h n)) (completed h)
        (decideEvent h)
        (handed_off_progress (states h) (rank h) (completed h) (localStep h allowed)
          (handoff h allowed)) bound 0 (initial h allowed) with
    | ⟨n, _, within, finished⟩ => match correspondence h allowed n finished with
      | ⟨q, alive, actual, fresh⟩ => ⟨q, alive, ⟨n, Nat.zero_add bound ▸ within, actual⟩, fresh⟩

/-- **The producer's output is the formation premise of secured new content.** This does not
establish all-things permission or a duty. -/
theorem securesNewContent_by_bound {H Q : Type} (admitted : H → Prop)
    (appears : H → Nat → Q → Prop) (living : Q → Prop) (before : H → Q → Prop) (bound : Nat)
    (relevance : H → Q → Prop) (g0 : LivingSignificance (boundedFrame appears bound) living relevance)
    (formed : ∀ h, admitted h → ∃ q, living q ∧ (boundedFrame appears bound).realized h q ∧
      ¬ before h q) :
    ∀ h, admitted h → ∃ q, relevance h q ∧ ¬ before h q :=
  SecuredContent.contingent_newContent (boundedFrame appears bound) living admitted before relevance
    g0 formed

/-- Under the continuation condition, the formed content falls under the relevance read from
significance (significance from every standpoint, with no valence). -/
theorem securesNewContent_by_bound_of_unrestricted {H Q F Pos : Type} (admitted : H → Prop)
    (appears : H → Nat → Q → Prop) (living : Q → Prop) (before : H → Q → Prop) (bound : Nat)
    {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig) (formation : Q → F)
    (step : Q → Nat)
    (formed : ∀ h, admitted h → ∃ q, living q ∧ (boundedFrame appears bound).realized h q ∧
      ¬ before h q) :
    ∀ h, admitted h → ∃ q,
      (boundedFrame appears bound).relevance living sig formation step h q ∧ ¬ before h q :=
  securesNewContent_by_bound admitted appears living before bound _
    (livingSignificance_of_unrestricted (boundedFrame appears bound) living unrestricted formation step) formed

/-- **Producer to consumer**: every operational hypothesis of generation by bound retained, and
positive relevance obtained from significance. -/
theorem revised_newContent_by_bound_of_unrestricted {H S Q F Pos : Type} (admitted : H → Prop)
    (states : H → Nat → S) (rank : H → Nat → S → Nat) (completed : H → Nat → Prop)
    (decideEvent : ∀ h n, Decidable (completed h n)) (appears : H → Nat → Q → Prop)
    (living : Q → Prop) (before : H → Q → Prop) (bound : Nat)
    (initial : ∀ h, admitted h → rank h 0 (states h 0) ≤ bound)
    (localStep : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h n (states h (n + 1)) < rank h n (states h n))
    (handoff : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h (n + 1) (states h (n + 1)) ≤ rank h n (states h (n + 1)))
    (correspondence : ∀ h, admitted h → ∀ n, completed h n →
      ∃ q, living q ∧ appears h n q ∧ ¬ before h q)
    {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig) (formation : Q → F)
    (step : Q → Nat) :
    ∀ h, admitted h → ∃ q,
      (boundedFrame appears bound).relevance living sig formation step h q ∧ ¬ before h q :=
  securesNewContent_by_bound_of_unrestricted admitted appears living before bound unrestricted
    formation step
    (newContent_by_bound admitted states rank completed decideEvent appears living before bound
      initial localStep handoff correspondence)

/-- **Generation by bound on a family of runs** of any process, the histories being the runs'
configurations. -/
theorem newContent_by_bound_on_runs {S A H Q F Pos : Type} {P : Process S A} (r : H → Run P)
    (admitted : H → Prop) (rank : H → Nat → S → Nat) (completed : H → Nat → Prop)
    (decideEvent : ∀ h n, Decidable (completed h n)) (appears : H → Nat → Q → Prop)
    (living : Q → Prop) (before : H → Q → Prop) (bound : Nat)
    (initial : ∀ h, admitted h → rank h 0 ((r h).state 0) ≤ bound)
    (localStep : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h n ((r h).state (n + 1)) < rank h n ((r h).state n))
    (handoff : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h (n + 1) ((r h).state (n + 1)) ≤ rank h n ((r h).state (n + 1)))
    (correspondence : ∀ h, admitted h → ∀ n, completed h n →
      ∃ q, living q ∧ appears h n q ∧ ¬ before h q)
    {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig) (formation : Q → F)
    (step : Q → Nat) :
    ∀ h, admitted h → ∃ q,
      (boundedFrame appears bound).relevance living sig formation step h q ∧ ¬ before h q :=
  revised_newContent_by_bound_of_unrestricted admitted (fun h => (r h).state) rank completed
    decideEvent appears living before bound initial localStep handoff correspondence unrestricted
    formation step

/-- **Along a run of a frame**, the handed certificate gives new realization within the bound.
Completion-to-realization correspondence stays a visible premise; a bound `B` allows at most
`B + 1` steps. -/
theorem Run.novel_by_handoff {S A Q : Type} (M : Frame S A Q) (r : Run M.P) (living : Q → Prop)
    (before : S → Q → Prop) (rank : Nat → S → Nat) (completed : Nat → Prop)
    (decision : ∀ n, Decidable (completed n)) (bound : Nat) (initial : rank 0 (r.state 0) ≤ bound)
    (localStep : ∀ n, ¬ completed n → rank n (r.state (n + 1)) < rank n (r.state n))
    (handoff : ∀ n, ¬ completed n → rank (n + 1) (r.state (n + 1)) ≤ rank n (r.state (n + 1)))
    (correspondence : ∀ n, completed n → Novel M living before (r.state (n + 1))) :
    ∃ n, n ≤ bound ∧ Novel M living before (r.state (n + 1)) :=
  match RenewalBound.renewal_within_rank_bound (fun n => rank n (r.state n)) completed decision
      (handed_off_progress r.state rank completed localStep handoff) bound 0 initial with
  | ⟨n, _, within, finished⟩ => ⟨n, Nat.zero_add bound ▸ within, correspondence n finished⟩

/-- The same realized witness falls under the relevance read from significance, under the
continuation condition. Its form
is not fixed in advance or across runs. -/
theorem Run.relevance_by_handoff_of_unrestricted {S A Q F Pos : Type} (M : Frame S A Q)
    (r : Run M.P) (living : Q → Prop) (before : S → Q → Prop) (rank : Nat → S → Nat)
    (completed : Nat → Prop) (decision : ∀ n, Decidable (completed n)) (bound : Nat)
    (initial : rank 0 (r.state 0) ≤ bound)
    (localStep : ∀ n, ¬ completed n → rank n (r.state (n + 1)) < rank n (r.state n))
    (handoff : ∀ n, ¬ completed n → rank (n + 1) (r.state (n + 1)) ≤ rank n (r.state (n + 1)))
    (correspondence : ∀ n, completed n → Novel M living before (r.state (n + 1)))
    {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig) (formation : Q → F)
    (step : Q → Nat) :
    ∃ n, n ≤ bound ∧ ∃ q,
      M.relevance living sig formation step (r.state (n + 1)) q ∧ ¬ before (r.state (n + 1)) q :=
  match Run.novel_by_handoff M r living before rank completed decision bound initial localStep
      handoff correspondence with
  | ⟨n, within, q, alive, real, fresh⟩ =>
    ⟨n, within, q, livingSignificance_of_unrestricted M living unrestricted formation step _ q alive real, fresh⟩

/-! ## Revised rules in a local arrangement

Two unfinished configurations and two formed outcomes: stages of shared activity, not
independent value owners. -/

inductive Stage where
  | leftReady | rightReady | formedLeft | formedRight

inductive Rule where
  | left | right | directRight

def completed (s : Stage) : Prop := s = .formedLeft ∨ s = .formedRight

def advance : Rule → Stage → Stage
  | _, .formedLeft => .formedLeft
  | _, .formedRight => .formedRight
  | .left, .leftReady => .rightReady
  | .right, .leftReady => .formedRight
  | .directRight, .leftReady => .formedRight
  | .right, .rightReady => .leftReady
  | .left, .rightReady => .formedLeft
  | .directRight, .rightReady => .formedRight

def remaining : Rule → Stage → Nat
  | _, .formedLeft => 0
  | _, .formedRight => 0
  | .left, .leftReady => 2
  | .right, .leftReady => 1
  | .directRight, .leftReady => 1
  | .right, .rightReady => 2
  | .left, .rightReady => 1
  | .directRight, .rightReady => 1

/-- **Each rule retained finishes within two steps.** -/
theorem each_fixed_rule_finishes (p : Rule) (s : Stage) : completed (advance p (advance p s)) := by
  cases p <;> cases s
  all_goals first | exact .inl rfl | exact .inr rfl

/-- **Each rule's unfinished step lowers its own remaining count.** -/
theorem each_rule_local_progress (p : Rule) (s : Stage) (unfinished : ¬ completed (advance p s)) :
    remaining p (advance p s) < remaining p s := by
  cases p <;> cases s
  all_goals first
    | exact absurd (.inl rfl) unfinished
    | exact absurd (.inr rfl) unfinished
    | exact Nat.lt_succ_self 1

def restartChoice : Stage → Rule
  | .leftReady => .left
  | .rightReady => .right
  | .formedLeft => .directRight
  | .formedRight => .directRight

def revisingRun : Nat → Stage
  | 0 => .leftReady
  | n + 1 => advance (restartChoice (revisingRun n)) (revisingRun n)

theorem revising_run_stays_unfinished : ∀ n,
    revisingRun n = .leftReady ∨ revisingRun n = .rightReady
  | 0 => .inl rfl
  | n + 1 => match revising_run_stays_unfinished n with
    | .inl h => .inr (by
        show advance (restartChoice (revisingRun n)) (revisingRun n) = _
        rw [h]; rfl)
    | .inr h => .inl (by
        show advance (restartChoice (revisingRun n)) (revisingRun n) = _
        rw [h]; rfl)

theorem revising_unfinished (n : Nat) : ¬ completed (revisingRun n) :=
  fun done => match revising_run_stays_unfinished n, done with
  | .inl h, .inl e => nomatch h.symm.trans e
  | .inl h, .inr e => nomatch h.symm.trans e
  | .inr h, .inl e => nomatch h.symm.trans e
  | .inr h, .inr e => nomatch h.symm.trans e

/-- **Revised rules can fail for ever**: every executed step belongs to a rule that finishes
when retained and lowers that rule's own remaining count, yet no outcome ever forms. -/
theorem revised_rules_can_fail_forever :
    (∀ n, completed (advance (restartChoice (revisingRun n))
      (advance (restartChoice (revisingRun n)) (revisingRun n)))) ∧
    (∀ n, remaining (restartChoice (revisingRun n)) (revisingRun (n + 1)) <
      remaining (restartChoice (revisingRun n)) (revisingRun n)) ∧
    (∀ n, ¬ completed (revisingRun n)) :=
  ⟨fun _ => each_fixed_rule_finishes _ _,
   fun n => each_rule_local_progress _ _ (revising_unfinished (n + 1)), revising_unfinished⟩

/-- **Each revision resets the remaining count** from 1 to 2. -/
theorem revision_resets_remaining (n : Nat) :
    remaining (restartChoice (revisingRun n)) (revisingRun (n + 1)) = 1 ∧
    remaining (restartChoice (revisingRun (n + 1))) (revisingRun (n + 1)) = 2 := by
  show remaining (restartChoice (revisingRun n))
      (advance (restartChoice (revisingRun n)) (revisingRun n)) = 1 ∧
    remaining (restartChoice (advance (restartChoice (revisingRun n)) (revisingRun n)))
      (advance (restartChoice (revisingRun n)) (revisingRun n)) = 2
  cases revising_run_stays_unfinished n with
  | inl h => rw [h]; exact ⟨rfl, rfl⟩
  | inr h => rw [h]; exact ⟨rfl, rfl⟩

/-- **A real revision changes the ensuing formed outcome and still meets the handoff bound**:
after the first left-rule step, the direct-right rule completes instead. This is not permission
to replace a specifically owed left outcome. -/
theorem changed_form_with_valid_handoff :
    advance .left .leftReady = .rightReady ∧
    remaining .directRight .rightReady ≤ remaining .left .rightReady ∧
    advance .directRight .rightReady = .formedRight ∧
    advance .left .rightReady = .formedLeft :=
  ⟨rfl, Nat.le_refl 1, rfl, rfl⟩

def realizes (s : Stage) (q : Bool) : Prop :=
  if q then s = .formedRight else s = .formedLeft

/-- **The realized form need not be fixed.** -/
theorem realized_form_need_not_be_fixed :
    (∀ p : Bool, ∃ q, realizes (advance (if p then .directRight else .left) .rightReady) q) ∧
    ¬ ∃ q, ∀ p : Bool, realizes (advance (if p then .directRight else .left) .rightReady) q :=
  ⟨fun p => ⟨p, by cases p <;> rfl⟩,
   fun ⟨q, all⟩ => match q, all with
    | false, all => nomatch (all true : Stage.formedRight = .formedLeft)
    | true, all => nomatch (all false : Stage.formedLeft = .formedRight)⟩

/-! ## The rules as actions of one process -/

/-- Each rule as one action: the step under a rule is that rule's advance. -/
def process : Process Stage Rule := ⟨fun s p t => t = advance p s⟩

/-- The process with the outcome each configuration realizes. -/
def frame : Frame Stage Rule Bool := ⟨process, realizes⟩

theorem step_iff {s t : Stage} {p : Rule} : process.step s p t ↔ t = advance p s := Iff.rfl

/-- The revising sequence as a run: at each step the rule `restartChoice` gives. -/
def revising : Run process := ⟨revisingRun, fun n => restartChoice (revisingRun n), fun _ => rfl⟩

theorem revising_state (n : Nat) : revising.state n = revisingRun n := rfl

/-- **A revision changes the formed outcome within the handoff bound**, as traces. -/
theorem changed_form :
    Trace process .leftReady [.left, .directRight] .formedRight ∧
    Trace process .leftReady [.left, .left] .formedLeft ∧
    remaining .directRight .rightReady ≤ remaining .left .rightReady :=
  ⟨.cons rfl (.cons rfl (.nil _)), .cons rfl (.cons rfl (.nil _)), Nat.le_refl 1⟩

/-- **The formed outcome is not fixed**: from the right-ready configuration each of the two rules
is a one-step trace ending where some outcome is realized, and no outcome is realized at the end
of every such trace. -/
theorem outcome_not_fixed :
    (∀ p : Bool, ∃ t q, Trace process .rightReady [if p then .directRight else .left] t ∧
      frame.realized t q) ∧
    ¬ ∃ q, ∀ (p : Bool) t, Trace process .rightReady [if p then .directRight else .left] t →
      frame.realized t q :=
  ⟨fun p => match realized_form_need_not_be_fixed.1 p with
     | ⟨q, holds⟩ => ⟨_, q, trace_singleton_iff.mpr rfl, holds⟩,
   fun ⟨q, all⟩ => realized_form_need_not_be_fixed.2
     ⟨q, fun p => all p _ (trace_singleton_iff.mpr rfl)⟩⟩

/-- **Revised rules can fail for ever along the revising run.** -/
theorem fails_forever :
    (∀ n, completed (advance (revising.act n) (advance (revising.act n) (revising.state n)))) ∧
    (∀ n, remaining (revising.act n) (revising.state (n + 1)) <
      remaining (revising.act n) (revising.state n)) ∧
    (∀ n, ¬ completed (revising.state n)) :=
  revised_rules_can_fail_forever

/-- **Each revision resets the remaining count along the revising run.** -/
theorem resets_remaining (n : Nat) :
    remaining (revising.act n) (revising.state (n + 1)) = 1 ∧
      remaining (revising.act (n + 1)) (revising.state (n + 1)) = 2 :=
  revision_resets_remaining n

end Handoff

end Becoming
