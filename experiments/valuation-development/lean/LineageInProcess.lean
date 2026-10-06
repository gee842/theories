/-
  The generation ledger of the valuation study as an instance of the shared
  process law, and its connection to the renewal–closure theorem.

  7 October 2026. AI-authored formal companion to §17 of
  `_process/research/2026-10-05-generative-foundation-review/root-foundation/VALUATION-DEVELOPMENT-ARGUMENT.md`.
  Additive module; it changes no verified source. Core Lean 4 only.

  Three connections:
  A. Every actual history of every process satisfying the per-event support law
     (`AccountLaw`, U1; renamed SustainLaw in the project vocabulary) has a sustained
     ledger, and consecutive segments of one history are generations that inherit
     exactly: `Ledger.seq` is trace concatenation.
  B. Conversely, generation ledgers are the events of a process (`lineageProcess`)
     that satisfies U1. The lineage bound of §16 is then the U2 prefix bound
     (`support_trace_balance`) of that process, not a separate result.
  C. The renewal channel process (`channelProcess`) satisfies U1, so every window of
     every execution is a sustained generation. On that shared process the
     renewal–closure theorem decides which kinds a lineage can keep. Arrivals are
     opened by the organization's own tokens, but whether a kind is kept is decided by
     membership in a self-renewing population, not by the kind's own arrivals: a kind
     that falls short can be kept by another kind's arrivals, and a kind can lapse
     beside a closure that renews forever.
-/
import ValuationBridges
import ResourceContinuation
import RenewalCharacterization

namespace ValuationDevelopment

open Generative Generative.Conditional

/-! ## A. Ledgers of actual histories -/

section Histories

universe u v
variable {State : Type u} {Action : Type v} {P : Process State Action}

/-- The ledger of a segment of a history: totals enacted and arrived along it, and
the support held at its two ends. -/
def traceLedger (reserve : State → Nat) (s t : State) (enacted arrived : Nat) : Ledger :=
  { enacted := enacted, arrived := arrived, heldStart := reserve s, heldEnd := reserve t }

/-- Every actual history of a process satisfying U1 has a sustained ledger. -/
theorem history_ledger_sustained (reserve : State → Nat)
    {demand credit : State → Action → State → Nat} (law : AccountLaw P reserve demand credit)
    {s t : State} {as : List Action} {spent received count : Nat}
    (h : SupportTrace P demand credit s as t spent received count) :
    (traceLedger reserve s t spent received).Sustained :=
  support_trace_balance reserve law h

/-- Consecutive segments of one history are generations: the successor inherits
exactly what its predecessor holds at the end, and their succession is the ledger
of the concatenated history, which is again sustained. -/
theorem consecutive_segments_are_generations (reserve : State → Nat)
    {demand credit : State → Action → State → Nat} (law : AccountLaw P reserve demand credit)
    {s m t : State} {xs ys : List Action} {sp₁ r₁ c₁ sp₂ r₂ c₂ : Nat}
    (left : SupportTrace P demand credit s xs m sp₁ r₁ c₁)
    (right : SupportTrace P demand credit m ys t sp₂ r₂ c₂) :
    (traceLedger reserve m t sp₂ r₂).heldStart = (traceLedger reserve s m sp₁ r₁).heldEnd ∧
    (traceLedger reserve s m sp₁ r₁).seq (traceLedger reserve m t sp₂ r₂) =
      traceLedger reserve s t (sp₁ + sp₂) (r₁ + r₂) ∧
    (traceLedger reserve s t (sp₁ + sp₂) (r₁ + r₂)).Sustained :=
  ⟨rfl, rfl, history_ledger_sustained reserve law (support_trace_append left right)⟩

end Histories

/-! ## B. Generations are the events of a process satisfying U1 -/

/-- The lineage process: the state is the support held; an event is a sustained
generation that starts with no more than is held, and leaves what it holds at its
end. Starting with less than is held records support dissipated between generations. -/
def lineageProcess : Process Nat Ledger where
  step r g r' := g.heldStart ≤ r ∧ r' = g.heldEnd ∧ g.Sustained

theorem lineage_account_law :
    AccountLaw lineageProcess id (fun _ g _ => g.enacted) (fun _ g _ => g.arrived) := by
  intro r g r' ⟨hs, he, hg⟩
  unfold Ledger.Sustained at hg
  simp only [id]
  omega

theorem lineLedger_heldEnd_congr : ∀ (rest : List Ledger) (g g' : Ledger),
    g.heldEnd = g'.heldEnd → (lineLedger g rest).heldEnd = (lineLedger g' rest).heldEnd
  | [], _, _, h => h
  | h :: rest, g, g', _ => lineLedger_heldEnd_congr rest (g.seq h) (g'.seq h) rfl

/-- A line of sustained, inheriting generations is an actual history of the lineage
process, with totals equal to the line's totals. -/
theorem line_is_lineage_history : ∀ (rest : List Ledger) (g : Ledger) (r : Nat),
    g.heldStart ≤ r → g.Sustained → (∀ h ∈ rest, h.Sustained) → Inherits (g :: rest) →
    ∃ count, SupportTrace lineageProcess (fun _ g _ => g.enacted) (fun _ g _ => g.arrived)
      r (g :: rest) (lineLedger g rest).heldEnd
      (lineLedger g rest).enacted (lineLedger g rest).arrived count := by
  intro rest
  induction rest with
  | nil =>
    intro g r hr hg _ _
    refine ⟨credited g.arrived + 0, ?_⟩
    have := SupportTrace.cons (P := lineageProcess) (demand := fun _ g _ => g.enacted)
      (credit := fun _ g _ => g.arrived) (s := r) (m := g.heldEnd) (a := g)
      ⟨hr, rfl, hg⟩ (SupportTrace.nil g.heldEnd)
    simpa [lineLedger] using this
  | cons h rest ih =>
    intro g r hr hg hall hinh
    obtain ⟨hhg, hinh'⟩ := hinh
    obtain ⟨count, tr⟩ := ih h g.heldEnd hhg (hall h (List.mem_cons_self ..))
      (fun k hk => hall k (List.mem_cons_of_mem _ hk)) hinh'
    refine ⟨credited g.arrived + count, ?_⟩
    have step := SupportTrace.cons (P := lineageProcess) (demand := fun _ g _ => g.enacted)
      (credit := fun _ g _ => g.arrived) (s := r) (a := g) ⟨hr, rfl, hg⟩ tr
    have hend : (lineLedger g (h :: rest)).heldEnd = (lineLedger h rest).heldEnd :=
      lineLedger_heldEnd_congr rest (g.seq h) h rfl
    obtain ⟨e1, a1, _⟩ := lineLedger_fields (h :: rest) g
    obtain ⟨e2, a2, _⟩ := lineLedger_fields rest h
    rw [hend, e1, a1]
    rw [e2, a2] at step
    simpa [List.map_cons, List.sum_cons, Nat.add_assoc] using step

/-- The lineage bound of §16 recovered as the U2 prefix bound of the lineage
process: one law, applied to a different carrier. -/
theorem lineage_bound_is_prefix_bound (rest : List Ledger) (g : Ledger) (hg : g.Sustained)
    (hall : ∀ h ∈ rest, h.Sustained) (hinh : Inherits (g :: rest)) :
    (lineLedger g rest).Sustained := by
  obtain ⟨count, tr⟩ := line_is_lineage_history rest g g.heldStart (Nat.le_refl _) hg hall hinh
  have hb := support_trace_balance id lineage_account_law tr
  obtain ⟨_, _, hst⟩ := lineLedger_fields rest g
  unfold Ledger.Sustained
  simp only [id] at hb
  rw [hst]
  omega

/-- Positive demand in every generation needs unbounded arrivals along an endless
line: the core theorem `unbounded_demand_requires_unbounded_credit`, applied to the
lineage process. -/
theorem endless_demanding_line_needs_unbounded_arrivals
    (held : Nat → Nat) (gens : Nat → Ledger)
    (steps : ∀ n, lineageProcess.step (held n) (gens n) (held (n + 1)))
    (unit : ∀ n, 1 ≤ (gens n).enacted) :
    ∀ bound, ∃ length, bound < intervalTotal (fun n => (gens n).arrived) 0 length := by
  apply unbounded_demand_requires_unbounded_credit (P := lineageProcess) id
    (demand := fun _ g _ => g.enacted) (credit := fun _ g _ => g.arrived)
    lineage_account_law held gens steps
  intro bound
  exact ⟨bound + 1, Nat.lt_of_lt_of_le (Nat.lt_succ_self bound)
    (interval_total_unit_bound (quantity := fun n => (gens n).enacted) unit 0 (bound + 1))⟩

/-! ## C. The renewal channel process -/

section Channel

open Generative.Conditional.Renewal

universe w
variable {Kind : Type w}

/-- The renewal channel process satisfies U1: what a tick forms is demanded from the
reserve, and what arrives is opened by the live tokens of the organization itself. -/
theorem channel_account_law (law : ChannelLaw Kind) :
    AccountLaw (channelProcess law) (fun c => c.reserve)
      (fun _ births _ => formation law births) (fun c _ _ => opened law.rate c.tokens) :=
  fun _ _ _ step => step.2.1

/-- The ledger of the generation occupying ticks `a, …, a + L - 1` of an execution. -/
def generationLedger {law : ChannelLaw Kind} (X : Execution law) (a L : Nat) : Ledger :=
  { enacted := intervalTotal (fun n => formation law (X.ticks n)) a L,
    arrived := intervalTotal (fun n => opened law.rate (X.states n).tokens) a L,
    heldStart := (X.states a).reserve,
    heldEnd := (X.states (a + L)).reserve }

/-- Every window of every execution is a sustained generation. -/
theorem generation_sustained {law : ChannelLaw Kind} (X : Execution law) (a L : Nat) :
    (generationLedger X a L).Sustained :=
  execution_interval_balance (P := channelProcess law) (fun c => c.reserve)
    (demand := fun _ births _ => formation law births)
    (credit := fun c _ _ => opened law.rate c.tokens)
    (channel_account_law law) X.states X.ticks X.steps a L

theorem intervalTotal_split (q : Nat → Nat) (a L : Nat) : ∀ L',
    intervalTotal q a (L + L') = intervalTotal q a L + intervalTotal q (a + L) L'
  | 0 => rfl
  | L' + 1 => by
    show intervalTotal q a (L + L') + q (a + (L + L')) =
      intervalTotal q a L + (intervalTotal q (a + L) L' + q (a + L + L'))
    rw [intervalTotal_split q a L L', Nat.add_assoc a L L']
    omega

/-- Successive windows are successive generations: each inherits exactly, and
their succession is the ledger of the joined window. -/
theorem generations_succeed {law : ChannelLaw Kind} (X : Execution law) (a L L' : Nat) :
    (generationLedger X (a + L) L').heldStart = (generationLedger X a L).heldEnd ∧
    (generationLedger X a L).seq (generationLedger X (a + L) L') = generationLedger X a (L + L') := by
  refine ⟨rfl, ?_⟩
  simp only [generationLedger, Ledger.seq, intervalTotal_split, Nat.add_assoc]

/-- The lineage of an execution: generation `i` occupies ticks `i·L, …, (i+1)·L - 1`.
It is an actual history of the lineage process. -/
theorem execution_lineage {law : ChannelLaw Kind} (X : Execution law) (L : Nat) :
    ∀ i, lineageProcess.step (X.states (i * L)).reserve (generationLedger X (i * L) L)
      (X.states ((i + 1) * L)).reserve := by
  intro i
  refine ⟨Nat.le_refl _, ?_, generation_sustained X (i * L) L⟩
  simp only [generationLedger, Nat.succ_mul]

/-- **Lineage and renewal on one process.** With finitely many kinds: every
generation of every execution is sustained, successive generations inherit exactly,
and some lineage stays live forever exactly when the law has a self-renewing
population. -/
theorem lineage_renewal_theorem [DecidableEq Kind] (law : ChannelLaw Kind)
    (U : List Kind) (complete : ∀ k, k ∈ U) :
    (∀ (X : Execution law) (a L : Nat), (generationLedger X a L).Sustained ∧
      (generationLedger X (a + L) L).heldStart = (generationLedger X a L).heldEnd) ∧
    (RenewsForever law ↔ ∃ B, SelfRenewing law B) :=
  ⟨fun X a L => ⟨generation_sustained X a L, rfl⟩,
    renewal_closure_theorem law U complete⟩

/-- **Attribution is by population, not by kind.** Kind `false` of `danglingSupport`
falls short of its own formation demand (it opens 2 and demands 5), yet some lineage
keeps it forever, on arrivals opened by kind `true`. In `lapsingCorrection` the
closure renews forever while the correction kind it supports cannot be kept. Which
kinds a lineage keeps is decided by membership in a self-renewing population
(`renewal_keeping_theorem`), not by what each kind brings in. -/
theorem attribution_is_by_population :
    (danglingSupport.rate false * danglingSupport.span false + 1 ≤ danglingSupport.demand false ∧
      KeepsForever danglingSupport (fun k => k = false)) ∧
    (RenewsForever lapsingCorrection ∧ ¬ KeepsForever lapsingCorrection (fun k => k = true)) := by
  refine ⟨⟨dangling_closure_falls_short, ?_⟩, lapsing_closure_renews_forever,
    lapsing_correction_cannot_be_kept⟩
  have complete : ∀ k : Bool, k ∈ [false, true] := by intro k; cases k <;> simp
  refine (renewal_keeping_theorem danglingSupport [false, true] complete
    (fun k => k = false)).2 ?_
  refine ⟨[false, true, true, true, true, true], ⟨List.cons_ne_nil _ _, ?_, ?_⟩, false,
    List.mem_cons_self, rfl, by decide⟩
  · intro k _
    exact ⟨false, List.mem_cons_self, rfl, Nat.le_refl 2⟩
  · show 10 ≤ 32
    decide

end Channel

end ValuationDevelopment
