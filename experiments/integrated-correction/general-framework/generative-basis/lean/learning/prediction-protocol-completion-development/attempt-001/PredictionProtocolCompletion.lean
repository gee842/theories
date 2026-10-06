import PredictionProtocolBridge
import ProtocolCompletion

/-!
# Completion of the unchanged payable predictor trial

The admitted domain is a decidable list of the actual remaining phase guards,
not an assertion that a completed path exists. Its resource checks retain the
actual post-receipt writing bill. Completion concerns one committed four-event
trial, excludes reversal/reformation during it, and supplies no physical clock.
Returned boundary states need not admit another trial. The total stochastic
exposure has different failed-write/source-expiry semantics and is not silently
identified with this relation.
-/

namespace PredictionProtocolCompletion

open Generative Generative.Learning.Protocols
open Generative.Learning.Protocols.Completion
open PredictionAction PredictionProtocolBridge

/-- Remaining bills and command latch, read from the existing physical state. -/
def phaseGuard (p : Parameters) (a : Bool) (s : State) : Prop :=
  match s.phase with
  | .ready => a = command s ∧ CycleEnabled p s
  | .rented => a = command s ∧ Enabled p s .work ∧
      Enabled p (advance p s .work) .write ∧
      Enabled p (advance p (advance p s .work) .write) .finish
  | .observed => a = s.physical.core.selector ∧ Enabled p s .write ∧
      Enabled p (advance p s .write) .finish
  | .written => a = s.physical.core.selector ∧ Enabled p s .finish

def Live (p : Parameters) (a : Bool) (s : State) : Prop :=
  s.score ≤ 4 ∧ phaseGuard p a s

def phaseRank (s : State) : Nat :=
  match s.phase with
  | .ready => 3
  | .rented => 2
  | .observed => 1
  | .written => 0

theorem live_entry_iff {p : Parameters} {a : Bool} {s : State}
    (ready : s.phase = .ready) :
    Live p a s ↔ s.score ≤ 4 ∧ a = command s ∧ macroGuard p s a := by
  simp only [Live, phaseGuard, ready]
  constructor
  · rintro ⟨hq, rfl, hc⟩
    exact ⟨hq, rfl, (cycle_enabled_iff_macroGuard p s).mp hc⟩
  · rintro ⟨hq, rfl, hg⟩
    exact ⟨hq, rfl, (cycle_enabled_iff_macroGuard p s).mpr hg⟩

theorem live_has_next {p : Parameters} {a : Bool} {s : State}
    (hs : Live p a s) :
    ∃ e t, (committed (trialProtocol p) a).step s e t := by
  have hg := hs.2
  cases hp : s.phase with
  | ready =>
    simp only [phaseGuard, hp] at hg
    exact ⟨.rent, advance p s .rent, ⟨⟨hg.2.1, rfl⟩, hg.1⟩⟩
  | rented =>
    simp only [phaseGuard, hp] at hg
    exact ⟨.work, advance p s .work, ⟨⟨hg.2.1, rfl⟩, hg.1⟩⟩
  | observed =>
    simp only [phaseGuard, hp] at hg
    exact ⟨.write, advance p s .write, ⟨⟨hg.2.1, rfl⟩, hg.1⟩⟩
  | written =>
    simp only [phaseGuard, hp] at hg
    exact ⟨.finish, advance p s .finish, ⟨⟨hg.2, rfl⟩, hg.1⟩⟩

theorem live_preserved_inside {p : Parameters} {a : Bool} {s t : State} {e : Event}
    (hs : Live p a s) (step : (committed (trialProtocol p) a).step s e t)
    (inside : ¬ (trialProtocol p).boundary t) : Live p a t := by
  have hq := step_score_bounded step.1 hs.1
  have he := committed_event step
  have ht := step.1.2
  subst e
  subst t
  refine ⟨hq, ?_⟩
  have hg := hs.2
  cases hp : s.phase <;>
    simp_all [phaseGuard, nextEvent, advance, command, CycleEnabled, trialProtocol]

theorem rank_decreases_inside {p : Parameters} {a : Bool} {s t : State} {e : Event}
    (hs : Live p a s) (step : (committed (trialProtocol p) a).step s e t)
    (inside : ¬ (trialProtocol p).boundary t) : phaseRank t < phaseRank s := by
  have hq := step_score_bounded step.1 hs.1
  have he := committed_event step
  have ht := step.1.2
  subst e
  subst t
  cases hp : s.phase <;>
    simp_all [phaseRank, nextEvent, advance, trialProtocol]

theorem payable_trial_contract (p : Parameters) :
    CompletionContract (trialProtocol p) (Live p) phaseRank := by
  exact ⟨fun _ _ => live_has_next, fun _ _ _ _ => live_preserved_inside,
    fun _ _ _ _ => rank_decreases_inside⟩

/-- The initial admission includes the first event despite starting at a boundary. -/
theorem admitted_trial_completes {p : Parameters} {a : Bool} {s : State}
    (entry : (trialProtocol p).boundary s) (issued : a = command s)
    (funded : macroGuard p s a) :
    ∃ word t, BlockPath (trialProtocol p) a s word t ∧
      word = cycleEvents ∧ t = cycleEnd p s ∧ word.length = 4 := by
  have live := (live_entry_iff entry.1).mpr ⟨entry.2, issued, funded⟩
  obtain ⟨word, t, block, _⟩ := completion_exists (payable_trial_contract p) live
  obtain ⟨_, _, hw, ht⟩ := (blockPath_iff_cycle entry).mp block
  exact ⟨word, t, block, hw, ht, by simp [hw, cycleEvents]⟩

/-- Any physically stopped unfinished prefix still has an enabled continuation. -/
theorem admitted_prefix_has_extension {p : Parameters} {a : Bool} {s t : State}
    {word : List Event} (entry : Live p a s)
    (prefix : Generative.Trace (internalProcess (trialProtocol p) a) s word t) :
    ∃ e u, (committed (trialProtocol p) a).step t e u :=
  internal_prefix_has_extension (payable_trial_contract p) prefix entry

theorem admitted_no_internal_deadlock {p : Parameters} {a : Bool} {s t : State}
    {word : List Event} (entry : Live p a s)
    (prefix : Generative.Trace (internalProcess (trialProtocol p) a) s word t)
    (maximal : ∀ e u, ¬ (committed (trialProtocol p) a).step t e u) : False :=
  no_unfinished_deadlocked_prefix (payable_trial_contract p) prefix entry maximal

theorem admitted_no_infinite_internal_run (p : Parameters) (a : Bool)
    (states : Nat → State) (events : Nat → Event)
    (entry : Live p a (states 0))
    (steps : ∀ n, (internalProcess (trialProtocol p) a).step
      (states n) (events n) (states (n + 1))) : False :=
  no_infinite_internal_run (payable_trial_contract p) a states events entry steps

end PredictionProtocolCompletion

#print axioms PredictionProtocolCompletion.live_entry_iff
#print axioms PredictionProtocolCompletion.live_has_next
#print axioms PredictionProtocolCompletion.live_preserved_inside
#print axioms PredictionProtocolCompletion.rank_decreases_inside
#print axioms PredictionProtocolCompletion.payable_trial_contract
#print axioms PredictionProtocolCompletion.admitted_trial_completes
#print axioms PredictionProtocolCompletion.admitted_prefix_has_extension
#print axioms PredictionProtocolCompletion.admitted_no_internal_deadlock
#print axioms PredictionProtocolCompletion.admitted_no_infinite_internal_run
