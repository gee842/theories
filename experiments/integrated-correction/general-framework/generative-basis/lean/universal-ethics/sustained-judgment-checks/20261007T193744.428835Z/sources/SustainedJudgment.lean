import LivingAllocation
import PracticalJudgment

/-! A finite-horizon connection from actual catalytic activity to collective
judgment. Material accounts are local counts, not welfare weights. The repeated
recipe has no damage, rate, spatial or stochastic law; it proves neither living
sufficiency nor an infinite continuation. J2/J4 and correspondence remain explicit.
-/
namespace SustainedJudgment

open Generative Generative.LivingOrganization PracticalJudgment

/-- An active pool with declared remaining substrate/support and realized output. -/
def stock (c s f p w : Nat) : Inventory Component
  | .active => c
  | .substrate => s
  | .support => f
  | .product => p
  | .spent => w
  | _ => 0

theorem production_step (c s f p w : Nat) (hc : 0 < c) :
    (process exampleRecipes allRoutes).step
      (stock c (s+1) (f+1) p w) .produce (stock c s f (p+1) (w+1)) := by
  refine ⟨trivial, ?_, ?_⟩ <;> intro x <;> cases x <;>
    simp [exampleRecipes, stock] <;> omega

/-- Arbitrarily long separately provisioned histories, not one infinite reserve. -/
theorem sustained_production (n c s f p w : Nat) (hc : 0 < c) :
    Trace (process exampleRecipes allRoutes)
      (stock c (s+n) (f+n) p w) (List.replicate n .produce)
      (stock c s f (p+n) (w+n)) := by
  induction n generalizing p w with
  | zero => simpa using (Trace.nil (stock c s f p w))
  | succ n ih =>
    have first := production_step c (s+n) (f+n) p w hc
    have tail := ih (p+1) (w+1)
    have joined := Trace.cons first tail
    simpa [List.replicate_succ, Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using joined

/-- Every actual history in this repeated-recipe family retains the catalyst and
consumes substrate/support once per operation. No inference from an endpoint label. -/
theorem production_account {before after : Inventory Component} {n : Nat}
    (h : Trace (process exampleRecipes allRoutes) before
      (List.replicate n .produce) after) :
    after .active = before .active ∧
    after .substrate + n = before .substrate ∧
    after .support + n = before .support ∧
    after .product = before .product + n := by
  induction n generalizing before with
  | zero =>
    have eq := trace_nil_iff.mp h
    subst after
    simp
  | succ n ih =>
    obtain ⟨middle, first, rest⟩ := trace_cons_iff.mp h
    have tail := ih rest
    have ca := first.2.2 Component.active
    have cs := first.2.2 Component.substrate
    have cf := first.2.2 Component.support
    have cp := first.2.2 Component.product
    simp [exampleRecipes] at ca cs cf cp
    exact ⟨by omega, by omega, by omega, by omega⟩

theorem positive_production_requires_competence {before after : Inventory Component}
    {n : Nat} (hn : 0 < n)
    (h : Trace (process exampleRecipes allRoutes) before
      (List.replicate n .produce) after) : 0 < before .active := by
  cases n with
  | zero => omega
  | succ n =>
    obtain ⟨_, first, _⟩ := trace_cons_iff.mp h
    have guard := first.2.1 Component.active
    simpa [exampleRecipes] using guard

def Sustains (n : Nat) (before : Inventory Component) : Prop :=
  ∃ after, Trace (process exampleRecipes allRoutes) before
    (List.replicate n .produce) after

theorem exact_finite_requirements (n c s f : Nat) (hn : 0 < n) :
    Sustains n (stock c s f 0 0) ↔ 0 < c ∧ n ≤ s ∧ n ≤ f := by
  constructor
  · rintro ⟨after, h⟩
    have account := production_account h
    have comp := positive_production_requires_competence hn h
    simp only [stock] at account comp
    exact ⟨comp, by omega, by omega⟩
  · rintro ⟨hc, hs, hf⟩
    have actual := sustained_production n c (s-n) (f-n) 0 0 hc
    have es : s-n+n=s := by omega
    have ef : f-n+n=f := by omega
    exact ⟨_, by simpa only [es, ef] using actual⟩

theorem insufficient_support_fails (n c s f : Nat) (hf : f < n) :
    ¬ Sustains n (stock c s f 0 0) := by
  rintro ⟨after, h⟩
  have account := (production_account h).2.2.1
  simp only [stock] at account
  omega

/-- Protection has substantive independently justified content. The comparator
condition requires an eligible restoration retaining EVERY other basic claim. -/
theorem frontier_sustains {H C G : Type}
    (eligible : H → Prop) (protect : H → C → Prop) (gain : H → G → Prop)
    (target : H → Prop) (claim : C)
    (meaning : ∀ a, protect a claim ↔ target a)
    (restoration : ∀ a, eligible a → ¬ target a →
      ∃ b, eligible b ∧ Included (protect a) (protect b) ∧ target b)
    {a : H} (chosen : Frontier eligible (Better protect gain) a) : target a := by
  classical
  apply Classical.byContradiction
  intro failed
  obtain ⟨b, hb, keep, success⟩ := restoration a chosen.1 failed
  exact chosen.2 b hb (protection_anchor keep claim
    ((meaning b).mpr success) (fun h => failed ((meaning a).mp h)))

/-- Existence of a frontier is a separate obligation (e.g. existing finite-menu
result), so impossible demands never yield requirements by empty quantification. -/
theorem collective_sustaining_requirement {H C G : Type}
    (eligible : H → Prop) (protect : H → C → Prop) (gain : H → G → Prop)
    (target : H → Prop) (claim : C)
    (meaning : ∀ a, protect a claim ↔ target a)
    (restoration : ∀ a, eligible a → ¬ target a →
      ∃ b, eligible b ∧ Included (protect a) (protect b) ∧ target b)
    (existsChoice : ∃ a, Frontier eligible (Better protect gain) a) :
    Required (Frontier eligible (Better protect gain)) target :=
  ⟨existsChoice, fun _ h => frontier_sustains eligible protect gain target claim meaning restoration h⟩

/-- Actual histories supply the means constraints for an already justified
collective requirement; contributor assignment is deliberately absent. -/
theorem collective_material_and_competence {H : Type} (ad : H → Prop)
    (c s f : H → Nat) (n : Nat) (hn : 0 < n)
    (warrant : Required ad (fun a => Sustains n (stock (c a) (s a) (f a) 0 0))) :
    Required ad (fun a => 0 < c a ∧ n ≤ s a ∧ n ≤ f a) := by
  apply necessary_means_required warrant
  intro a _ h
  exact (exact_finite_requirements n (c a) (s a) (f a) hn).mp h

/-- The general recipe theorem also applies where preservation is impossible
and reconstruction or import must precede a needed operation. -/
theorem collective_entry_after_loss {H : Type} (ad : H → Prop)
    (initial before after : H → Inventory Component) (word : H → List Operation)
    (absent : ∀ a, ad a → ¬ Present organizingPool (initial a))
    (warrant : Required ad (fun a =>
      Trace (process exampleRecipes allRoutes) (initial a) (word a) (before a) ∧
      (process exampleRecipes allRoutes).step (before a) .produce (after a))) :
    Required ad (fun a => EntryOccurs exampleRecipes allRoutes organizingPool
      (initial a) (word a) (before a)) := by
  apply necessary_means_required warrant
  intro a ha h
  apply operation_after_empty_state_requires_entry exampleRecipes allRoutes organizingPool
    (absent a ha) h.1 h.2
  simp [Touches, exampleRecipes, organizingPool]

/-! Joint allocation witness. These are pre-positioned, finite support units.
The two coordinates are differentiated contributions to the same process;
permission, transport, other needs, competence and substrate must be checked
before treating a pair as an eligible real plan. -/
def Joint (n leftCap rightCap : Nat) (p : Nat × Nat) : Prop :=
  p.1 ≤ leftCap ∧ p.2 ≤ rightCap ∧ n ≤ p.1 + p.2

theorem joint_plan_has_actual_history {n l r : Nat} {p : Nat × Nat}
    (hn : 0 < n) (h : Joint n l r p) :
    Sustains n (stock 1 n (p.1+p.2) 0 0) :=
  (exact_finite_requirements n 1 n (p.1+p.2) hn).mpr ⟨by omega, by omega, h.2.2⟩

theorem joint_feasible_iff (n l r : Nat) :
    (∃ p, Joint n l r p) ↔ n ≤ l+r := by
  constructor
  · rintro ⟨p, hp⟩
    unfold Joint at hp
    omega
  · intro h
    exact ⟨(l,r), by exact ⟨Nat.le_refl _, Nat.le_refl _, h⟩⟩

theorem joint_shortfall_no_unlimited_duty {n l r : Nat} (h : l+r<n)
    (task : Nat × Nat → Prop) : ¬ Required (Joint n l r) task := by
  apply impossible_menu_no_duty
  intro p hp
  have possible := (joint_feasible_iff n l r).mp ⟨p,hp⟩
  omega

theorem alternating_contributors_preserve_choice (n : Nat) (hn : 0 < n) :
    Required (Joint n n n) (fun p => 0 < p.1 ∨ 0 < p.2) ∧
    ¬ Required (Joint n n n) (fun p => 0 < p.1) ∧
    ¬ Required (Joint n n n) (fun p => 0 < p.2) := by
  have left : Joint n n n (n,0) := by simp [Joint]
  have right : Joint n n n (0,n) := by simp [Joint]
  refine ⟨⟨⟨(n,0),left⟩, ?_⟩, ?_, ?_⟩
  · intro p hp
    unfold Joint at hp
    omega
  · exact alternative_defeats_specific_duty right (by simp)
  · exact alternative_defeats_specific_duty left (by simp)

theorem sole_available_contribution_required (n : Nat) :
    Required (Joint n n 0) (fun p => n ≤ p.1) := by
  refine ⟨⟨(n,0), by simp [Joint]⟩, ?_⟩
  intro p hp
  unfold Joint at hp
  omega

/-- Two individually sustainable episodes can fail when joined without new
support. The same initial stock cannot be reset between them. -/
theorem isolated_success_not_joint_success :
    Sustains 1 (stock 1 2 1 0 0) ∧ ¬ Sustains 2 (stock 1 2 1 0 0) := by
  constructor
  · exact (exact_finite_requirements 1 1 2 1 (by decide)).mpr (by decide)
  · exact insufficient_support_fails 2 1 2 1 (by decide)

/-- A declared epoch permits at most one operation per competent unit.
This is an explicit local throughput law, not derived from stoichiometry.
Demand is a list of independently specified per-epoch outputs, including zero. -/
def Scheduled (c s f : Nat) : List Nat → Prop
  | [] => True
  | k :: ks => k ≤ c ∧ k ≤ s ∧ k ≤ f ∧ Scheduled c (s-k) (f-k) ks

theorem schedule_exact (ds : List Nat) (c s f : Nat) :
    Scheduled c s f ds ↔ ds.sum ≤ s ∧ ds.sum ≤ f ∧ ∀ k ∈ ds, k ≤ c := by
  induction ds generalizing s f with
  | nil => simp [Scheduled]
  | cons k ks ih =>
    simp only [Scheduled, ih, List.sum_cons, List.mem_cons]
    constructor
    · rintro ⟨hc, hs, hf, hss, hff, hr⟩
      refine ⟨by omega, by omega, ?_⟩
      intro x hx
      rcases hx with eq | hx
      · subst x; exact hc
      · exact hr x hx
    · rintro ⟨hs, hf, hr⟩
      exact ⟨hr k (Or.inl rfl), by omega, by omega, by omega, by omega,
        fun x hx => hr x (Or.inr hx)⟩

/-- The schedule has one actual concatenated reaction history; reserves are
carried across every epoch. A zero-demand epoch requires no productive event. -/
theorem scheduled_actual_history (ds : List Nat) (c s f p w : Nat)
    (h : Scheduled c s f ds) :
    Trace (process exampleRecipes allRoutes) (stock c s f p w)
      (List.replicate ds.sum .produce)
      (stock c (s-ds.sum) (f-ds.sum) (p+ds.sum) (w+ds.sum)) := by
  have bounds := (schedule_exact ds c s f).mp h
  by_cases positive : 0 < c
  · have trace := sustained_production ds.sum c (s-ds.sum) (f-ds.sum) p w positive
    have es : s-ds.sum+ds.sum=s := by omega
    have ef : f-ds.sum+ds.sum=f := by omega
    simpa only [es,ef] using trace
  · have sumzero : ds.sum = 0 := by
      induction ds with
      | nil => rfl
      | cons k ks ih =>
        have hk := bounds.2.2 k (by simp)
        have tail : Scheduled c s f ks := (schedule_exact ks c s f).mpr
          ⟨by simp only [List.sum_cons] at bounds; omega,
           by simp only [List.sum_cons] at bounds; omega,
           fun x hx => bounds.2.2 x (by simp [hx])⟩
        have hz := ih tail ((schedule_exact ks c s f).mp tail)
        simp only [List.sum_cons]; omega
    simp only [sumzero, Nat.sub_zero, Nat.add_zero, List.replicate_zero]
    exact Trace.nil _

theorem partial_competence_misses_deadline :
    Scheduled 2 2 2 [2] ∧ ¬ Scheduled 1 2 2 [2] ∧ Scheduled 1 2 2 [1,1] := by
  simp [Scheduled]

theorem zero_demand_does_not_require_competence : Scheduled 0 0 0 [0,0] := by simp [Scheduled]

theorem collective_schedule_constraints {H : Type} (ad : H → Prop)
    (c s f : H → Nat) (demand : H → List Nat)
    (warrant : Required ad (fun a => Scheduled (c a) (s a) (f a) (demand a))) :
    Required ad (fun a => (demand a).sum ≤ s a ∧ (demand a).sum ≤ f a ∧
      ∀ k ∈ demand a, k ≤ c a) := by
  apply necessary_means_required warrant
  intro a _ h
  exact (schedule_exact (demand a) (c a) (s a) (f a)).mp h

/-- Each labelled step is one declared service epoch, preserving the whole
batch trace and its competence bound. Epoch duration is supplied by calibration. -/
def timedProcess : Process (Inventory Component) Nat where
  step before k after := k ≤ before .active ∧
    Trace (process exampleRecipes allRoutes) before (List.replicate k .produce) after

theorem scheduled_timed_history (ds : List Nat) (c s f p w : Nat)
    (h : Scheduled c s f ds) :
    Trace timedProcess (stock c s f p w) ds
      (stock c (s-ds.sum) (f-ds.sum) (p+ds.sum) (w+ds.sum)) := by
  induction ds generalizing s f p w with
  | nil => simpa using (Trace.nil (stock c s f p w))
  | cons k ks ih =>
    obtain ⟨hc,hs,hf,tail⟩ := h
    have single : Scheduled c s f [k] := ⟨hc,hs,hf,trivial⟩
    have batch := scheduled_actual_history [k] c s f p w single
    simp only [List.sum_cons, List.sum_nil, Nat.add_zero] at batch
    have first : timedProcess.step (stock c s f p w) k
        (stock c (s-k) (f-k) (p+k) (w+k)) := ⟨hc,batch⟩
    have rest := ih (s-k) (f-k) (p+k) (w+k) tail
    have joined := Trace.cons first rest
    simpa [List.sum_cons, Nat.sub_sub, Nat.add_assoc] using joined

/-- End-to-end bridge over arbitrary candidate plans. Target protection,
restoration without another basic loss, and ethical eligibility are hypotheses.
The physical trace and all schedule constraints are consequences. -/
theorem judgment_to_sustained_history {H C G : Type}
    (eligible : H → Prop) (protect : H → C → Prop) (gain : H → G → Prop)
    (c s f : H → Nat) (ds : H → List Nat) (claim : C)
    (meaning : ∀ a, protect a claim ↔ Scheduled (c a) (s a) (f a) (ds a))
    (restoration : ∀ a, eligible a → ¬ Scheduled (c a) (s a) (f a) (ds a) →
      ∃ b, eligible b ∧ Included (protect a) (protect b) ∧
        Scheduled (c b) (s b) (f b) (ds b))
    (existsChoice : ∃ a, Frontier eligible (Better protect gain) a) :
    Required (Frontier eligible (Better protect gain)) (fun a =>
      (ds a).sum ≤ s a ∧ (ds a).sum ≤ f a ∧ (∀ k ∈ ds a, k ≤ c a) ∧
      Trace (process exampleRecipes allRoutes) (stock (c a) (s a) (f a) 0 0)
        (List.replicate (ds a).sum .produce)
        (stock (c a) (s a-(ds a).sum) (f a-(ds a).sum) (ds a).sum (ds a).sum)) := by
  have warrant := collective_sustaining_requirement eligible protect gain
    (fun a => Scheduled (c a) (s a) (f a) (ds a)) claim meaning restoration existsChoice
  apply necessary_means_required warrant
  intro a _ h
  have bounds := (schedule_exact (ds a) (c a) (s a) (f a)).mp h
  exact ⟨bounds.1, bounds.2.1, bounds.2.2,
    by simpa using scheduled_actual_history (ds a) (c a) (s a) (f a) 0 0 h⟩

inductive Choice where
  | left | right | withhold
  deriving DecidableEq

inductive Claim where
  | living | leftLife | rightLife
  deriving DecidableEq

def contribution : Choice → Nat × Nat
  | .left => (2,0)
  | .right => (0,2)
  | .withhold => (0,0)

def protects (a : Choice) : Claim → Prop
  | .living => Scheduled 1 2 ((contribution a).1 + (contribution a).2) [1,1]
  | .leftLife => (contribution a).1 ≤ 2
  | .rightLife => (contribution a).2 ≤ 2

/-- The optional realization is genuinely lost when either support route is used.
The two-unit spare-capacity classification is supplied, not a human burden metric. -/
def enrichment (a : Choice) (_ : Unit) : Prop := a = .withhold

theorem support_improves_protection (a : Choice) (ha : a ≠ .withhold) :
    Better protects enrichment a .withhold := by
  apply protection_anchor (c := Claim.living)
  · intro claim h
    cases a <;> cases claim <;> simp_all [protects, contribution, Scheduled]
  · cases a <;> simp_all [protects, contribution, Scheduled]
  · simp [protects, contribution, Scheduled]

theorem support_frontier (a : Choice) (ha : a ≠ .withhold) :
    Frontier (fun _ => True) (Better protects enrichment) a := by
  refine ⟨trivial, ?_⟩
  intro b _ h
  have allProtected : ∀ x, protects a x := by
    intro x; cases a <;> cases x <;> simp_all [protects, contribution, Scheduled]
  rcases h with h | h
  · exact h.2 (fun x _ => allProtected x)
  · have notOmit : b ≠ .withhold := by
      intro eq; subst b
      have living := h.1 Claim.living (allProtected Claim.living)
      simp [protects, contribution, Scheduled] at living
    apply h.2.2.2
    intro x hx
    exact False.elim (notOmit hx)

theorem actual_collective_choice_without_fixed_contributor :
    Required (Frontier (fun _ : Choice => True) (Better protects enrichment))
      (fun a => Scheduled 1 2 ((contribution a).1+(contribution a).2) [1,1]) ∧
    ¬ Required (Frontier (fun _ : Choice => True) (Better protects enrichment))
      (fun a => 0 < (contribution a).1) ∧
    ¬ Required (Frontier (fun _ : Choice => True) (Better protects enrichment))
      (fun a => 0 < (contribution a).2) := by
  have left := support_frontier .left (by decide)
  have right := support_frontier .right (by decide)
  refine ⟨⟨⟨.left,left⟩, ?_⟩, ?_, ?_⟩
  · intro a ha
    cases a with
    | left => simp [contribution, Scheduled]
    | right => simp [contribution, Scheduled]
    | withhold => exact False.elim (ha.2 .left trivial (support_improves_protection .left (by decide)))
  · exact alternative_defeats_specific_duty right (by simp [contribution])
  · exact alternative_defeats_specific_duty left (by simp [contribution])

theorem optional_loss_remains :
    enrichment .withhold () ∧ ¬ enrichment .left () ∧ ¬ enrichment .right () := by
  simp [enrichment]

/-- Connection to the concurrently completed general allocation result.
Arbitrary reaction families, changing organization and losses are retained.
The batch horizon remains untimed; its physical duration requires calibration. -/
theorem judgment_requires_organized_capacity {H C G Species Reaction : Type}
    [DecidableEq Species]
    (recipes : Reaction → Recipe Species) (allowed : Reaction → Prop)
    (participant : Species) (uses : Reaction → Nat)
    (requires : ∀ r, allowed r → uses r ≤ (recipes r).inputs.count participant)
    (eligible : H → Prop) (protect : H → C → Prop) (gain : H → G → Prop)
    (initial finalState : H → Inventory Species) (batches : H → List (List Reaction))
    (need : H → Nat) (claim : C)
    (meaning : ∀ a, protect a claim ↔
      Trace (LivingAllocation.batchProcess recipes allowed) (initial a) (batches a) (finalState a) ∧
      need a ≤ LivingAllocation.totalUses uses (batches a))
    (restoration : ∀ a, eligible a → ¬ protect a claim →
      ∃ b, eligible b ∧ Included (protect a) (protect b) ∧ protect b claim)
    (existsChoice : ∃ a, Frontier eligible (Better protect gain) a) :
    Required (Frontier eligible (Better protect gain)) (fun a =>
      Trace (process recipes allowed) (initial a) (batches a).flatten (finalState a) ∧
      need a ≤ (batches a).length * initial a participant +
        LivingAllocation.laterCredit recipes participant (batches a)) := by
  have warranted := collective_sustaining_requirement eligible protect gain
    (fun a => protect a claim) claim (fun _ => Iff.rfl) restoration existsChoice
  apply necessary_means_required warranted
  intro a _ ha
  obtain ⟨trace, enough⟩ := (meaning a).mp ha
  exact ⟨LivingAllocation.batches_serialize recipes allowed trace,
    Nat.le_trans enough (LivingAllocation.allocation_horizon_bound
      recipes allowed participant uses requires trace)⟩

/-- This is conditional necessity of prior increases, not a command to maximize
organization. Which route is justified still depends on other basic claims. -/
theorem above_retained_capacity_requires_change
    {requiredUses initialCount batches credit : Nat}
    (bound : requiredUses ≤ batches * initialCount + credit)
    (beyond : batches * initialCount < requiredUses) : 0 < credit := by omega

end SustainedJudgment
