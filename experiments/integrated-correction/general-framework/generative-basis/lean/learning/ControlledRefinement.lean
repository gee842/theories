import ControllerRevision

/-!
# Exact world refinement compatible with an installed controller

World possibility alone does not preserve controlled behavior. A sufficient
additional condition is agreement of the complete accessible observation on
every actual concrete edge. The same deterministic controller and inherited
memory then give exact finite (action, observation)-labelled histories.

These conditions are sufficient, not necessary for one fixed controller: it
may ignore distinctions or never select some events. No probability, physical
implementation, adversarial guarantee, timing, or infinite-path claim follows.
The controller and its sensing/update architecture remain supplied. Costs
require their own compatible state/edge valuations; existing account pullback
theorems apply only to those declared valuations.
-/

namespace Generative.Learning.Refinement

universe u v w x y z

variable {State : Type u} {Other : Type v} {Third : Type w}
variable {Action : Type x} {Observation : Type y} {Memory : Type z}

/-- Exactness from each concrete state, not a union of edges over its fibre. -/
def LocalExact (P : Process State Action) (Q : Process Other Action)
    (q : State → Other) : Prop :=
  ∀ s a r, Q.step (q s) a r ↔ ∃ t, P.step s a t ∧ q t = r

/-- Agreement is required on admitted concrete edges only. -/
def ObservationCompatible (P : Process State Action) (q : State → Other)
    (senseP : State → Action → State → Observation)
    (senseQ : Other → Action → Other → Observation) : Prop :=
  ∀ s a t, P.step s a t → senseP s a t = senseQ (q s) a (q t)

def retainMemory (q : State → Other) (p : State × Memory) : Other × Memory :=
  (q p.1, p.2)

/-- A compatible deterministic summary channel cannot separate edges whose
projected predecessor, action and projected successor are identical. -/
theorem compatible_observations_agree_on_fibres
    {P : Process State Action} {q : State → Other}
    {senseP : State → Action → State → Observation}
    {senseQ : Other → Action → Other → Observation}
    (ho : ObservationCompatible P q senseP senseQ)
    {s t s' t' : State} {a : Action}
    (h : P.step s a t) (h' : P.step s' a t')
    (hstart : q s = q s') (hend : q t = q t') :
    senseP s a t = senseP s' a t' := by
  rw [ho s a t h, ho s' a t' h', hstart, hend]

/-- Two valid interfaces compose through the same actual intermediate map. -/
theorem local_exact_comp {P : Process State Action} {Q : Process Other Action}
    {R : Process Third Action} {q : State → Other} {r : Other → Third}
    (hp : LocalExact P Q q) (hq : LocalExact Q R r) :
    LocalExact P R (fun s => r (q s)) := by
  intro s a u
  constructor
  · intro h
    obtain ⟨v, hv, hrv⟩ := (hq (q s) a u).mp h
    obtain ⟨t, ht, hqt⟩ := (hp s a v).mp hv
    exact ⟨t, ht, (congrArg r hqt).trans hrv⟩
  · rintro ⟨t, ht, hrt⟩
    exact (hq (q s) a u).mpr ⟨q t, (hp s a (q t)).mpr ⟨t, ht, rfl⟩, hrt⟩

theorem observation_compatible_comp {P : Process State Action}
    {Q : Process Other Action} {q : State → Other} {r : Other → Third}
    {senseP : State → Action → State → Observation}
    {senseQ : Other → Action → Other → Observation}
    {senseR : Third → Action → Third → Observation}
    (hp : LocalExact P Q q)
    (op : ObservationCompatible P q senseP senseQ)
    (oq : ObservationCompatible Q r senseQ senseR) :
    ObservationCompatible P (fun s => r (q s)) senseP senseR := by
  intro s a t hs
  exact (op s a t hs).trans
    (oq (q s) a (q t) ((hp s a (q t)).mpr ⟨t, hs, rfl⟩))

/-- Retaining identical memory and an edge-compatible channel makes exact
world refinement an exact closed-loop refinement. -/
theorem closed_loop_local_exact
    (C : Controller Memory Action Observation)
    {P : Process State Action} {Q : Process Other Action} {q : State → Other}
    {senseP : State → Action → State → Observation}
    {senseQ : Other → Action → Other → Observation}
    (hw : LocalExact P Q q) (ho : ObservationCompatible P q senseP senseQ) :
    LocalExact (closedLoop C P senseP) (closedLoop C Q senseQ) (retainMemory q) := by
  rintro ⟨s, m⟩ ⟨a, o⟩ ⟨r, n⟩
  constructor
  · rintro ⟨hq, ha, hsense, hmemory⟩
    obtain ⟨t, ht, hqt⟩ := (hw s a r).mp hq
    refine ⟨(t, n), ⟨ht, ha, ?_, hmemory⟩, ?_⟩
    · exact hsense.trans ((ho s a t ht).trans (congrArg (senseQ (q s) a) hqt)).symm
    · exact Prod.ext hqt rfl
  · rintro ⟨⟨t, k⟩, ⟨ht, ha, hsense, hmemory⟩, heq⟩
    have hqt : q t = r := congrArg Prod.fst heq
    have hkn : k = n := congrArg Prod.snd heq
    exact ⟨(hw s a r).mpr ⟨t, ht, hqt⟩, ha,
      hsense.trans ((ho s a t ht).trans (congrArg (senseQ (q s) a) hqt)),
      hkn.symm.trans hmemory⟩

/-- Exact finite histories retain observations, commands and projected endpoints.
The existential endpoint is an actual concrete successor with the same memory. -/
theorem controlled_trace_exact
    (C : Controller Memory Action Observation)
    {P : Process State Action} {Q : Process Other Action} {q : State → Other}
    {senseP : State → Action → State → Observation}
    {senseQ : Other → Action → Other → Observation}
    (hw : LocalExact P Q q) (ho : ObservationCompatible P q senseP senseQ)
    (p : State × Memory) (events : List (Action × Observation)) (r : Other × Memory) :
    Trace (closedLoop C Q senseQ) (retainMemory q p) events r ↔
      ∃ t, Trace (closedLoop C P senseP) p events t ∧ retainMemory q t = r := by
  exact local_exact_iff_trace_exact.mp (closed_loop_local_exact C hw ho) p events r

/-- Possibility for the supplied controller; no robust or optimal-policy claim. -/
theorem controlled_feasible_exact
    (C : Controller Memory Action Observation)
    {P : Process State Action} {Q : Process Other Action} {q : State → Other}
    {senseP : State → Action → State → Observation}
    {senseQ : Other → Action → Other → Observation}
    (hw : LocalExact P Q q) (ho : ObservationCompatible P q senseP senseQ)
    (p : State × Memory) (events : List (Action × Observation)) :
    Feasible (closedLoop C P senseP) p events ↔
      Feasible (closedLoop C Q senseQ) (retainMemory q p) events := by
  constructor
  · rintro ⟨t, ht⟩
    exact ⟨retainMemory q t, (controlled_trace_exact C hw ho p events _).mpr ⟨t, ht, rfl⟩⟩
  · rintro ⟨r, hr⟩
    obtain ⟨t, ht, _⟩ := (controlled_trace_exact C hw ho p events r).mp hr
    exact ⟨t, ht⟩

namespace ObservationLoss

inductive Command where
  | probe | left | right
  deriving DecidableEq

inductive BitMemory where
  | unknown | remembered (bit : Bool)
  deriving DecidableEq

/-- Every command preserves the hidden bit and consumes one fuel unit. -/
def world : Process (Bool × Nat) Command where
  step s _ t := t.1 = s.1 ∧ s.2 = t.2 + 1

def summaryWorld : Process Nat Command where
  step s _ t := s = t + 1

def controller : Controller BitMemory Command Bool where
  choose m := match m with
    | .unknown => .probe
    | .remembered false => .left
    | .remembered true => .right
  revise m bit := match m with
    | .unknown => .remembered bit
    | .remembered old => .remembered old

def sense (_ : Bool × Nat) (_ : Command) (t : Bool × Nat) : Bool := t.1
def erasedSense (_ : Nat) (_ : Command) (_ : Nat) : Bool := false

/-- Forgetting the bit is exact for every uncontrolled event history. -/
theorem world_local_exact : LocalExact world summaryWorld Prod.snd := by
  intro s a r
  constructor
  · intro h
    exact ⟨(s.1, r), ⟨rfl, h⟩, rfl⟩
  · rintro ⟨t, ⟨_, h⟩, ht⟩
    exact h.trans (congrArg (fun n => n + 1) ht)

theorem world_trace_exact (s : Bool × Nat) (word : List Command) (r : Nat) :
    Trace summaryWorld s.2 word r ↔ ∃ t, Trace world s word t ∧ t.2 = r := by
  exact local_exact_iff_trace_exact.mp world_local_exact s word r

/-- Both worlds have the same declared unit expenditure and no supplied credit. -/
theorem summary_unit_account : Conditional.AccountLaw summaryWorld (fun n => n)
    (fun _ _ _ => 1) (fun _ _ _ => 0) := by
  intro s a t h
  change s = t + 1 at h
  change t + 1 ≤ s + 0
  omega

theorem concrete_unit_account : Conditional.AccountLaw world Prod.snd
    (fun _ _ _ => 1) (fun _ _ _ => 0) := by
  exact Conditional.account_law_pullback (P := world) summaryWorld Prod.snd
    (fun _ _ _ h => h.2) (fun n => n)
    (fun _ _ _ => 1) (fun _ _ _ => 0) summary_unit_account

/-- No deterministic channel on the erased state can reproduce this observation
on every edge, irrespective of how it is chosen. -/
theorem no_compatible_summary_channel
    (channel : Nat → Command → Nat → Bool) :
    ¬ ObservationCompatible world Prod.snd sense channel := by
  intro h
  have hfalse := h (false, 2) .probe (false, 1) ⟨rfl, rfl⟩
  have htrue := h (true, 2) .probe (true, 1) ⟨rfl, rfl⟩
  have impossible : false = true := hfalse.trans htrue.symm
  cases impossible

theorem concrete_probe_then_right :
    Trace (closedLoop controller world sense)
      ((true, 2), .unknown) [(.probe, true), (.right, true)]
      ((true, 0), .remembered true) := by
  refine .cons (m := ((true, 1), .remembered true)) ?_ (.cons ?_ (.nil _))
  all_goals simp [closedLoop, world, controller, sense]

theorem summary_probe_then_left :
    Trace (closedLoop controller summaryWorld erasedSense)
      (2, .unknown) [(.probe, false), (.left, false)]
      (0, .remembered false) := by
  refine .cons (m := (1, .remembered false)) ?_ (.cons ?_ (.nil _))
  all_goals simp [closedLoop, summaryWorld, controller, erasedSense]

/-- The failure is visible in the command word even if observation labels are
ignored: no observations/end state can make probe-then-right executable here. -/
theorem summary_cannot_issue_probe_then_right (o₁ o₂ : Bool) (r : Nat × BitMemory) :
    ¬ Trace (closedLoop controller summaryWorld erasedSense)
      (2, .unknown) [(.probe, o₁), (.right, o₂)] r := by
  intro h
  obtain ⟨mid, first, tail⟩ := trace_cons_iff.mp h
  obtain ⟨last, second, _⟩ := trace_cons_iff.mp tail
  have ho : o₁ = false := first.2.2.1
  have hm : mid.2 = .remembered false := by
    simpa only [controller, ho] using first.2.2.2
  have bad : Command.right = Command.left := by
    simpa only [hm, controller] using second.2.1
  cases bad

/-- Therefore the exact world quotient fails to be an exact closed-loop quotient. -/
theorem controlled_local_exact_fails :
    ¬ LocalExact (closedLoop controller world sense)
      (closedLoop controller summaryWorld erasedSense) (retainMemory Prod.snd) := by
  intro h
  have projected := (local_exact_iff_trace_exact.mp h
    ((true, 2), .unknown) [(.probe, true), (.right, true)] (0, .remembered true)).mpr
      ⟨((true, 0), .remembered true), concrete_probe_then_right, rfl⟩
  exact summary_cannot_issue_probe_then_right true true (0, .remembered true) projected

end ObservationLoss

end Generative.Learning.Refinement

#print axioms Generative.Learning.Refinement.local_exact_comp
#print axioms Generative.Learning.Refinement.compatible_observations_agree_on_fibres
#print axioms Generative.Learning.Refinement.observation_compatible_comp
#print axioms Generative.Learning.Refinement.closed_loop_local_exact
#print axioms Generative.Learning.Refinement.controlled_trace_exact
#print axioms Generative.Learning.Refinement.controlled_feasible_exact
#print axioms Generative.Learning.Refinement.ObservationLoss.world_local_exact
#print axioms Generative.Learning.Refinement.ObservationLoss.world_trace_exact
#print axioms Generative.Learning.Refinement.ObservationLoss.summary_unit_account
#print axioms Generative.Learning.Refinement.ObservationLoss.concrete_unit_account
#print axioms Generative.Learning.Refinement.ObservationLoss.no_compatible_summary_channel
#print axioms Generative.Learning.Refinement.ObservationLoss.concrete_probe_then_right
#print axioms Generative.Learning.Refinement.ObservationLoss.summary_probe_then_left
#print axioms Generative.Learning.Refinement.ObservationLoss.summary_cannot_issue_probe_then_right
#print axioms Generative.Learning.Refinement.ObservationLoss.controlled_local_exact_fails
