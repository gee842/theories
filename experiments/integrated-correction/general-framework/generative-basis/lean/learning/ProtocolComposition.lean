import ControlledRefinement
import Depletion

/-!
# Finite protocol blocks through actual intermediate states

A supplied protocol identifies boundary states and the micro-events permitted
under one committed command. A completed block contains at least one actual
micro-event and returns to a boundary for the first time. Its existence is not
an implementable scheduling strategy, a termination guarantee, or a timing law.
Intermediate interaction, sensing, interruption and memory changes must be
represented in the microstate/permissions if they occur; they are not erased by
calling a block atomic. The protocol and observation decoder remain supplied.

The controller implementation result decodes BOTH abstract world and memory
from each actual boundary microstate. It adds no free memory register. An
endpoint report can express a path-dependent observation only if the needed
record is retained in those boundary states. Exactness is a local contract to
be established for each concrete representative, not an inferred consequence of
the definitions. All histories here are finite and existential.

Resource conclusions inherit the actual micro-event AccountLaw. That law is a
net inequality; it does not establish prepayment, physical timing or solvency
before an event. Such restrictions must be guards or additional premises.
-/

namespace Generative.Learning.Protocols

universe u v w x y z

variable {State : Type u} {MicroEvent : Type v} {Command : Type w}
variable {World : Type x} {Observation : Type y} {Memory : Type z}

structure Protocol (P : Process State MicroEvent) (Command : Type w) where
  boundary : State → Prop
  permits : Command → State → MicroEvent → State → Prop

variable {P : Process State MicroEvent}

/-- The command stays fixed throughout a block. The permission law must explain
any physical latch, interrupted command or concurrent activity in an application. -/
def committed (I : Protocol P Command) (a : Command) : Process State MicroEvent where
  step s e t := P.step s e t ∧ I.permits a s e t

/-- A nonempty first-return block. A starting boundary is required separately by
the boundary-state type; recursive tails start at internal states. -/
inductive BlockPath (I : Protocol P Command) (a : Command) :
    State → List MicroEvent → State → Prop where
  | finish {s t : State} {e : MicroEvent} :
      (committed I a).step s e t → I.boundary t → BlockPath I a s [e] t
  | next {s m t : State} {e : MicroEvent} {events : List MicroEvent} :
      (committed I a).step s e m → ¬ I.boundary m →
      BlockPath I a m events t → BlockPath I a s (e :: events) t

def BoundaryState (I : Protocol P Command) := {s : State // I.boundary s}

def blockProcess (I : Protocol P Command) : Process (BoundaryState I) Command where
  step s a t := ∃ events, BlockPath I a s.val events t.val

theorem blockPath_nonempty {I : Protocol P Command} {a : Command}
    {s t : State} {events : List MicroEvent} (h : BlockPath I a s events t) :
    events ≠ [] := by
  cases h <;> simp

theorem blockPath_ends_at_boundary {I : Protocol P Command} {a : Command}
    {s t : State} {events : List MicroEvent} (h : BlockPath I a s events t) :
    I.boundary t := by
  induction h with
  | finish _ ht => exact ht
  | next _ _ _ ih => exact ih

theorem blockPath_committed_trace {I : Protocol P Command} {a : Command}
    {s t : State} {events : List MicroEvent} (h : BlockPath I a s events t) :
    Trace (committed I a) s events t := by
  induction h with
  | finish hs _ => exact .cons hs (.nil _)
  | next hs _ _ ih => exact .cons hs ih

theorem blockPath_micro_trace {I : Protocol P Command} {a : Command}
    {s t : State} {events : List MicroEvent} (h : BlockPath I a s events t) :
    Trace P s events t := by
  exact trace_map (P := committed I a) (Q := P) (f := fun s => s)
    (fun _ _ _ hs => hs.1) (blockPath_committed_trace h)

/-- Records the actual micro words and intermediate boundary representatives. -/
inductive Realization (I : Protocol P Command) :
    BoundaryState I → List Command → BoundaryState I → List MicroEvent → Prop where
  | nil (s : BoundaryState I) : Realization I s [] s []
  | cons {s m t : BoundaryState I} {a : Command} {actions : List Command}
      {block rest : List MicroEvent} :
      BlockPath I a s.val block m.val → Realization I m actions t rest →
      Realization I s (a :: actions) t (block ++ rest)

theorem realization_micro_trace {I : Protocol P Command}
    {s t : BoundaryState I} {actions : List Command} {events : List MicroEvent}
    (h : Realization I s actions t events) : Trace P s.val events t.val := by
  induction h with
  | nil s => exact .nil s.val
  | cons hb _ ih =>
    exact trace_append_iff.mpr ⟨_, blockPath_micro_trace hb, ih⟩

theorem realization_block_trace {I : Protocol P Command}
    {s t : BoundaryState I} {actions : List Command} {events : List MicroEvent}
    (h : Realization I s actions t events) : Trace (blockProcess I) s actions t := by
  induction h with
  | nil s => exact .nil s
  | cons hb _ ih => exact .cons ⟨_, hb⟩ ih

theorem block_trace_iff_realization (I : Protocol P Command)
    (s : BoundaryState I) (actions : List Command) (t : BoundaryState I) :
    Trace (blockProcess I) s actions t ↔ ∃ events, Realization I s actions t events := by
  constructor
  · intro h
    induction h with
    | nil s => exact ⟨[], .nil s⟩
    | cons hs _ ih =>
      obtain ⟨block, hb⟩ := hs
      obtain ⟨rest, hr⟩ := ih
      exact ⟨block ++ rest, .cons hb hr⟩
  · rintro ⟨_, h⟩
    exact realization_block_trace h

theorem realization_length_bound {I : Protocol P Command}
    {s t : BoundaryState I} {actions : List Command} {events : List MicroEvent}
    (h : Realization I s actions t events) : actions.length ≤ events.length := by
  induction h with
  | nil => simp
  | @cons s m t a actions block rest hb hr ih =>
    have hn : 0 < block.length := by
      cases block with
      | nil => exact False.elim (blockPath_nonempty hb rfl)
      | cons => simp
    simp only [List.length_cons, List.length_append]
    omega

/-- The report is delivered at completion. A path-dependent report requires an
adequate retained physical record in the states supplied to this function. -/
def reportedProcess (I : Protocol P Command)
    (report : BoundaryState I → Command → BoundaryState I → Observation) :
    Process (BoundaryState I) (Command × Observation) where
  step s e t := (blockProcess I).step s e.1 t ∧ e.2 = report s e.1 t

/-- Unlike an unlabelled flattening, this retains the report at every actual
boundary, so no different intermediate representative supplies an observation. -/
inductive ReportedRealization (I : Protocol P Command)
    (report : BoundaryState I → Command → BoundaryState I → Observation) :
    BoundaryState I → List (Command × Observation) → BoundaryState I →
      List MicroEvent → Prop where
  | nil (s : BoundaryState I) : ReportedRealization I report s [] s []
  | cons {s m t : BoundaryState I} {a : Command} {o : Observation}
      {events : List (Command × Observation)} {block rest : List MicroEvent} :
      BlockPath I a s.val block m.val → o = report s a m →
      ReportedRealization I report m events t rest →
      ReportedRealization I report s ((a, o) :: events) t (block ++ rest)

theorem reportedRealization_forget {I : Protocol P Command}
    {report : BoundaryState I → Command → BoundaryState I → Observation}
    {s t : BoundaryState I} {events : List (Command × Observation)}
    {micro : List MicroEvent} (h : ReportedRealization I report s events t micro) :
    Realization I s (events.map Prod.fst) t micro := by
  induction h with
  | nil s => exact .nil s
  | cons hb _ _ ih => exact .cons hb ih

theorem reportedRealization_trace {I : Protocol P Command}
    {report : BoundaryState I → Command → BoundaryState I → Observation}
    {s t : BoundaryState I} {events : List (Command × Observation)}
    {micro : List MicroEvent} (h : ReportedRealization I report s events t micro) :
    Trace (reportedProcess I report) s events t := by
  induction h with
  | nil s => exact .nil s
  | cons hb ho _ ih => exact .cons ⟨⟨_, hb⟩, ho⟩ ih

theorem reported_trace_iff_realization (I : Protocol P Command)
    (report : BoundaryState I → Command → BoundaryState I → Observation)
    (s : BoundaryState I) (events : List (Command × Observation)) (t : BoundaryState I) :
    Trace (reportedProcess I report) s events t ↔
      ∃ micro, ReportedRealization I report s events t micro := by
  constructor
  · intro h
    induction h with
    | nil s => exact ⟨[], .nil s⟩
    | @cons s m t e events hs ht ih =>
      obtain ⟨⟨block, hb⟩, ho⟩ := hs
      obtain ⟨rest, hr⟩ := ih
      obtain ⟨a, o⟩ := e
      exact ⟨block ++ rest, .cons hb ho hr⟩
  · rintro ⟨_, h⟩
    exact reportedRealization_trace h

/-- The decoder reads abstract world AND inherited memory from an actual
boundary microstate. The local implementation contract includes the command,
observation and update equations of the abstract closed loop; it is supplied
and must be proved for a concrete mechanism. No separate free memory is added. -/
theorem controller_trace_iff_implementation (I : Protocol P Command)
    (report : BoundaryState I → Command → BoundaryState I → Observation)
    (C : Controller Memory Command Observation) (Q : Process World Command)
    (sense : World → Command → World → Observation)
    (decode : BoundaryState I → World × Memory)
    (contract : Refinement.LocalExact (reportedProcess I report) (closedLoop C Q sense) decode)
    (s : BoundaryState I) (events : List (Command × Observation)) (r : World × Memory) :
    Trace (closedLoop C Q sense) (decode s) events r ↔
      ∃ t micro, ReportedRealization I report s events t micro ∧ decode t = r := by
  constructor
  · intro h
    obtain ⟨t, ht, heq⟩ := (local_exact_iff_trace_exact.mp contract s events r).mp h
    obtain ⟨micro, hm⟩ := (reported_trace_iff_realization I report s events t).mp ht
    exact ⟨t, micro, hm, heq⟩
  · rintro ⟨t, micro, hm, heq⟩
    exact (local_exact_iff_trace_exact.mp contract s events r).mpr
      ⟨t, reportedRealization_trace hm, heq⟩

/-- A realized block sequence inherits the actual micro-event resource account.
The report/update labels add no resources, and no event cost is manufactured. -/
theorem realization_support_bound {I : Protocol P Command}
    {s t : BoundaryState I} {actions : List Command} {events : List MicroEvent}
    (h : Realization I s actions t events)
    (reserve : State → Nat) (demand credit : State → MicroEvent → State → Nat)
    (law : Conditional.AccountLaw P reserve demand credit) :
    ∃ spent received count,
      Conditional.SupportTrace P demand credit s.val events t.val spent received count ∧
      spent + reserve t.val ≤ reserve s.val + received := by
  obtain ⟨spent, received, count, ht⟩ := Conditional.trace_has_support_account demand credit
    (realization_micro_trace h)
  exact ⟨spent, received, count, ht, Conditional.support_trace_balance reserve law ht⟩

/-- Any cut, including inside a block, keeps its actual inherited reserve and
both expense histories. Net balance alone does not certify event prepayment. -/
theorem realization_prefix_support {I : Protocol P Command}
    {s t : BoundaryState I} {actions : List Command} {before after : List MicroEvent}
    (h : Realization I s actions t (before ++ after))
    (reserve : State → Nat) (demand credit : State → MicroEvent → State → Nat)
    (law : Conditional.AccountLaw P reserve demand credit) :
    ∃ m spent₁ received₁ count₁ spent₂ received₂ count₂,
      Conditional.SupportTrace P demand credit s.val before m spent₁ received₁ count₁ ∧
      Conditional.SupportTrace P demand credit m after t.val spent₂ received₂ count₂ ∧
      spent₁ + reserve m ≤ reserve s.val + received₁ ∧
      spent₂ + reserve t.val ≤ reserve m + received₂ := by
  obtain ⟨m, hp, hs⟩ := trace_append_iff.mp (realization_micro_trace h)
  obtain ⟨d₁, c₁, k₁, hp'⟩ := Conditional.trace_has_support_account demand credit hp
  obtain ⟨d₂, c₂, k₂, hs'⟩ := Conditional.trace_has_support_account demand credit hs
  exact ⟨m, d₁, c₁, k₁, d₂, c₂, k₂, hp', hs',
    Conditional.support_trace_balance reserve law hp',
    Conditional.support_trace_balance reserve law hs'⟩

/-- A decreasing rank bounds the number of internal events of completed blocks.
This is not a completion theorem: a run could deadlock before its final event. -/
theorem block_length_bound {I : Protocol P Command} {a : Command}
    (rank : State → Nat)
    (decreases : ∀ s e t, (committed I a).step s e t →
      ¬ I.boundary t → rank t < rank s)
    {s t : State} {events : List MicroEvent} (h : BlockPath I a s events t) :
    events.length ≤ rank s + 1 := by
  induction h with
  | finish => simp
  | next hs hi _ ih =>
    have lower := decreases _ _ _ hs hi
    simp only [List.length_cons]
    omega

/-- Internal continuation deliberately excludes events reaching a boundary. -/
def internalProcess (I : Protocol P Command) (a : Command) : Process State MicroEvent where
  step s e t := (committed I a).step s e t ∧ ¬ I.boundary t

theorem internal_trace_rank_bound {I : Protocol P Command} {a : Command}
    (rank : State → Nat)
    (decreases : ∀ s e t, (committed I a).step s e t →
      ¬ I.boundary t → rank t < rank s)
    {s t : State} {events : List MicroEvent}
    (h : Trace (internalProcess I a) s events t) :
    events.length + rank t ≤ rank s := by
  exact trace_reserve_bound (P := internalProcess I a) rank
    (fun _ _ _ hs => decreases _ _ _ hs.1 hs.2) h

/-- Strict internal descent rules out an infinite internal run, but leaves
finite deadlock possible. It does not provide nonblocking or a physical clock. -/
theorem no_infinite_internal_execution {I : Protocol P Command} {a : Command}
    (rank : State → Nat)
    (decreases : ∀ s e t, (committed I a).step s e t →
      ¬ I.boundary t → rank t < rank s) :
    ¬ ∃ states : Nat → State, ∃ events : Nat → MicroEvent,
      ∀ n, (internalProcess I a).step (states n) (events n) (states (n + 1)) := by
  exact no_infinite_execution_under_depletion rank
    (fun _ _ _ hs => decreases _ _ _ hs.1 hs.2)

end Generative.Learning.Protocols

#print axioms Generative.Learning.Protocols.blockPath_nonempty
#print axioms Generative.Learning.Protocols.blockPath_ends_at_boundary
#print axioms Generative.Learning.Protocols.blockPath_committed_trace
#print axioms Generative.Learning.Protocols.blockPath_micro_trace
#print axioms Generative.Learning.Protocols.realization_micro_trace
#print axioms Generative.Learning.Protocols.realization_block_trace
#print axioms Generative.Learning.Protocols.block_trace_iff_realization
#print axioms Generative.Learning.Protocols.realization_length_bound
#print axioms Generative.Learning.Protocols.reportedRealization_forget
#print axioms Generative.Learning.Protocols.reportedRealization_trace
#print axioms Generative.Learning.Protocols.reported_trace_iff_realization
#print axioms Generative.Learning.Protocols.controller_trace_iff_implementation
#print axioms Generative.Learning.Protocols.realization_support_bound
#print axioms Generative.Learning.Protocols.realization_prefix_support
#print axioms Generative.Learning.Protocols.block_length_bound
#print axioms Generative.Learning.Protocols.internal_trace_rank_bound
#print axioms Generative.Learning.Protocols.no_infinite_internal_execution
