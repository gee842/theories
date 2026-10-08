import ScaleRevision
import PracticalJudgment

/-! Executed inquiry/response histories joined to scoped practical comparison.
The live cases, menu, threshold and protection priority are supplied. The model
is one joint process; possible readout biases are alternative descriptions of
its realization. No formation of those epistemic alternatives is proved. -/
namespace InquiryJudgment
noncomputable section
open ScaleRevision PracticalJudgment
open RemainingDependency (charge tariff decode)
set_option maxRecDepth 32768
set_option maxHeartbeats 4000000

/-- Work funding and workspace capacity are distinct from response supply. -/
theorem response_charge_succeeds (s : State)
    (capacity : max s.account.live 8 + 2 ≤ s.account.capacity)
    (funding : tariff s.account 1 8 2 0 0 ≤ s.account.fuel) :
    (charge s.account 1 8 2 0 0).2 = .none := by
  simp [charge, Nat.not_lt.mpr capacity, Nat.not_lt.mpr funding]

/-- Joins the old body-only result to the actually charged, phase-guarded event. -/
theorem funded_calibrated_response (cfg : Config) (θ : ℝ) (s : State)
    (active : s.stopped = false) (phase : s.phase = 3)
    (capacity : max s.account.live 8 + 2 ≤ s.account.capacity)
    (funding : tariff s.account 1 8 2 0 0 ≤ s.account.fuel)
    (ready : s.view.atStage = s.stage ∧ decode 0 false s.view.tag ≠ none ∧
      dose s.view θ cfg.allowance ≤ s.source)
    (calibrated : |(s.a - loss s) - forecast s.view| ≤ cfg.allowance) :
    θ ≤ (advance cfg θ s .respond).a ∧
    (advance cfg θ s .respond).phase = 4 ∧
    (advance cfg θ s .respond).stopped = false ∧
    (advance cfg θ s .respond).b = s.b := by
  have charged := response_charge_succeeds s capacity funding
  have hprotected := calibrated_response_margin s.view (s.a - loss s) θ cfg.allowance calibrated
  simpa [advance, active, phase, paid, charged, respondBody, ready, loss] using
    (show θ ≤ s.a - loss s + dose s.view θ cfg.allowance ∧ True from ⟨hprotected, trivial⟩)

/-- Correspondence, calibration and feasibility must hold at the actual live case. -/
theorem robust_execution_at_actual {W : Type} (live : W → Prop)
    (cfg : W → Config) (state : W → State) (θ : ℝ) (actual : W)
    (truth : live actual)
    (certificate : ∀ w, live w →
      (state w).stopped = false ∧ (state w).phase = 3 ∧
      max (state w).account.live 8 + 2 ≤ (state w).account.capacity ∧
      tariff (state w).account 1 8 2 0 0 ≤ (state w).account.fuel ∧
      ((state w).view.atStage = (state w).stage ∧
        decode 0 false (state w).view.tag ≠ none ∧
        dose (state w).view θ (cfg w).allowance ≤ (state w).source) ∧
      |((state w).a - loss (state w)) - forecast (state w).view| ≤ (cfg w).allowance) :
    θ ≤ (advance (cfg actual) θ (state actual) .respond).a := by
  obtain ⟨ha,hp,hc,hf,hr,he⟩ := certificate actual truth
  exact (funded_calibrated_response _ _ _ ha hp hc hf hr he).1

inductive Case where | accurate | biased deriving DecidableEq
inductive Plan where | measured | margin | fixed deriving DecidableEq
inductive Claim where | continuation | companion deriving DecidableEq

def config (w : Case) (p : Plan) : Config :=
  {bias := if w = .biased then -3 else 0,
   allowance := if p = .margin then 3 else 0}

def events (p : Plan) : List Event :=
  inquiry ++ [if p = .fixed then .fixedRespond else .respond]

def outcome (fuel : Nat) (supply : ℝ) (w : Case) (p : Plan) : State :=
  run (config w p) 1 (entrance fuel supply) (events p)

/-- Endpoint claim includes enacted response and the shared stage-four deadline.
Denial stuttering at an earlier apparently healthy state cannot satisfy it. -/
def holds (s : State) : Claim → Prop
  | .continuation => 1 ≤ s.a ∧ s.phase = 4 ∧ s.stage = 4 ∧ s.stopped = false
  | .companion => 3 ≤ s.b ∧ 0 ≤ s.source

def protects (live : Case → Prop) (p : Plan) (c : Claim) : Prop :=
  Robust live (fun w p => holds (outcome 4176 1 w p) c) p

def chosen {G : Type} (live : Case → Prop) (gain : Plan → G → Prop) (p : Plan) : Prop :=
  Frontier (fun _ => True) (Better (protects live) gain) p

def both (_ : Case) : Prop := True
def accurateOnly (w : Case) : Prop := w = .accurate

/-- Every candidate denotes an actual inherited event trace, including failures. -/
theorem outcome_is_trace (fuel : Nat) (supply : ℝ) (w : Case) (p : Plan) :
    Generative.Trace (SystemsOrganization.deterministic (advance (config w p) 1))
      (entrance fuel supply) (events p) (outcome fuel supply w p) :=
  run_is_core_trace _ _ _ _

theorem all_work_accounted (fuel : Nat) (supply : ℝ) (w : Case) (p : Plan) :
    workTotal (outcome fuel supply w p) = fuel := by
  exact (run_work_conserved _ _ _ _).trans (by simp [workTotal, entrance])

/-- Six exact executions, not an empirical or universal sensor calibration. -/
theorem continuation_table (w : Case) (p : Plan) :
    holds (outcome 4176 1 w p) .continuation ↔
      p = .fixed ∨ (w = .accurate ∧ p = .measured) ∨ (w = .biased ∧ p = .margin) := by
  cases w <;> cases p <;>
    simp [holds, outcome, config, events] <;>
    norm_num [run, inquiry, SystemsOrganization.evolve,
      advance, entrance, paid, charge, tariff, probeBody, inspectBody, reviseBody,
      respondBody, fixedBody, total, drift, loss, decode, forecast, dose] <;> simp

theorem companion_retained (w : Case) (p : Plan) :
    holds (outcome 4176 1 w p) .companion := by
  cases w <;> cases p <;>
    simp [holds, outcome, config, events] <;>
    norm_num [run, inquiry, SystemsOrganization.evolve,
      advance, entrance, paid, charge, tariff, probeBody, inspectBody, reviseBody,
      respondBody, fixedBody, total, drift, loss, decode, forecast, dose] <;> simp

theorem fixed_protects (live : Case → Prop) (c : Claim) : protects live .fixed c := by
  intro w _
  cases c with
  | continuation => exact (continuation_table w .fixed).mpr (Or.inl rfl)
  | companion => exact companion_retained _ _

theorem robust_continuation_iff (p : Plan) :
    protects both p .continuation ↔ p = .fixed := by
  constructor
  · intro h
    have ha := (continuation_table .accurate p).mp (h .accurate trivial)
    have hb := (continuation_table .biased p).mp (h .biased trivial)
    cases p <;> simp_all
  · rintro rfl
    exact fixed_protects _ _

/-- Other candidates lose a protected claim. This excludes them for any gains. -/
theorem fixed_dominates_failures {G : Type} (gain : Plan → G → Prop)
    (p : Plan) (hp : p ≠ .fixed) : Better (protects both) gain .fixed p := by
  exact protection_anchor (p := protects both) (g := gain) (a := .fixed) (b := p)
    (fun c _ => fixed_protects both c) .continuation
    (fixed_protects both .continuation)
    (fun h => hp ((robust_continuation_iff p).mp h))

theorem fixed_is_chosen {G : Type} (gain : Plan → G → Prop) : chosen both gain .fixed := by
  refine ⟨trivial, ?_⟩
  intro p _ better
  by_cases hp : p = .fixed
  · subst p
    exact better_irrefl _ _ _ better
  · exact no_protection_trade_by_count .continuation (fixed_protects both .continuation)
      (fun h => hp ((robust_continuation_iff p).mp h)) better

theorem chosen_iff_fixed {G : Type} (gain : Plan → G → Prop) (p : Plan) :
    chosen both gain p ↔ p = .fixed := by
  constructor
  · intro h
    by_contra hp
    exact h.2 .fixed trivial (fixed_dominates_failures gain p hp)
  · rintro rfl
    exact fixed_is_chosen gain

/-- The reason requires a real, affordable event history in every admitted case. -/
theorem chosen_has_protecting_trace {G : Type} (gain : Plan → G → Prop)
    (p : Plan) (h : chosen both gain p) (w : Case) :
    Generative.Trace (SystemsOrganization.deterministic (advance (config w p) 1))
      (entrance 4176 1) (events p) (outcome 4176 1 w p) ∧
    holds (outcome 4176 1 w p) .continuation ∧
    holds (outcome 4176 1 w p) .companion := by
  have hp := (chosen_iff_fixed gain p).mp h
  subst p
  exact ⟨outcome_is_trace _ _ _ _, fixed_protects both .continuation w trivial,
    companion_retained _ _⟩

theorem collective_response_required {G : Type} (gain : Plan → G → Prop) :
    Required (chosen both gain) (fun p => protects both p .continuation) := by
  refine ⟨⟨.fixed, fixed_is_chosen gain⟩, ?_⟩
  intro p hp
  exact (robust_continuation_iff p).mpr ((chosen_iff_fixed gain p).mp hp)

/-- Each sensor case has a successful measured variant, but those two variants
alone have no common successful choice before the case has been resolved. -/
theorem pointwise_success_not_common_choice :
    (∀ w, ∃ p, p ≠ .fixed ∧ holds (outcome 4176 1 w p) .continuation) ∧
    ¬ ∃ p, p ≠ .fixed ∧ protects both p .continuation := by
  constructor
  · intro w
    cases w with
    | accurate => exact ⟨.measured, by decide, (continuation_table _ _).mpr (by simp)⟩
    | biased => exact ⟨.margin, by decide, (continuation_table _ _).mpr (by simp)⟩
  · rintro ⟨p,hp,h⟩
    exact hp ((robust_continuation_iff p).mp h)

/-- Valid narrowing preserves protection; actual-case inclusion remains necessary. -/
theorem protection_under_narrowing (old new : Case → Prop)
    (subset : Included new old) (p : Plan) (c : Claim) :
    protects old p c → protects new p c := robust_under_refinement subset

theorem accurate_measurement_protects (c : Claim) : protects accurateOnly .measured c := by
  intro w hw
  have hw' : w = .accurate := hw
  subst w
  cases c with
  | continuation => exact (continuation_table _ _).mpr (by simp)
  | companion => exact companion_retained _ _

theorem false_narrowing_loses_actual_claim :
    protects accurateOnly .measured .continuation ∧
    ¬ holds (outcome 4176 1 .biased .measured) .continuation := by
  exact ⟨accurate_measurement_protects _, by rw [continuation_table]; simp⟩

theorem accurate_measured_is_chosen :
    chosen accurateOnly (fun (_ : Plan) (_ : Unit) => False) .measured := by
  refine ⟨trivial, ?_⟩
  intro p _ h
  rcases h with h | h
  · exact h.2 (fun c _ => accurate_measurement_protects c)
  · exact h.2.2.2 (fun _ hfalse => hfalse)

/-- Increasing uncertainty can defeat a previously undominated choice. -/
theorem broader_cases_change_judgment :
    chosen accurateOnly (fun (_ : Plan) (_ : Unit) => False) .measured ∧
    ¬ chosen both (fun (_ : Plan) (_ : Unit) => False) .measured := by
  exact ⟨accurate_measured_is_chosen, by rw [chosen_iff_fixed]; decide⟩

theorem optional_supply_loss_is_real :
    (outcome 4176 1 .biased .measured).source = 1 ∧
    (outcome 4176 1 .biased .fixed).source = 0 := by
  simp [outcome, config, events]
  norm_num [run, inquiry, SystemsOrganization.evolve,
    advance, entrance, paid, charge, tariff, probeBody, inspectBody, reviseBody,
    respondBody, fixedBody, total, drift, loss, decode, forecast, dose]
  simp

/-- Every admitted plan includes the same inquiry prefix. With too little work,
none enacts the due response. This does not exclude an unmodeled earlier action. -/
theorem underfunded_menu_has_no_success (w : Case) (p : Plan) :
    ¬ holds (outcome 3132 1 w p) .continuation := by
  cases w <;> cases p <;>
    simp [holds, outcome, config, events] <;>
    norm_num [run, inquiry, SystemsOrganization.evolve,
      advance, entrance, paid, charge, tariff, probeBody, inspectBody, reviseBody,
      respondBody, fixedBody, total, drift, loss, decode, forecast, dose] <;> simp

/-- A supplied rule using the actually acquired coordinate. Its efficacy depends
on this specific two-case channel and retained b=3. The final operation's tariff
is stipulated to include this branch; a measured implementation is not proved. -/
def selectedAllowance (v : View) : ℝ := if v.second = 0 then 3 else 0

def adaptiveAdvance (w : Case) (s : State) (e : Event) : State :=
  if e = .respond then
    advance {allowance := selectedAllowance s.view} 1 s e
  else advance (config w .measured) 1 s e

def adaptiveOutcome (w : Case) : State :=
  SystemsOrganization.evolve (adaptiveAdvance w) (entrance 4176 1) complete

theorem selection_uses_acquired_coordinate (v v' : View) (h : v.second = v'.second) :
    selectedAllowance v = selectedAllowance v' := by simp [selectedAllowance, h]

theorem adaptive_is_trace (w : Case) :
    Generative.Trace (SystemsOrganization.deterministic (adaptiveAdvance w))
      (entrance 4176 1) complete (adaptiveOutcome w) :=
  (SystemsOrganization.deterministic_trace_iff _ _ _ _).mpr rfl

/-- The state selected by the acquired record matches the previously checked
successful history, not a free choice from the unobserved case label. -/
theorem adaptive_matches_successful_history (w : Case) :
    adaptiveOutcome w = outcome 4176 1 w (if w = .accurate then .measured else .margin) := by
  cases w <;>
    simp [adaptiveOutcome, outcome, config, events, complete, inquiry, run,
      SystemsOrganization.evolve, adaptiveAdvance, advance, selectedAllowance,
      entrance, paid, charge, tariff, probeBody, inspectBody, reviseBody,
      respondBody, total, drift, loss, decode, forecast, dose]

theorem adaptive_protects (w : Case) (c : Claim) : holds (adaptiveOutcome w) c := by
  rw [adaptive_matches_successful_history]
  cases c with
  | companion => exact companion_retained _ _
  | continuation => cases w <;> rw [continuation_table] <;> simp

theorem adaptive_work_accounted (w : Case) : workTotal (adaptiveOutcome w) = 4176 := by
  rw [adaptive_matches_successful_history]
  exact all_work_accounted _ _ _ _

/-- `none` adds the acquired-record policy to the original three-plan menu. -/
def extendedOutcome (w : Case) : Option Plan → State
  | none => adaptiveOutcome w
  | some p => outcome 4176 1 w p

def extendedProtect (p : Option Plan) (c : Claim) : Prop :=
  ∀ w, holds (extendedOutcome w p) c

def extendedChosen (p : Option Plan) : Prop :=
  Frontier (fun _ => True) (Better extendedProtect (fun _ (_ : Unit) => False)) p

theorem complete_protection_is_undominated (p : Option Plan)
    (h : ∀ c, extendedProtect p c) : extendedChosen p := by
  refine ⟨trivial, ?_⟩
  intro q _ better
  rcases better with better | better
  · exact better.2 (fun c _ => h c)
  · exact better.2.2.2 (fun _ impossible => impossible)

theorem extended_fixed_is_chosen : extendedChosen (some .fixed) := by
  apply complete_protection_is_undominated
  intro c w
  exact fixed_protects both c w trivial

theorem extended_adaptive_is_chosen : extendedChosen none := by
  apply complete_protection_is_undominated
  intro c w
  exact adaptive_protects w c

/-- Menu formation matters: a newly admitted successful policy removes the old
fixed plan's indispensability while retaining a collective protection reason. -/
theorem extended_protection_required_without_fixed_requirement :
    Required extendedChosen (fun p => extendedProtect p .continuation) ∧
    ¬ Required extendedChosen (fun p => p = some .fixed) := by
  constructor
  · refine ⟨⟨none, extended_adaptive_is_chosen⟩, ?_⟩
    intro p hp
    by_contra failed
    have improvement : Better extendedProtect (fun _ (_ : Unit) => False) none p :=
      protection_anchor (fun c _ w => adaptive_protects w c) .continuation
        (fun w => adaptive_protects w .continuation) failed
    exact hp.2 none trivial improvement
  · exact alternative_defeats_specific_duty extended_adaptive_is_chosen (by simp)

end
end InquiryJudgment
