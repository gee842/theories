import RelationsAcrossScales
import RemainingDependency

/-! A new quantitative realization using the existing resource charger and
context-bound evidence decoder. This is not a replay of the ancestral learner.
All positions, records, support and stage changes belong to one joint process.
Successful inquiry steps take time in the declared law; denied attempts do not
advance that stage. Explicit waits model additional elapsed stages. -/
namespace ScaleRevision
noncomputable section
open RemainingDependency
set_option maxRecDepth 32768
set_option maxHeartbeats 4000000

structure View where
  total : ℝ := 0
  second : ℝ := 0
  loss : ℝ := 0
  atStage : Nat := 0
  tag : Option Datum := none
  fine : Bool := false

structure Config where
  bias : ℝ := 0
  clamp : Bool := false
  wrongContext : Bool := false
  ignoreDelay : Bool := false
  allowance : ℝ := 0

structure State where
  a : ℝ
  b : ℝ
  coupled : Bool := false
  source : ℝ := 1
  stage : Nat := 0
  phase : Nat := 0
  view : View := {}
  account : Account
  stopped : Bool := false
  delivered : ℝ := 0

def total (s : State) : ℝ := s.a + s.b
def loss (s : State) : ℝ := if s.coupled then s.b else 0

def drift (s : State) : State :=
  {s with a := s.a - loss s, stage := s.stage + 1}

def forecast (v : View) : ℝ :=
  if v.fine then v.total - v.second - v.loss else (v.total - v.loss) / 2

def dose (v : View) (θ error : ℝ) : ℝ := max 0 (θ + error - forecast v)

/-- Uses the inherited tariff, account and denial behavior. Logical real-valued
registers here are idealized; no finite-bit or measured energy claim is made. -/
def paid (s : State) (f : State → State) : State :=
  let r := charge s.account 1 8 2 0 0
  if r.2 = .none then f {s with account := r.1}
  else {s with stopped := true}

def probeBody (cfg : Config) (s : State) : State :=
  let t := drift s
  {t with phase := 1, view := {
    total := total t, loss := total s - total t, atStage := t.stage,
    tag := some ⟨if cfg.wrongContext then 1 else 0, false,
      decide (total s ≠ total t)⟩ }}

def inspectBody (cfg : Config) (s : State) : State :=
  let t := drift s
  {t with phase := 2, view := {s.view with total := total t, second := t.b + cfg.bias, atStage := t.stage}}

def reviseBody (cfg : Config) (s : State) : State :=
  let t := drift s
  {t with phase := 3, view := {s.view with
    total := if cfg.ignoreDelay then s.view.total else s.view.total - s.view.loss,
    atStage := t.stage,
    fine := !cfg.clamp && (decode 0 false s.view.tag == some true)}}

def respondBody (cfg : Config) (θ : ℝ) (s : State) : State :=
  let u := dose s.view θ cfg.allowance
  if s.view.atStage = s.stage ∧ decode 0 false s.view.tag ≠ none ∧ u ≤ s.source then
    {s with a := s.a - loss s + u, source := s.source - u, stage := s.stage + 1, phase := 4, delivered := s.delivered + u}
  else {drift s with stopped := true}

/-- An equally funded fixed intervention, supplied as a rival action. -/
def fixedBody (s : State) : State :=
  if 1 ≤ s.source then
    {s with a := s.a - loss s + 1, source := s.source - 1, stage := s.stage + 1, phase := 4, delivered := s.delivered + 1}
  else {drift s with stopped := true}

inductive Event where
  | activate | probe | inspect | revise | respond | fixedRespond | wait
  deriving DecidableEq, Repr

def advance (cfg : Config) (θ : ℝ) (s : State) (e : Event) : State :=
  if s.stopped then s else
  match e with
  | .activate => if s.phase = 0 then {s with coupled := true} else {s with stopped := true}
  | .probe => if s.phase = 0 then paid s (probeBody cfg) else {s with stopped := true}
  | .inspect => if s.phase = 1 then paid s (inspectBody cfg) else {s with stopped := true}
  | .revise => if s.phase = 2 then paid s (reviseBody cfg) else {s with stopped := true}
  | .respond => if s.phase = 3 then paid s (respondBody cfg θ) else {s with stopped := true}
  | .fixedRespond => if s.phase = 3 then paid s fixedBody else {s with stopped := true}
  | .wait => paid s drift

def run (cfg : Config) (θ : ℝ) (s : State) (es : List Event) : State :=
  SystemsOrganization.evolve (advance cfg θ) s es

def entrance (fuel : Nat := 4176) (supply : ℝ := 1) : State :=
  {a := 12, b := 3, source := supply,
    account := {fuel := fuel, live := 8, peak := 10, capacity := 32}}

def inquiry : List Event := [.activate, .probe, .inspect, .revise]
def complete : List Event := inquiry ++ [.respond]

/-- A declared actual history, not a post-hoc relabeling of outputs. -/
theorem run_is_core_trace (cfg : Config) (θ : ℝ) (s : State) (es : List Event) :
    Generative.Trace (SystemsOrganization.deterministic (advance cfg θ)) s es
      (run cfg θ s es) := by
  exact (SystemsOrganization.deterministic_trace_iff (advance cfg θ) s _ es).mpr rfl

theorem probe_obtains_actual_loss (cfg : Config) (s : State) :
    (probeBody cfg s).view.loss = loss s := by
  simp only [probeBody, total, drift]
  ring

/-- A binding is evidence provenance, not evidence truth. -/
theorem truthful_changed_probe_requests_refinement (s : State)
    (h : total s ≠ total (drift s)) :
    decode 0 false (probeBody {} s).view.tag = some true := by
  simp [probeBody, decode, h]

theorem revised_exact_forecast (v : View) (a b l : ℝ)
    (hf : v.fine = true) (ht : v.total = a+b)
    (hb : v.second = b) (hl : v.loss = l) :
    forecast v = a-l := by
  simp only [forecast, hf, ↓reduceIte, ht, hb, hl]
  ring

/-- The earlier observable error certificate gives the actual post-response
condition after a supplied additive response. No normative threshold is proved. -/
theorem calibrated_response_margin (v : View) (actual θ E : ℝ)
    (h : |actual - forecast v| ≤ E) : θ ≤ actual + dose v θ E := by
  have lower := (abs_le.mp h).1
  have hd : θ + E - forecast v ≤ dose v θ E := le_max_right _ _
  linarith

theorem readout_error_enters_response {X Y : Type} [PseudoMetricSpace Y]
    (p : X → Y) (f : X → ℝ) (g : Y → ℝ) (x : X) (y : Y)
    (v : View) (a K E θ : ℝ) (hK : 0 ≤ K)
    (hc : |f x - g (p x)| ≤ a)
    (hs : |g (p x) - g y| ≤ K * dist (p x) y)
    (hr : dist (p x) y ≤ E) (hv : forecast v = g y) :
    θ ≤ f x + dose v θ (a + K * E) := by
  apply calibrated_response_margin
  rw [hv]
  exact RelationsAcrossScales.observable_error p f g x y a K E hK hc hs hr

theorem dose_nonnegative (v : View) (θ E : ℝ) : 0 ≤ dose v θ E := le_max_left _ _

theorem bounded_source_after_response (cfg : Config) (θ : ℝ) (s : State)
    (hs : 0 ≤ s.source) : 0 ≤ (respondBody cfg θ s).source := by
  unfold respondBody
  dsimp only
  split
  · rename_i h
    dsimp only
    linarith [h.2.2]
  · exact hs

theorem response_keeps_second (cfg : Config) (θ : ℝ) (s : State) :
    (respondBody cfg θ s).b = s.b := by
  unfold respondBody
  dsimp only
  split <;> rfl

theorem response_support_balance (cfg : Config) (θ : ℝ) (s : State)
    (ok : s.view.atStage = s.stage ∧ decode 0 false s.view.tag ≠ none ∧
      dose s.view θ cfg.allowance ≤ s.source) :
    (respondBody cfg θ s).a + (respondBody cfg θ s).source + loss s =
      s.a + s.source := by
  simp only [respondBody]
  rw [if_pos ok]
  dsimp only
  ring

theorem actual_response_condition (cfg : Config) (θ : ℝ) (s : State)
    (ok : s.view.atStage = s.stage ∧ decode 0 false s.view.tag ≠ none ∧
      dose s.view θ cfg.allowance ≤ s.source)
    (calibrated : |(s.a - loss s) - forecast s.view| ≤ cfg.allowance) :
    θ ≤ (respondBody cfg θ s).a := by
  have h := calibrated_response_margin s.view (s.a - loss s) θ cfg.allowance calibrated
  simpa only [respondBody, if_pos ok] using h

def workTotal (s : State) : Nat := s.account.fuel + s.account.spent

theorem paid_work_conserved (s : State) (f : State → State)
    (hf : ∀ t, workTotal (f t) = workTotal t) :
    workTotal (paid s f) = workTotal s := by
  unfold paid
  dsimp only
  split
  · rw [hf]
    exact charge_conserves s.account 1 8 2 0 0
  · rfl

theorem advance_work_conserved (cfg : Config) (θ : ℝ) (s : State) (e : Event) :
    workTotal (advance cfg θ s e) = workTotal s := by
  have hp : workTotal (paid s (probeBody cfg)) = workTotal s :=
    paid_work_conserved s _ (fun _ => rfl)
  have hi : workTotal (paid s (inspectBody cfg)) = workTotal s :=
    paid_work_conserved s _ (fun _ => rfl)
  have hv : workTotal (paid s (reviseBody cfg)) = workTotal s :=
    paid_work_conserved s _ (fun _ => rfl)
  have hr : workTotal (paid s (respondBody cfg θ)) = workTotal s := by
    apply paid_work_conserved
    intro t
    unfold respondBody
    dsimp only
    split <;> rfl
  have hfixed : workTotal (paid s fixedBody) = workTotal s := by
    apply paid_work_conserved
    intro t
    unfold fixedBody
    split <;> rfl
  have hw : workTotal (paid s drift) = workTotal s :=
    paid_work_conserved s _ (fun _ => rfl)
  cases e <;> simp only [advance]
  all_goals split
  all_goals first | rfl | assumption | (split <;> first | rfl | assumption)

theorem run_work_conserved (cfg : Config) (θ : ℝ) (s : State) (es : List Event) :
    workTotal (run cfg θ s es) = workTotal s := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih =>
    exact (ih (advance cfg θ s e)).trans (advance_work_conserved cfg θ s e)

/-- Extra waiting is not silently treated as a fresh measurement. -/
theorem waited_evidence_rejected (cfg : Config) (θ : ℝ) (s : State)
    (hfresh : s.view.atStage = s.stage) :
    (respondBody cfg θ (drift s)).stopped = true := by
  have hbad : ¬ s.view.atStage = s.stage + 1 := by omega
  simp [respondBody, drift, hbad]

/-! Concrete rational-valued histories within the real-valued model. These
are checks of exact definitions, not numerical approximations or biology. -/
theorem acquired_revision_endpoint :
    let s := run {} 1 (entrance) inquiry
    s.a = 3 ∧ s.b = 3 ∧ s.stage = 3 ∧ s.view.total = 6 ∧
      s.view.second = 3 ∧ s.view.loss = 3 ∧ s.view.fine = true ∧
      forecast s.view = 0 ∧ s.account.fuel = 1044 := by
  norm_num [run, inquiry, SystemsOrganization.evolve, advance, entrance,
    paid, charge, tariff, probeBody, inspectBody, reviseBody, total, drift, loss,
    decode, forecast]

theorem enacted_refinement_protects :
    let s := run {} 1 (entrance) complete
    s.a = 1 ∧ s.b = 3 ∧ s.source = 0 ∧ s.delivered = 1 ∧
      s.stage = 4 ∧ s.phase = 4 ∧ s.stopped = false ∧
      s.account.fuel = 0 ∧ s.account.spent = 4176 := by
  norm_num [run, complete, inquiry, SystemsOrganization.evolve, advance, entrance,
    paid, charge, tariff, probeBody, inspectBody, reviseBody, respondBody,
    total, drift, loss, decode, forecast, dose]
  simp

theorem clamped_description_loses_condition :
    let s := run {clamp := true} 1 (entrance) complete
    s.a = 0 ∧ s.b = 3 ∧ s.source = 1 ∧ s.delivered = 0 ∧
      s.account.spent = 4176 ∧ s.phase = 4 ∧ s.stopped = false := by
  norm_num [run, complete, inquiry, SystemsOrganization.evolve, advance, entrance,
    paid, charge, tariff, probeBody, inspectBody, reviseBody, respondBody,
    total, drift, loss, decode, forecast, dose]
  simp

theorem ignored_revision_delay_loses_condition :
    let s := run {ignoreDelay := true} 1 (entrance) complete
    s.a = 0 ∧ s.view.fine = true ∧ s.source = 1 ∧ s.phase = 4 := by
  norm_num [run, complete, inquiry, SystemsOrganization.evolve, advance, entrance,
    paid, charge, tariff, probeBody, inspectBody, reviseBody, respondBody,
    total, drift, loss, decode, forecast, dose]
  simp

theorem biased_new_coordinate_loses_condition :
    let s := run {bias := -3} 1 (entrance) complete
    s.a = 0 ∧ s.view.fine = true ∧ s.view.second = 0 ∧ s.source = 1 ∧ s.phase = 4 := by
  norm_num [run, complete, inquiry, SystemsOrganization.evolve, advance, entrance,
    paid, charge, tariff, probeBody, inspectBody, reviseBody, respondBody,
    total, drift, loss, decode, forecast, dose]
  simp

theorem inquiry_can_exhaust_response_funding :
    let s := run {} 1 (entrance 3132) complete
    s.view.fine = true ∧ s.account.fuel = 0 ∧ s.account.spent = 3132 ∧
      s.stopped = true ∧ s.phase = 3 ∧ s.delivered = 0 := by
  norm_num [run, complete, inquiry, SystemsOrganization.evolve, advance, entrance,
    paid, charge, tariff, probeBody, inspectBody, reviseBody, respondBody,
    total, drift, loss, decode, forecast, dose]
  simp

theorem insufficient_response_source :
    let s := run {} 1 (entrance 4176 0) complete
    s.view.fine = true ∧ s.stopped = true ∧ s.phase = 3 ∧
      s.delivered = 0 ∧ s.source = 0 ∧ s.account.spent = 4176 := by
  norm_num [run, complete, inquiry, SystemsOrganization.evolve, advance, entrance,
    paid, charge, tariff, probeBody, inspectBody, reviseBody, respondBody,
    total, drift, loss, decode, forecast, dose]

theorem mismatched_context_withholds_response :
    let s := run {wrongContext := true} 1 (entrance) complete
    s.stopped = true ∧ s.phase = 3 ∧ s.delivered = 0 ∧ s.view.fine = false := by
  norm_num [run, complete, inquiry, SystemsOrganization.evolve, advance, entrance,
    paid, charge, tariff, probeBody, inspectBody, reviseBody, respondBody,
    total, drift, loss, decode, forecast, dose]

theorem matched_revision_preserves_other_inputs (cfg : Config) (s : State) :
    let a := reviseBody cfg s
    let b := reviseBody {cfg with clamp := true} s
    a.a = b.a ∧ a.b = b.b ∧ a.view.total = b.view.total ∧
      a.view.second = b.view.second ∧ a.view.loss = b.view.loss ∧
      a.view.atStage = b.view.atStage ∧ a.account = b.account := by
  exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩

theorem bounded_bias_margin_recovers :
    let s := run {bias := -3, allowance := 3} 1 (entrance) complete
    s.a = 1 ∧ s.b = 3 ∧ s.source = 0 ∧ s.delivered = 1 ∧ s.phase = 4 := by
  norm_num [run, complete, inquiry, SystemsOrganization.evolve, advance, entrance,
    paid, charge, tariff, probeBody, inspectBody, reviseBody, respondBody,
    total, drift, loss, decode, forecast, dose]
  simp

theorem conservative_margin_can_exceed_source :
    let s := run {allowance := 3} 1 (entrance) complete
    s.a = 0 ∧ s.view.fine = true ∧ s.stopped = true ∧ s.phase = 3 ∧
      s.delivered = 0 ∧ s.source = 1 ∧ s.stage = 4 := by
  norm_num [run, complete, inquiry, SystemsOrganization.evolve, advance, entrance,
    paid, charge, tariff, probeBody, inspectBody, reviseBody, respondBody,
    total, drift, loss, decode, forecast, dose]

theorem fixed_response_also_protects :
    let s := run {clamp := true} 1 (entrance) (inquiry ++ [.fixedRespond])
    s.a = 1 ∧ s.b = 3 ∧ s.source = 0 ∧ s.view.fine = false ∧
      s.delivered = 1 ∧ s.account.spent = 4176 ∧ s.phase = 4 := by
  norm_num [run, inquiry, SystemsOrganization.evolve, advance, entrance,
    paid, charge, tariff, probeBody, inspectBody, reviseBody, fixedBody,
    total, drift, loss, decode]

end
end ScaleRevision

#print axioms ScaleRevision.run_is_core_trace
#print axioms ScaleRevision.probe_obtains_actual_loss
#print axioms ScaleRevision.truthful_changed_probe_requests_refinement
#print axioms ScaleRevision.revised_exact_forecast
#print axioms ScaleRevision.calibrated_response_margin
#print axioms ScaleRevision.readout_error_enters_response
#print axioms ScaleRevision.dose_nonnegative
#print axioms ScaleRevision.bounded_source_after_response
#print axioms ScaleRevision.response_keeps_second
#print axioms ScaleRevision.response_support_balance
#print axioms ScaleRevision.actual_response_condition
#print axioms ScaleRevision.paid_work_conserved
#print axioms ScaleRevision.advance_work_conserved
#print axioms ScaleRevision.run_work_conserved
#print axioms ScaleRevision.waited_evidence_rejected
#print axioms ScaleRevision.acquired_revision_endpoint
#print axioms ScaleRevision.enacted_refinement_protects
#print axioms ScaleRevision.clamped_description_loses_condition
#print axioms ScaleRevision.ignored_revision_delay_loses_condition
#print axioms ScaleRevision.biased_new_coordinate_loses_condition
#print axioms ScaleRevision.inquiry_can_exhaust_response_funding
#print axioms ScaleRevision.insufficient_response_source
#print axioms ScaleRevision.mismatched_context_withholds_response
#print axioms ScaleRevision.matched_revision_preserves_other_inputs
#print axioms ScaleRevision.bounded_bias_margin_recovers
#print axioms ScaleRevision.conservative_margin_can_exceed_source
#print axioms ScaleRevision.fixed_response_also_protects
