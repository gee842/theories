import PredictionAction
import ProtocolComposition

/-!
An actual instance of finite paid protocol composition. Only completed trials of
PredictionAction's payable-write deterministic subprocess are summarized here.
The protocol excludes updater formation and reversal, both of which remain real
ready-state operations outside the trial. The command is checked before work,
then retained as the executed selector while writing may change the next command.
All memory, reserves and intermediate costs are the existing material-state fields.
No new register, sensor, completion guarantee or stochastic refinement is supplied.
-/
namespace PredictionProtocolBridge

open Generative Generative.Learning.Protocols PredictionAction

def trialProtocol (p : Parameters) : Protocol (process p) Bool where
  boundary s := s.phase = .ready ∧ s.score ≤ 4
  permits a s e _ := match e with
    | .rent | .work => a = command s
    | .write | .finish => a = s.physical.core.selector
    | .formUpdater _ | .reverse => False

abbrev Boundary (p : Parameters) := BoundaryState (trialProtocol p)

def nextEvent : Phase → Event
  | .ready => .rent
  | .rented => .work
  | .observed => .write
  | .written => .finish

def remainingEvents : Phase → List Event
  | .ready => cycleEvents
  | .rented => [.work, .write, .finish]
  | .observed => [.write, .finish]
  | .written => [.finish]

def remainingEnd (p : Parameters) (s : State) : State :=
  match s.phase with
  | .ready => cycleEnd p s
  | .rented => advance p (advance p (advance p s .work) .write) .finish
  | .observed => advance p (advance p s .write) .finish
  | .written => advance p s .finish

theorem committed_event {p : Parameters} {a : Bool} {s t : State} {e : Event}
    (h : (committed (trialProtocol p) a).step s e t) : e = nextEvent s.phase := by
  rcases h with ⟨⟨he, _⟩, hp⟩
  cases e with
  | formUpdater _ => exact False.elim hp
  | reverse => exact False.elim hp
  | rent => rw [he.1]; rfl
  | work => rw [he.1]; rfl
  | write => rw [he.1]; rfl
  | finish => rw [he.1]; rfl

theorem block_remaining_shape {p : Parameters} {a : Bool} {s t : State}
    {events : List Event} (h : BlockPath (trialProtocol p) a s events t)
    (hq : s.score ≤ 4) :
    events = remainingEvents s.phase ∧ t = remainingEnd p s := by
  induction h with
  | @finish s t e hs ht =>
      have he := committed_event hs
      have heq := hs.1.2
      subst e
      subst t
      cases hh : s.phase <;>
        simp_all [trialProtocol, nextEvent, advance, remainingEvents, remainingEnd]
  | @next s m t e events hs hn hb ih =>
      have hm := step_score_bounded hs.1 hq
      obtain ⟨hev, hte⟩ := ih hm
      have he := committed_event hs
      have heq := hs.1.2
      subst e
      subst m
      cases hh : s.phase <;>
        simp_all [trialProtocol, nextEvent, advance, remainingEvents, remainingEnd, cycleEnd, cycleEvents]

/-- A physically completed cycle returns with the inherited score invariant. -/
theorem cycle_boundary {p : Parameters} {s : State}
    (hq : s.score ≤ 4) (hc : CycleEnabled p s) :
    (trialProtocol p).boundary (cycleEnd p s) := by
  exact ⟨rfl, trace_score_bounded (paid_cycle p s hc) hq⟩

theorem cycle_block {p : Parameters} {s : State} {a : Bool}
    (hq : s.score ≤ 4) (ha : a = command s) (hc : CycleEnabled p s) :
    BlockPath (trialProtocol p) a s cycleEvents (cycleEnd p s) := by
  apply BlockPath.next (m := advance p s .rent)
  · exact ⟨⟨hc.1, rfl⟩, ha⟩
  · simp [trialProtocol, advance]
  apply BlockPath.next (m := advance p (advance p s .rent) .work)
  · exact ⟨⟨hc.2.1, rfl⟩, ha⟩
  · simp [trialProtocol, advance]
  apply BlockPath.next (m := advance p (advance p (advance p s .rent) .work) .write)
  · exact ⟨⟨hc.2.2.1, rfl⟩, ha⟩
  · simp [trialProtocol, advance]
  apply BlockPath.finish
  · exact ⟨⟨hc.2.2.2, rfl⟩, ha⟩
  · exact cycle_boundary hq hc

theorem cycle_trace_enabled {p : Parameters} {s t : State}
    (h : PredictionAction.Trace p s cycleEvents t) : CycleEnabled p s := by
  obtain ⟨s₁, h₁, ht₁⟩ := trace_cons_iff.mp h
  obtain ⟨s₂, h₂, ht₂⟩ := trace_cons_iff.mp ht₁
  obtain ⟨s₃, h₃, ht₃⟩ := trace_cons_iff.mp ht₂
  obtain ⟨s₄, h₄, _⟩ := trace_cons_iff.mp ht₃
  have hs₁ := h₁.2
  have hs₂ := h₂.2
  have hs₃ := h₃.2
  subst s₁; subst s₂; subst s₃
  exact ⟨h₁.1, h₂.1, h₃.1, h₄.1⟩

/-- No extra protocol assumption: actual phases force the four-event trial. -/
theorem blockPath_iff_cycle {p : Parameters} {s t : State} {a : Bool}
    {events : List Event} (hs : (trialProtocol p).boundary s) :
    BlockPath (trialProtocol p) a s events t ↔
      a = command s ∧ CycleEnabled p s ∧ events = cycleEvents ∧ t = cycleEnd p s := by
  constructor
  · intro h
    have shape := block_remaining_shape h hs.2
    have hw : events = cycleEvents := by simpa [remainingEvents, hs.1] using shape.1
    have he : t = cycleEnd p s := by simpa [remainingEnd, hs.1] using shape.2
    have hc := cycle_trace_enabled (hw ▸ blockPath_micro_trace h)
    have hcomm := blockPath_committed_trace h
    rw [hw] at hcomm
    obtain ⟨_, hfirst, _⟩ := trace_cons_iff.mp hcomm
    exact ⟨hfirst.2, hc, hw, he⟩
  · rintro ⟨ha, hc, rfl, rfl⟩
    exact cycle_block hs.2 ha hc

/-- The plant response, not a controller access to its hidden regime. -/
def macroReceipt (s : State) (a : Bool) : Bool := receiptOf a s.physical.core.regime true

def postWorkFuel (p : Parameters) (s : State) (a : Bool) : Nat :=
  if macroReceipt s a then
    s.physical.core.fuel - p.rent - p.base.selector.trial + p.base.selector.packet - maintenance p
  else s.physical.core.fuel - p.rent - p.base.selector.trial

/-- Explicit sequential affordability, including writing after the actual return. -/
def macroGuard (p : Parameters) (s : State) (a : Bool) : Prop :=
  s.phase = .ready ∧ 0 < s.physical.core.lease ∧ 0 < s.physical.moduleLease ∧
  p.rent + p.base.selector.trial ≤ s.physical.core.fuel ∧
  0 < s.physical.core.packets ∧ p.writing ≤ postWorkFuel p s a

/-- Direct arithmetic macro law; no block relation occurs in this definition. -/
def macroEnd (p : Parameters) (s : State) (a : Bool) : State :=
  { s with
    phase := .ready, receipt := false,
    score := revisedScore s.physical.directed s.score (decode a (macroReceipt s a)),
    physical := { s.physical with
      moduleLease := if macroReceipt s a then p.base.moduleLifetime else s.physical.moduleLease - 1,
      core := { s.physical.core with
        fuel := postWorkFuel p s a - p.writing,
        packets := s.physical.core.packets - 1, selector := a,
        lease := if macroReceipt s a then p.base.selector.lifetime else s.physical.core.lease - 1 } } }

theorem cycle_enabled_iff_macroGuard (p : Parameters) (s : State) :
    CycleEnabled p s ↔ macroGuard p s (command s) := by
  simp only [CycleEnabled, PredictionAction.Enabled, advance, macroGuard, postWorkFuel,
    macroReceipt, capture, command, true_and]
  constructor
  · rintro ⟨⟨hphase, hlease, hmodule, hfuel⟩, ⟨_, _, hwork, hpacket⟩, hwrite, _⟩
    exact ⟨hphase, hlease, hmodule, by omega, hpacket, hwrite⟩
  · rintro ⟨hphase, hlease, hmodule, hstart, hpacket, hwrite⟩
    exact ⟨⟨hphase, hlease, hmodule, by omega⟩,
      ⟨hlease, hmodule, by omega, hpacket⟩, hwrite, hlease, hmodule⟩

theorem cycle_end_eq_macroEnd (p : Parameters) (s : State) :
    cycleEnd p s = macroEnd p s (command s) := by rfl

def macroProcess (p : Parameters) : Process (Boundary p) Bool where
  step s a t := a = command s.val ∧ macroGuard p s.val a ∧ t.val = macroEnd p s.val a

theorem completed_step_iff {p : Parameters} {s t : Boundary p} {a : Bool} :
    (blockProcess (trialProtocol p)).step s a t ↔
      a = command s.val ∧ CycleEnabled p s.val ∧ t.val = cycleEnd p s.val := by
  constructor
  · rintro ⟨events, hb⟩
    obtain ⟨ha, hc, _, he⟩ := (blockPath_iff_cycle s.property).mp hb
    exact ⟨ha, hc, he⟩
  · rintro ⟨ha, hc, he⟩
    exact ⟨cycleEvents, (blockPath_iff_cycle s.property).mpr ⟨ha, hc, rfl, he⟩⟩

theorem macro_step_iff_completed {p : Parameters} {s t : Boundary p} {a : Bool} :
    (macroProcess p).step s a t ↔ (blockProcess (trialProtocol p)).step s a t := by
  rw [completed_step_iff]
  change (a = command s.val ∧ macroGuard p s.val a ∧ t.val = macroEnd p s.val a) ↔ _
  constructor
  · rintro ⟨rfl, hg, ht⟩
    exact ⟨rfl, (cycle_enabled_iff_macroGuard p s.val).mpr hg,
      ht.trans (cycle_end_eq_macroEnd p s.val).symm⟩
  · rintro ⟨rfl, hg, ht⟩
    exact ⟨rfl, (cycle_enabled_iff_macroGuard p s.val).mp hg,
      ht.trans (cycle_end_eq_macroEnd p s.val)⟩

theorem macro_trace_iff_realization (p : Parameters) (s t : Boundary p) (actions : List Bool) :
    Generative.Trace (macroProcess p) s actions t ↔
      ∃ micro, Realization (trialProtocol p) s actions t micro := by
  rw [← block_trace_iff_realization]
  constructor
  · exact trace_map (f := id) (fun _ _ _ h => macro_step_iff_completed.mp h)
  · exact trace_map (f := id) (fun _ _ _ h => macro_step_iff_completed.mpr h)

/-- Every actual realized trial contributes exactly four represented phase events. -/
theorem realization_event_count {p : Parameters} {s t : Boundary p}
    {actions : List Bool} {micro : List Event}
    (h : Realization (trialProtocol p) s actions t micro) : micro.length = 4 * actions.length := by
  induction h with
  | nil => rfl
  | @cons s m t a actions block rest hb hr ih =>
      have hw := ((blockPath_iff_cycle s.property).mp hb).2.2.1
      simp only [hw, List.length_append, List.length_cons, List.length_nil, cycleEvents] at *
      omega

/-- Each completed physical trial consumes one inherited finite source packet. -/
theorem realization_source_consumption {p : Parameters} {s t : Boundary p}
    {actions : List Bool} {micro : List Event}
    (h : Realization (trialProtocol p) s actions t micro) :
    t.val.physical.core.packets + actions.length = s.val.physical.core.packets := by
  induction h with
  | nil => simp
  | @cons s m t a actions block rest hb hr ih =>
      obtain ⟨_, hc, _, he⟩ := (blockPath_iff_cycle s.property).mp hb
      have hpos := ((cycle_enabled_iff_macroGuard p s.val).mp hc).2.2.2.2.1
      have hm : m.val.physical.core.packets = s.val.physical.core.packets - 1 := by
        rw [he]
        rfl
      simp only [List.length_cons]
      omega

/-- The macro summary inherits the actual finite source and every micro expense. -/
theorem realized_energy_material {p : Parameters} {s t : Boundary p}
    {actions : List Bool} {micro : List Event}
    (hp : UpdaterFormation.Admissible p.base)
    (h : Realization (trialProtocol p) s actions t micro) :
    energy p t.val + spentAlong p s.val micro = energy p s.val ∧
      t.val.physical.material = s.val.physical.material := by
  have ht := realization_micro_trace h
  exact ⟨trace_energy_ledger hp ht, trace_material_preserved ht⟩

/-- Prefix cuts retain their actual intermediate state, even inside a trial. -/
theorem realized_prefix_ledger {p : Parameters} {s t : Boundary p}
    {actions : List Bool} {before after : List Event}
    (hp : UpdaterFormation.Admissible p.base)
    (h : Realization (trialProtocol p) s actions t (before ++ after)) :
    ∃ m, PredictionAction.Trace p s.val before m ∧ PredictionAction.Trace p m after t.val ∧
      energy p m + spentAlong p s.val before = energy p s.val ∧
      energy p t.val + spentAlong p m after = energy p m := by
  obtain ⟨m, h₁, h₂⟩ := trace_append_iff.mp (realization_micro_trace h)
  exact ⟨m, h₁, h₂, trace_energy_ledger hp h₁, trace_energy_ledger hp h₂⟩

end PredictionProtocolBridge

#print axioms PredictionProtocolBridge.committed_event
#print axioms PredictionProtocolBridge.block_remaining_shape
#print axioms PredictionProtocolBridge.cycle_boundary
#print axioms PredictionProtocolBridge.cycle_block
#print axioms PredictionProtocolBridge.cycle_trace_enabled
#print axioms PredictionProtocolBridge.blockPath_iff_cycle
#print axioms PredictionProtocolBridge.cycle_enabled_iff_macroGuard
#print axioms PredictionProtocolBridge.cycle_end_eq_macroEnd
#print axioms PredictionProtocolBridge.completed_step_iff
#print axioms PredictionProtocolBridge.macro_step_iff_completed
#print axioms PredictionProtocolBridge.macro_trace_iff_realization
#print axioms PredictionProtocolBridge.realization_event_count
#print axioms PredictionProtocolBridge.realization_source_consumption
#print axioms PredictionProtocolBridge.realized_energy_material
#print axioms PredictionProtocolBridge.realized_prefix_ledger
