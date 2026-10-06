import ResourceContinuation

/-!
A necessary information interface for revision. A deterministic controller has
no access beyond its initial memory and the supplied observation channel.
Clock, resource readings, direct inputs and innovations must be included in that
channel or memory if the modeled update uses them. The update architecture is
supplied; these theorems do not derive its origin or optimality.
-/

namespace Generative.Learning

universe u v w x y

structure Controller (Memory : Type u) (Action : Type v) (Observation : Type w) where
  choose : Memory → Action
  revise : Memory → Observation → Memory

variable {Memory : Type u} {Action : Type v} {Observation : Type w}
variable {State : Type x} {Other : Type y}

def advance (C : Controller Memory Action Observation) : Memory → List Observation → Memory
  | m, [] => m
  | m, o :: os => advance C (C.revise m o) os

def issued (C : Controller Memory Action Observation) : Memory → List Observation → List Action
  | _, [] => []
  | m, o :: os => C.choose m :: issued C (C.revise m o) os

/-- Sensing uses the actual predecessor, chosen event and actual successor.
The successor memory is carried into the next event, without a reset. -/
def closedLoop (C : Controller Memory Action Observation) (P : Process State Action)
    (sense : State → Action → State → Observation) :
    Process (State × Memory) (Action × Observation) where
  step p e q := P.step p.1 e.1 q.1 ∧ e.1 = C.choose p.2 ∧
    e.2 = sense p.1 e.1 q.1 ∧ q.2 = C.revise p.2 e.2

theorem controlled_trace_world (C : Controller Memory Action Observation)
    (P : Process State Action) (sense : State → Action → State → Observation)
    {p q : State × Memory} {events : List (Action × Observation)}
    (h : Trace (closedLoop C P sense) p events q) :
    Trace P p.1 (events.map Prod.fst) q.1 := by
  induction h with
  | nil p => exact .nil p.1
  | cons hs _ ih => exact .cons hs.1 ih

theorem controlled_trace_memory (C : Controller Memory Action Observation)
    (P : Process State Action) (sense : State → Action → State → Observation)
    {p q : State × Memory} {events : List (Action × Observation)}
    (h : Trace (closedLoop C P sense) p events q) :
    q.2 = advance C p.2 (events.map Prod.snd) := by
  induction h with
  | nil p => rfl
  | cons hs _ ih =>
    simpa only [List.map_cons, advance, hs.2.2.2] using ih

theorem controlled_trace_commands (C : Controller Memory Action Observation)
    (P : Process State Action) (sense : State → Action → State → Observation)
    {p q : State × Memory} {events : List (Action × Observation)}
    (h : Trace (closedLoop C P sense) p events q) :
    events.map Prod.fst = issued C p.2 (events.map Prod.snd) := by
  induction h with
  | nil p => rfl
  | cons hs _ ih =>
    simpa only [List.map_cons, issued, hs.2.1, hs.2.2.2] using congrArg (List.cons _) ih

theorem same_feedback_same_memory (C : Controller Memory Action Observation)
    (P : Process State Action) (Q : Process Other Action)
    (senseP : State → Action → State → Observation)
    (senseQ : Other → Action → Other → Observation)
    {p q : State × Memory} {r s : Other × Memory}
    {left right : List (Action × Observation)}
    (hp : Trace (closedLoop C P senseP) p left q)
    (hq : Trace (closedLoop C Q senseQ) r right s)
    (hm : p.2 = r.2) (ho : left.map Prod.snd = right.map Prod.snd) :
    q.2 = s.2 := by
  rw [controlled_trace_memory C P senseP hp,
    controlled_trace_memory C Q senseQ hq, hm, ho]

theorem same_feedback_same_commands (C : Controller Memory Action Observation)
    (P : Process State Action) (Q : Process Other Action)
    (senseP : State → Action → State → Observation)
    (senseQ : Other → Action → Other → Observation)
    {p q : State × Memory} {r s : Other × Memory}
    {left right : List (Action × Observation)}
    (hp : Trace (closedLoop C P senseP) p left q)
    (hq : Trace (closedLoop C Q senseQ) r right s)
    (hm : p.2 = r.2) (ho : left.map Prod.snd = right.map Prod.snd) :
    left.map Prod.fst = right.map Prod.fst := by
  rw [controlled_trace_commands C P senseP hp,
    controlled_trace_commands C Q senseQ hq, hm, ho]

/-- A common history cannot choose an action supporting two incompatible actual
continuation tasks. The suffixes are external comparison tasks, not controller
inputs or an evaluative signal supplied to its update. Feasibility is existential,
so this does not assert robust success against nondeterministic outcomes. -/
theorem same_feedback_excludes_incompatible_futures
    (C : Controller Memory Action Observation)
    (P : Process State Action) (Q : Process Other Action)
    (senseP : State → Action → State → Observation)
    (senseQ : Other → Action → Other → Observation)
    {p q : State × Memory} {r s : Other × Memory}
    {left right : List (Action × Observation)} {suffixP suffixQ : List Action}
    (hp : Trace (closedLoop C P senseP) p left q)
    (hq : Trace (closedLoop C Q senseQ) r right s)
    (hm : p.2 = r.2) (ho : left.map Prod.snd = right.map Prod.snd)
    (hincompatible : ∀ a, Feasible P q.1 (a :: suffixP) →
      Feasible Q s.1 (a :: suffixQ) → False) :
    ¬ (Feasible P q.1 (C.choose q.2 :: suffixP) ∧
       Feasible Q s.1 (C.choose s.2 :: suffixQ)) := by
  intro h
  have heq := same_feedback_same_memory C P Q senseP senseQ hp hq hm ho
  rw [← heq] at h
  exact hincompatible _ h.1 h.2

theorem opposite_futures_require_feedback_difference
    (C : Controller Memory Action Observation)
    (P : Process State Action) (Q : Process Other Action)
    (senseP : State → Action → State → Observation)
    (senseQ : Other → Action → Other → Observation)
    {p q : State × Memory} {r s : Other × Memory}
    {left right : List (Action × Observation)} {suffixP suffixQ : List Action}
    (hp : Trace (closedLoop C P senseP) p left q)
    (hq : Trace (closedLoop C Q senseQ) r right s)
    (hm : p.2 = r.2)
    (hincompatible : ∀ a, Feasible P q.1 (a :: suffixP) →
      Feasible Q s.1 (a :: suffixQ) → False)
    (successP : Feasible P q.1 (C.choose q.2 :: suffixP))
    (successQ : Feasible Q s.1 (C.choose s.2 :: suffixQ)) :
    left.map Prod.snd ≠ right.map Prod.snd := by
  intro ho
  exact same_feedback_excludes_incompatible_futures C P Q senseP senseQ
    hp hq hm ho hincompatible ⟨successP, successQ⟩

/-- Adding a controller restricts the permitted world steps and preserves any
already justified resource law. This charges only costs present in P; sensing
or memory costs omitted from P are not manufactured by this theorem. -/
theorem closed_loop_account_law
    (C : Controller Memory Action Observation) (P : Process State Action)
    (sense : State → Action → State → Observation)
    (reserve : State → Nat) (demand credit : State → Action → State → Nat)
    (h : Conditional.AccountLaw P reserve demand credit) :
    Conditional.AccountLaw (closedLoop C P sense) (fun p => reserve p.1)
      (fun p e q => demand p.1 e.1 q.1)
      (fun p e q => credit p.1 e.1 q.1) := by
  intro p e q hs
  exact h _ _ _ hs.1

end Generative.Learning

#print axioms Generative.Learning.controlled_trace_world
#print axioms Generative.Learning.controlled_trace_memory
#print axioms Generative.Learning.controlled_trace_commands
#print axioms Generative.Learning.same_feedback_same_memory
#print axioms Generative.Learning.same_feedback_same_commands
#print axioms Generative.Learning.same_feedback_excludes_incompatible_futures
#print axioms Generative.Learning.opposite_futures_require_feedback_difference
#print axioms Generative.Learning.closed_loop_account_law
