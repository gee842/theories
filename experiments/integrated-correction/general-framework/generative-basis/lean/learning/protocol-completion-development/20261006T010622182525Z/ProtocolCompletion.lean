import ProtocolComposition

/-!
# Completion of an issued protocol under explicit progress conditions

Live is a supplied command-dependent domain of admitted unfinished executions,
not biological life or a success predicate. A contract includes the issued entry
even when it is already a boundary. Every permitted internal outcome must remain
Live and lower the rank. Enabledness supplies a next event but no physical clock,
scheduler, fairness, probability, free refusal report or resource reset.

An arbitrary stopped prefix need not have completed. The finite maximality
statement concerns a prefix with no enabled committed extension; the infinite
statement concerns an actual sequence of committed events. A scheduler allowed
to wait without events is outside this event-count claim.
-/

namespace Generative.Learning.Protocols.Completion

universe u v w x y z

variable {State : Type u} {MicroEvent : Type v} {Command : Type w}
variable {World : Type x} {Observation : Type y} {Memory : Type z}
variable {P : Process State MicroEvent} {I : Protocol P Command}
variable {Live : Command → State → Prop} {rank : State → Nat}

structure CompletionContract (I : Protocol P Command)
    (Live : Command → State → Prop) (rank : State → Nat) : Prop where
  next : ∀ a s, Live a s → ∃ e t, (committed I a).step s e t
  preserve : ∀ a s e t, Live a s → (committed I a).step s e t →
    ¬ I.boundary t → Live a t
  descend : ∀ a s e t, Live a s → (committed I a).step s e t →
    ¬ I.boundary t → rank t < rank s

/-- Every internal prefix keeps the progress premises at its actual endpoint. -/
theorem internal_prefix_live (law : CompletionContract I Live rank)
    {a : Command} {s t : State} {word : List MicroEvent}
    (trace : Trace (internalProcess I a) s word t) (start : Live a s) : Live a t := by
  induction trace with
  | nil => exact start
  | @cons s m t e es step rest ih =>
    exact ih (law.preserve a s e m start step.1 step.2)

theorem internal_prefix_rank (law : CompletionContract I Live rank)
    {a : Command} {s t : State} {word : List MicroEvent}
    (trace : Trace (internalProcess I a) s word t) (start : Live a s) :
    word.length + rank t ≤ rank s := by
  induction trace with
  | nil => simp
  | @cons s m t e es step rest ih =>
    have live := law.preserve a s e m start step.1 step.2
    have lower := law.descend a s e m start step.1 step.2
    have bound := ih live
    simp only [List.length_cons]
    omega

/-- Includes the zero-length prefix at the initial issued boundary. -/
theorem internal_prefix_has_extension (law : CompletionContract I Live rank)
    {a : Command} {s t : State} {word : List MicroEvent}
    (trace : Trace (internalProcess I a) s word t) (start : Live a s) :
    ∃ e u, (committed I a).step t e u := by
  exact law.next a t (internal_prefix_live law trace start)

/-- A finite unfinished prefix cannot be maximal by physical deadlock. -/
theorem no_unfinished_deadlocked_prefix (law : CompletionContract I Live rank)
    {a : Command} {s t : State} {word : List MicroEvent}
    (trace : Trace (internalProcess I a) s word t) (start : Live a s)
    (deadlock : ∀ e u, ¬ (committed I a).step t e u) : False := by
  obtain ⟨e, u, step⟩ := internal_prefix_has_extension law trace start
  exact deadlock e u step

/-- All possible completed blocks from the admitted domain obey the same bound. -/
theorem completed_block_bound (law : CompletionContract I Live rank)
    {a : Command} {s t : State} {word : List MicroEvent}
    (block : BlockPath I a s word t) (start : Live a s) :
    word.length ≤ rank s + 1 := by
  induction block with
  | finish => simp
  | @next s m t e es step inside tail ih =>
    have lower := law.descend a s e m start step inside
    have bound := ih (law.preserve a s e m start step inside)
    simp only [List.length_cons]
    omega

/-- A completed actual block exists; the maximality claims are not vacuous. -/
theorem completion_exists (law : CompletionContract I Live rank)
    {a : Command} {s : State} (start : Live a s) :
    ∃ word t, BlockPath I a s word t ∧ word.length ≤ rank s + 1 := by
  suffices aux : ∀ n, ∀ s : State, rank s = n → Live a s →
      ∃ word t, BlockPath I a s word t ∧ word.length ≤ rank s + 1 by
    exact aux (rank s) s rfl start
  intro n
  induction n using Nat.strongRecOn with
  | ind n ih =>
    intro s hr hs
    obtain ⟨e, t, step⟩ := law.next a s hs
    by_cases boundary : I.boundary t
    · exact ⟨[e], t, .finish step boundary, by simp⟩
    · have lower := law.descend a s e t hs step boundary
      obtain ⟨word, u, tail, bound⟩ :=
        ih (rank t) (by omega) t rfl (law.preserve a s e t hs step boundary)
      refine ⟨e :: word, u, .next step boundary tail, ?_⟩
      simp only [List.length_cons]
      omega

/-- No actual infinite execution can stay inside a single admitted block. -/
theorem no_infinite_internal_run (law : CompletionContract I Live rank)
    (a : Command) (states : Nat → State) (events : Nat → MicroEvent)
    (start : Live a (states 0))
    (steps : ∀ n, (internalProcess I a).step (states n) (events n) (states (n + 1))) :
    False := by
  have live : ∀ n, Live a (states n) := by
    intro n
    induction n with
    | zero => exact start
    | succ n ih => exact law.preserve a _ _ _ ih (steps n).1 (steps n).2
  have bound : ∀ n, n + rank (states n) ≤ rank (states 0) := by
    intro n
    induction n with
    | zero => omega
    | succ n ih =>
      have lower := law.descend a _ _ _ (live n) (steps n).1 (steps n).2
      omega
  have exceeded := bound (rank (states 0) + 1)
  omega

/-- A finite issued attempt stops at its first actual return or because no
committed extension exists. An arbitrary voluntarily stopped prefix is excluded. -/
def FiniteMaximalAttempt (I : Protocol P Command) (a : Command)
    (s : State) (word : List MicroEvent) (t : State) : Prop :=
  BlockPath I a s word t ∨
    (Trace (internalProcess I a) s word t ∧ ∀ e u, ¬ (committed I a).step t e u)

theorem finite_maximal_attempt_completes (law : CompletionContract I Live rank)
    {a : Command} {s t : State} {word : List MicroEvent}
    (start : Live a s) (attempt : FiniteMaximalAttempt I a s word t) :
    BlockPath I a s word t ∧ word.length ≤ rank s + 1 := by
  rcases attempt with block | ⟨unfinished, deadlock⟩
  · exact ⟨block, completed_block_bound law block start⟩
  · exact False.elim (no_unfinished_deadlocked_prefix law unfinished start deadlock)

/-- Completed histories append through their actual boundary and retained report. -/
theorem reported_realization_append
    {report : BoundaryState I → Command → BoundaryState I → Observation}
    {s m t : BoundaryState I} {left right : List (Command × Observation)}
    {before after : List MicroEvent}
    (historyPrefix : ReportedRealization I report s left m before)
    (suffix : ReportedRealization I report m right t after) :
    ReportedRealization I report s (left ++ right) t (before ++ after) := by
  induction historyPrefix with
  | nil => simpa using suffix
  | cons hb ho hp ih =>
    simpa [List.append_assoc] using ReportedRealization.cons hb ho (ih suffix)

/-- Completion supplies an actual reported reference step and inherited memory.
The existing LocalExact hypothesis supplies its semantic content; no arbitrary
outcome valuation is introduced by this theorem. -/
theorem issued_reference_completion
    (law : CompletionContract I Live rank)
    (report : BoundaryState I → Command → BoundaryState I → Observation)
    (C : Controller Memory Command Observation) (Q : Process World Command)
    (sense : World → Command → World → Observation)
    (decode : BoundaryState I → World × Memory)
    (exactness : Refinement.LocalExact (reportedProcess I report) (closedLoop C Q sense) decode)
    (s : BoundaryState I) (start : Live (C.choose (decode s).2) s.val) :
    ∃ t : BoundaryState I, ∃ word,
      BlockPath I (C.choose (decode s).2) s.val word t.val ∧
      word.length ≤ rank s.val + 1 ∧
      (closedLoop C Q sense).step (decode s)
        (C.choose (decode s).2, report s (C.choose (decode s).2) t) (decode t) := by
  obtain ⟨word, t, block, bound⟩ := completion_exists law start
  let target : BoundaryState I := ⟨t, blockPath_ends_at_boundary block⟩
  refine ⟨target, word, block, bound, ?_⟩
  exact (exactness s _ (decode target)).mpr
    ⟨target, ⟨⟨word, block⟩, rfl⟩, rfl⟩

/-- An existing reported history can take the next admitted command without
resetting its boundary, memory, source or previous micro-event word. -/
theorem reported_history_continues
    (law : CompletionContract I Live rank)
    (report : BoundaryState I → Command → BoundaryState I → Observation)
    (C : Controller Memory Command Observation) (Q : Process World Command)
    (sense : World → Command → World → Observation)
    (decode : BoundaryState I → World × Memory)
    (exactness : Refinement.LocalExact (reportedProcess I report) (closedLoop C Q sense) decode)
    {s m : BoundaryState I} {events : List (Command × Observation)} {before : List MicroEvent}
    (historyPrefix : ReportedRealization I report s events m before)
    (start : Live (C.choose (decode m).2) m.val) :
    ∃ t : BoundaryState I, ∃ word,
      ReportedRealization I report s
        (events ++ [(C.choose (decode m).2, report m (C.choose (decode m).2) t)])
        t (before ++ word) ∧ word.length ≤ rank m.val + 1 ∧
      (closedLoop C Q sense).step (decode m)
        (C.choose (decode m).2, report m (C.choose (decode m).2) t) (decode t) := by
  obtain ⟨t, word, block, bound, step⟩ :=
    issued_reference_completion law report C Q sense decode exactness m start
  have tail : ReportedRealization I report m
      [(C.choose (decode m).2, report m (C.choose (decode m).2) t)] t word := by
    simpa using (ReportedRealization.cons (report := report) block rfl (.nil t))
  exact ⟨t, word, reported_realization_append historyPrefix tail, bound, step⟩

/-- Each coordinate of a declared supporting account remains separate. The
actual prefix can end inside a block; no terminal credit prepays an earlier bill. -/
theorem reported_history_prefix_accounts {Index : Type}
    {report : BoundaryState I → Command → BoundaryState I → Observation}
    {s t : BoundaryState I} {events : List (Command × Observation)}
    {before after : List MicroEvent}
    (history : ReportedRealization I report s events t (before ++ after))
    (reserve : Index → State → Nat)
    (demand credit : Index → State → MicroEvent → State → Nat)
    (laws : ∀ i, Conditional.AccountLaw P (reserve i) (demand i) (credit i)) :
    ∃ m, ∀ i, ∃ d₁ c₁ k₁ d₂ c₂ k₂,
      Conditional.SupportTrace P (demand i) (credit i) s.val before m d₁ c₁ k₁ ∧
      Conditional.SupportTrace P (demand i) (credit i) m after t.val d₂ c₂ k₂ ∧
      d₁ + reserve i m ≤ reserve i s.val + c₁ ∧
      d₂ + reserve i t.val ≤ reserve i m + c₂ := by
  obtain ⟨m, hp, hs⟩ := trace_append_iff.mp
    (realization_micro_trace (reportedRealization_forget history))
  refine ⟨m, ?_⟩
  intro i
  obtain ⟨d₁, c₁, k₁, account₁⟩ := Conditional.trace_has_support_account (demand i) (credit i) hp
  obtain ⟨d₂, c₂, k₂, account₂⟩ := Conditional.trace_has_support_account (demand i) (credit i) hs
  exact ⟨d₁, c₁, k₁, d₂, c₂, k₂, account₁, account₂,
    Conditional.support_trace_balance (reserve i) (laws i) account₁,
    Conditional.support_trace_balance (reserve i) (laws i) account₂⟩

end Generative.Learning.Protocols.Completion

#print axioms Generative.Learning.Protocols.Completion.internal_prefix_live
#print axioms Generative.Learning.Protocols.Completion.internal_prefix_rank
#print axioms Generative.Learning.Protocols.Completion.internal_prefix_has_extension
#print axioms Generative.Learning.Protocols.Completion.no_unfinished_deadlocked_prefix
#print axioms Generative.Learning.Protocols.Completion.completed_block_bound
#print axioms Generative.Learning.Protocols.Completion.completion_exists
#print axioms Generative.Learning.Protocols.Completion.no_infinite_internal_run
#print axioms Generative.Learning.Protocols.Completion.finite_maximal_attempt_completes
#print axioms Generative.Learning.Protocols.Completion.reported_realization_append
#print axioms Generative.Learning.Protocols.Completion.issued_reference_completion
#print axioms Generative.Learning.Protocols.Completion.reported_history_continues
#print axioms Generative.Learning.Protocols.Completion.reported_history_prefix_accounts
