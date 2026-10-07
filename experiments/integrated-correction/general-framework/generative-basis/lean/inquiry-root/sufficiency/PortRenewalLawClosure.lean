import PortRenewalBoundary

set_option maxRecDepth 10000

/-!
# Exact native replenishment and the contact-renewal mapping obstruction

The existing native law has no aging of contact and has only a finite source.
We retain its actual transitions and derive completed encounter costs, source
consumption and bounded replenishment. Separate theorems refute the specific
contact-only correspondence to ChannelLaw: its births need a surviving earlier
token and its tokens age on every tick. These are not claims that no enriched
representation or physically replenishing process can exist.
-/

namespace Generative.InquirySufficiency.PortRenewalLawClosure

open Generative NativePacketProcess NativePortContinuation
open FormationClosure AcquiredContact RevisingPort WholePortContinuation
open Conditional.Renewal

universe u

/-- A channel cannot form a token when its preceding token list is empty. -/
theorem no_channel_birth_from_empty {Kind : Type u} (law : ChannelLaw Kind)
    {c d : Config Kind} {k : Kind} {ks : List Kind}
    (empty : c.tokens = []) (step : (channelProcess law).step c (k :: ks) d) : False := by
  obtain ⟨tok, member, _⟩ := step.2.2 k List.mem_cons_self
  rw [empty] at member
  cases member

/-- A live token list cannot equal its own aged list. This uses actual aging,
not an independently supplied declining potential for the native contact. -/
theorem live_tokens_do_not_stand_still {Kind : Type u} (tokens : List (Token Kind))
    (live : 1 ≤ opened (fun _ => 1) tokens) : tokens ≠ aged tokens := by
  intro fixed
  have balance := weighted_aged (fun _ => 1) tokens
  rw [← fixed] at balance
  have impossible : weighted (fun _ => 1) tokens + 1 ≤ weighted (fun _ => 1) tokens :=
    Nat.le_trans (Nat.add_le_add_left live _) (Nat.le_of_eq balance)
  exact Nat.lt_irrefl _ impossible

/-- A contact-only map which represents a blocked contact by no token cannot
represent the port's actual first formation as a channel birth. Additional
supporting organization must be represented and related to the recovery law. -/
theorem no_contact_only_formation_map {Kind : Type u} (law : ChannelLaw Kind)
    (view : Port → Config Kind) (kind : Kind)
    (blocked_empty : ∀ x, x.native.blocked = true → (view x).tokens = []) :
    ¬ (∀ x y, formPort x = .complete y →
      (channelProcess law).step (view x) [kind] (view y)) := by
  intro maps
  let x := PortRenewalBoundary.examplePort 100000 10 0
  let y := PortRenewalBoundary.formedExample 100000 10 0
  exact no_channel_birth_from_empty law (blocked_empty x rfl) (maps x y rfl)

/-- Read has an actual supported native step and preserves the contact. -/
theorem read_port_step {x : Port} (ready : Supportable x.native) :
    FormationClosure.process.step x (nativeE .read)
      ⟨enact x.native, x.spare, x.recovered⟩ :=
  ⟨⟨_, read_complete x.native ready⟩, rfl, rfl⟩

/-- If tokens depend only on the contact coordinate, even one ordinary read
contradicts ChannelLaw's aging with no births. This does not rule out a richer
map which tracks genuine age/maintenance state absent from this coordinate. -/
theorem no_contact_invariant_live_map {Kind : Type u} (law : ChannelLaw Kind)
    (view : Port → Config Kind)
    (same_contact : ∀ x y, contact x = contact y → (view x).tokens = (view y).tokens)
    {x : Port} (live : Live (view x)) :
    ¬ (channelProcess law).step (view x) []
      (view ⟨enact x.native, x.spare, x.recovered⟩) := by
  intro mapped
  have unchanged := same_contact x ⟨enact x.native, x.spare, x.recovered⟩ rfl
  have shape := mapped.1
  change (view ⟨enact x.native, x.spare, x.recovered⟩).tokens =
    aged (view x).tokens ++ [] at shape
  rw [append_nil_eq] at shape
  exact live_tokens_do_not_stand_still _ live (unchanged.trans shape)

/-- A native command consumes source only when a probe completes. -/
def sourceUsed : Command → Nat
  | .probe => 10
  | .a => 0
  | .reset => 0
  | .read => 0

/-- A probe has both an interface and a receipt stage. -/
def supportStages : Command → Nat
  | .probe => 2
  | .a => 1
  | .reset => 1
  | .read => 1

/-- Source consumption and enacted demand are exact, not upper estimates.
The native overhead is retained by each completed call. -/
theorem native_step_amounts {s t : State} {c : Command}
    (step : NativePacketProcess.process.step s c t) :
    t.source + sourceUsed c = s.source ∧
    t.enacted = s.enacted + supportStages c * draw s ∧ draw t = draw s := by
  obtain ⟨o, done⟩ := step
  cases c with
  | probe =>
    obtain ⟨ready, rfl, _⟩ := (probe_complete_iff s t o).mp done
    refine ⟨sub_add_restore _ _ ready.2.1, ?_, rfl⟩
    change (s.enacted + draw s) + draw s = s.enacted + 2 * draw s
    omega
  | reset =>
    obtain ⟨_, rfl, _⟩ := reset_shape done
    exact ⟨rfl, by change s.enacted + draw s = s.enacted + 1 * draw s; rw [Nat.one_mul], rfl⟩
  | a =>
    obtain ⟨_, rfl, _⟩ := a_shape done
    exact ⟨rfl, by change s.enacted + draw s = s.enacted + 1 * draw s; rw [Nat.one_mul], rfl⟩
  | read =>
    unfold execute at done
    generalize interface : support s = out at done
    cases out with
    | capacity => cases done
    | insufficient => cases done
    | sustained ready =>
      obtain ⟨_, rfl⟩ := (support_sustained_iff s ready).mp interface
      cases done
      exact ⟨rfl, by change s.enacted + draw s = s.enacted + 1 * draw s; rw [Nat.one_mul], rfl⟩

/-- A completed inquiry consumes exactly two source packets and seven draws.
No intact-reset or accurate-memory assumption is required for these quantities. -/
theorem inquiry_amounts {s : State} (q : Inquiry s) :
    q.s5.source + 20 = s.source ∧
    q.s5.enacted = s.enacted + 7 * draw s ∧ draw q.s5 = draw s := by
  have h1 := native_step_amounts ⟨_, q.step1⟩
  have h2 := native_step_amounts ⟨_, q.step2⟩
  have h3 := native_step_amounts ⟨_, q.step3⟩
  have h4 := native_step_amounts ⟨_, q.step4⟩
  have h5 := native_step_amounts ⟨_, q.step5⟩
  change q.s1.source + 0 = s.source ∧
    q.s1.enacted = s.enacted + 1 * draw s ∧ draw q.s1 = draw s at h1
  change q.s2.source + 10 = q.s1.source ∧
    q.s2.enacted = q.s1.enacted + 2 * draw q.s1 ∧ draw q.s2 = draw q.s1 at h2
  change q.s3.source + 0 = q.s2.source ∧
    q.s3.enacted = q.s2.enacted + 1 * draw q.s2 ∧ draw q.s3 = draw q.s2 at h3
  change q.s4.source + 0 = q.s3.source ∧
    q.s4.enacted = q.s3.enacted + 1 * draw q.s3 ∧ draw q.s4 = draw q.s3 at h4
  change q.s5.source + 10 = q.s4.source ∧
    q.s5.enacted = q.s4.enacted + 2 * draw q.s4 ∧ draw q.s5 = draw q.s4 at h5
  refine ⟨?_, ?_, h5.2.2.trans (h4.2.2.trans (h3.2.2.trans (h2.2.2.trans h1.2.2)))⟩
  · omega
  · omega

/-- The exact arrival in an intact inquiry follows the native gate. The sensor
and receipt inversions do not alter its accumulated arrival. -/
theorem inquiry_arrival {s : State} (q : Inquiry s) (intact : s.broken = false) :
    q.s5.arrived = s.arrived + (if s.blocked then 0 else 655360) := by
  obtain ⟨s1, s2, s3, s4, s5, r0, r1, o1, o3, o4, h1, h2, h3, h4, h5⟩ := q
  obtain ⟨_, rfl, rfl⟩ := reset_shape h1
  obtain ⟨_, rfl, _⟩ := (probe_complete_iff _ _ _).mp h2
  obtain ⟨_, rfl, rfl⟩ := a_shape h3
  obtain ⟨_, rfl, rfl⟩ := a_shape h4
  obtain ⟨_, rfl, _⟩ := (probe_complete_iff _ _ _).mp h5
  cases s with
  | mk phase tau sigma broken blocked flip source held live workspace capacity enacted
      arrived transferred dissipated =>
    subst intact
    cases tau <;> cases blocked
    · change arrived + 0 + 655360 = arrived + 655360
      exact congrArg (fun n => n + 655360) (Nat.add_zero arrived)
    · change arrived + 0 + 0 = arrived + 0
      exact Nat.add_zero (arrived + 0)
    · change arrived + 655360 + 0 = arrived + 655360
      exact Nat.add_zero (arrived + 655360)
    · change arrived + 0 + 0 = arrived + 0
      exact Nat.add_zero (arrived + 0)

/-- Exact endpoint equation for local held replenishment through an open
contact, including all seven actually completed support stages. -/
theorem inquiry_held_balance {s : State} (q : Inquiry s)
    (intact : s.broken = false) :
    q.s5.held + 7 * draw s = s.held + (if s.blocked then 0 else 655360) := by
  have balance := continues_exact (inquiry_continues q)
  rw [(inquiry_amounts q).2.1, inquiry_arrival q intact,
    add_sub_self_left, add_sub_self_left] at balance
  exact balance

/-- Whole-source opportunity does not grow through a completed native call. -/
theorem native_source_bound {s t : State} {c : Command}
    (step : NativePacketProcess.process.step s c t) :
    t.arrived + yieldPerUnit * t.source ≤ s.arrived + yieldPerUnit * s.source := by
  obtain ⟨_, shape⟩ := completed_shape step
  rcases shape with ⟨p, rfl⟩ | ⟨ready, rfl⟩
  · exact Nat.le_refl _
  · exact convert_keeps_potential_bound { enact s with held := s.arrived } ready.2.1

/-- This actual source bound composes through all intermediate native states. -/
theorem native_trace_source_bound {s t : State} {cs : List Command}
    (history : Trace NativePacketProcess.process s cs t) :
    t.arrived + yieldPerUnit * t.source ≤ s.arrived + yieldPerUnit * s.source := by
  induction history with
  | nil => exact Nat.le_refl _
  | cons step _ ih => exact Nat.le_trans ih (native_source_bound step)

/-- Formation changes the contact but neither source nor accumulated arrivals. -/
theorem acted_source_retained {b : Bool} {x z : Port} (act : acted b x z) :
    z.native.source = x.native.source ∧ z.native.arrived = x.native.arrived ∧
      draw z.native = draw x.native := by
  cases b with
  | false => rw [act]; exact ⟨rfl, rfl, rfl⟩
  | true =>
    obtain ⟨_, _, rfl⟩ := (formPort_complete_iff x z).mp act
    exact ⟨rfl, rfl, rfl⟩

/-- Every completed encounter consumes exactly twenty source units, even when
its acquired choice forms a contact. -/
theorem encounter_source_exact {a b : Revising} {found : Bool × Bool}
    (step : revising.step a (.inr found) b) :
    b.1.native.source + 20 = a.1.native.source := by
  obtain ⟨_, z, act, q, reached, _⟩ := step
  rw [reached]
  exact (inquiry_amounts q).1.trans (acted_source_retained act).1

/-- A formation adds exactly one draw to the inquiry's seven. -/
theorem encounter_enacted_exact {a b : Revising} {found : Bool × Bool}
    (step : revising.step a (.inr found) b) :
    b.1.native.enacted = a.1.native.enacted +
      (7 + if PortValuation.portOrg.select a.2 found then 1 else 0) * draw a.1.native := by
  obtain ⟨_, z, act, q, reached, _⟩ := step
  rw [reached]
  have amount := (inquiry_amounts q).2.1
  generalize chose : PortValuation.portOrg.select a.2 found = choice at act ⊢
  cases choice with
  | false => change z = a.1 at act; subst z; exact amount
  | true =>
    obtain ⟨_, _, rfl⟩ := (formPort_complete_iff a.1 z).mp act
    change q.s5.enacted = a.1.native.enacted + draw a.1.native + 7 * draw a.1.native at amount
    change q.s5.enacted = a.1.native.enacted + 8 * draw a.1.native
    omega

/-- Arrival is fixed by the actual contact after the act. Forming contributes
no arrival itself; the subsequent inquiry makes the packet transfer. -/
theorem encounter_arrival_exact {a b : Revising} {found : Bool × Bool}
    (step : revising.step a (.inr found) b) (intact : a.1.native.broken = false) :
    b.1.native.arrived = a.1.native.arrived +
      (if b.1.native.blocked then 0 else 655360) := by
  obtain ⟨_, z, act, q, reached, _⟩ := step
  have intactZ : z.native.broken = false := (acted_effects act).1.trans intact
  have amount := inquiry_arrival q intactZ
  have kept := acted_source_retained act
  have contactKept := (inquiry_reveals q intactZ).2.2.2.2.2.1
  rw [reached]
  change q.s5.arrived = a.1.native.arrived + (if q.s5.blocked then 0 else 655360)
  rw [contactKept, ← kept.2.1]
  exact amount

/-- Full encounter replenishment criterion, including optional formation and
both stages of each probe. All quantities have the same held-tick units. -/
theorem encounter_held_balance {a b : Revising} {found : Bool × Bool}
    (step : revising.step a (.inr found) b) (intact : a.1.native.broken = false) :
    b.1.native.held +
      (7 + if PortValuation.portOrg.select a.2 found then 1 else 0) * draw a.1.native =
      a.1.native.held + (if b.1.native.blocked then 0 else 655360) := by
  have balance := continues_exact (revising_continues step)
  rw [encounter_enacted_exact step, encounter_arrival_exact step intact,
    add_sub_self_left, add_sub_self_left] at balance
  exact balance

/-- Local held support is replenished exactly under this inequality. This is
an operational condition; it does not appraise the encounter ethically. -/
theorem encounter_replenishes_iff {a b : Revising} {found : Bool × Bool}
    (step : revising.step a (.inr found) b) (intact : a.1.native.broken = false)
    (opened : b.1.native.blocked = false) :
    a.1.native.held ≤ b.1.native.held ↔
      (7 + if PortValuation.portOrg.select a.2 found then 1 else 0) * draw a.1.native ≤ 655360 := by
  have balance := encounter_held_balance step intact
  rw [opened] at balance
  change b.1.native.held +
    (7 + if PortValuation.portOrg.select a.2 found then 1 else 0) * draw a.1.native =
    a.1.native.held + 655360 at balance
  constructor <;> intro h <;> omega

/-- The source bound also covers the extended port's native, recovery and
formation events, independently of any particular inquiry schedule. -/
theorem extended_source_bound {x y : Port} {e : FormationClosure.Event}
    (step : FormationClosure.process.step x e y) :
    y.native.arrived + yieldPerUnit * y.native.source ≤
      x.native.arrived + yieldPerUnit * x.native.source := by
  cases e with
  | inl event =>
    cases event with
    | inl command => exact native_source_bound step.1
    | inr _ =>
      obtain ⟨_, _, rfl⟩ := (recover_complete_iff x y).mp step
      exact Nat.le_refl _
  | inr _ =>
    obtain ⟨_, _, rfl⟩ := (formPort_complete_iff x y).mp step
    exact Nat.le_refl _

/-- A source bound for every completed extended history, including adaptive
inquiries represented there; it does not assert the seven-draw schedule for them. -/
theorem extended_trace_source_bound {x y : Port} {es : List FormationClosure.Event}
    (history : Trace FormationClosure.process x es y) :
    y.native.arrived + yieldPerUnit * y.native.source ≤
      x.native.arrived + yieldPerUnit * x.native.source := by
  induction history with
  | nil => exact Nat.le_refl _
  | cons step _ ih => exact Nat.le_trans ih (extended_source_bound step)

/-- Source opportunity is retained through recovery and formation and can
only be consumed by actual probes, including those inside encounters. -/
theorem revising_source_bound {a b : Revising} {e : RevisingEvent}
    (step : revising.step a e b) :
    b.1.native.arrived + yieldPerUnit * b.1.native.source ≤
      a.1.native.arrived + yieldPerUnit * a.1.native.source := by
  cases e with
  | inl event =>
    cases event with
    | inl command => exact native_source_bound step.1.1
    | inr _ =>
      obtain ⟨_, _, reached⟩ := (recover_complete_iff a.1 b.1).mp step.1
      rw [reached]
      exact Nat.le_refl _
  | inr found =>
    obtain ⟨_, z, act, q, reached, _⟩ := step
    rw [reached]
    have bound := native_trace_source_bound q.trace
    have kept := acted_source_retained act
    rw [kept.1, kept.2.1] at bound
    exact bound

/-- Future actual arrivals cannot exceed the source still present at the start.
This is stronger than U1 and does not install an unbounded raw-flow oracle. -/
theorem revising_trace_source_bound {a b : Revising} {es : List RevisingEvent}
    (history : Trace revising a es b) :
    b.1.native.arrived + yieldPerUnit * b.1.native.source ≤
      a.1.native.arrived + yieldPerUnit * a.1.native.source := by
  induction history with
  | nil => exact Nat.le_refl _
  | cons step _ ih => exact Nat.le_trans ih (revising_source_bound step)

/-- Two draws held before probing suffice, regardless of whether the contact
actually converts this packet. The source guard remains mandatory. -/
theorem probe_ready_of_two_draws (s : State) (capacity : peak s ≤ s.capacity)
    (source : 10 ≤ s.source) (covered : 2 * draw s ≤ s.held) : ProbeReady s := by
  apply (probeReady_exact s).2
  refine ⟨capacity, by omega, source, ?_⟩
  omega

/-- Exact probe replenishment in held ticks, after both supported stages. -/
theorem probe_held_balance (s : State) (ready : ProbeReady s) :
    (probeFinal s).held + 2 * draw s = s.held + arrivalAmount s := by
  have balance := step_sustained_exact ⟨_, probe_complete s ready⟩
  change (probeFinal s).held +
    (((s.enacted + draw s) + draw s) - s.enacted) =
      s.held + ((s.arrived + arrivalAmount s) - s.arrived) at balance
  rw [Nat.add_assoc, add_sub_self_left, add_sub_self_left] at balance
  omega

/-- A sufficient transient reserve for the five-command inquiry. This is a
constructed Inquiry, not an assumed successful run or a refreshed initial state. -/
def fundedInquiry (s : State) (capacity : peak s ≤ s.capacity)
    (source : 20 ≤ s.source) (covered : 7 * draw s ≤ s.held) : Inquiry s := by
  let s1 : State := { enact s with phase := if s.broken then s.phase else .p0 }
  let s2 := probeFinal s1
  let s3 : State := { enact s2 with phase := nextPhase s2.phase }
  let s4 : State := { enact s3 with phase := nextPhase s3.phase }
  let s5 := probeFinal s4
  have cover0 : draw s ≤ s.held := by omega
  have h1 : s1.held + draw s = s.held := sub_add_restore _ _ cover0
  have ready1 : ProbeReady s1 := probe_ready_of_two_draws s1 capacity (by change 10 ≤ s.source; omega) (by
    change 2 * draw s ≤ s1.held
    omega)
  have h2 : s2.held + 2 * draw s = s1.held + arrivalAmount s1 := probe_held_balance s1 ready1
  have cover2 : draw s2 ≤ s2.held := by change draw s ≤ s2.held; omega
  have h3 : s3.held + draw s = s2.held := sub_add_restore _ _ cover2
  have cover3 : draw s3 ≤ s3.held := by change draw s ≤ s3.held; omega
  have h4 : s4.held + draw s = s3.held := sub_add_restore _ _ cover3
  have source4 : 10 ≤ s4.source := by change 10 ≤ s.source - 10; omega
  have ready4 : ProbeReady s4 := probe_ready_of_two_draws s4 capacity source4 (by
    change 2 * draw s ≤ s4.held
    omega)
  exact ⟨s1, s2, s3, s4, s5, receiptBit s1, receiptBit s4,
    .silent, .silent, .silent,
    reset_complete s ⟨capacity, cover0⟩, probe_complete s1 ready1,
    a_complete s2 ⟨capacity, cover2⟩, a_complete s3 ⟨capacity, cover3⟩,
    probe_complete s4 ready4⟩

/-- A completed encounter which retains an already open, accurately identified
contact. Its existence requires actual source and transient reserve. -/
theorem funded_open_encounter (a : Revising) (intact : a.1.native.broken = false)
    (opened : a.1.native.blocked = false) (accurate : Accurate a)
    (capacity : peak a.1.native ≤ a.1.native.capacity)
    (source : 20 ≤ a.1.native.source) (covered : 7 * draw a.1.native ≤ a.1.native.held) :
    ∃ b, revising.step a (meet (contact a.1)) b ∧
      b.1.native.source + 20 = a.1.native.source ∧
      b.1.native.held + 7 * draw a.1.native = a.1.native.held + 655360 ∧
      b.1.native.broken = false ∧ b.1.native.blocked = false ∧ Accurate b ∧
      peak b.1.native = peak a.1.native ∧
      b.1.native.capacity = a.1.native.capacity ∧ draw b.1.native = draw a.1.native := by
  let q := fundedInquiry a.1.native capacity source covered
  let b : Revising := (⟨q.s5, a.1.spare, a.1.recovered⟩,
    some (q.reading.arrived0, q.reading.arrived1))
  have select : PortValuation.portOrg.select a.2 (contact a.1) = false :=
    (accurate_selects_blocked accurate _).trans opened
  have step : revising.step a (meet (contact a.1)) b := by
    refine ⟨rfl, a.1, ?_, q, rfl, rfl⟩
    rw [select]
    rfl
  have balance := inquiry_held_balance q intact
  rw [opened] at balance
  have keeps := inquiry_reveals q intact
  refine ⟨b, step, encounter_source_exact step, balance,
    (step_retains_broken step).trans intact, keeps.2.2.2.2.2.1.trans opened,
    encounter_accurate step intact, ?_, ?_, (inquiry_amounts q).2.2⟩
  · rfl
  · rfl

/-- Count only encounters; native probes between them may consume more source. -/
def encounterCount : List RevisingEvent → Nat
  | [] => 0
  | .inl _ :: es => encounterCount es
  | .inr _ :: es => encounterCount es + 1

/-- All other completed events preserve or consume source, never replenish it. -/
theorem revising_source_nonincreasing {a b : Revising} {e : RevisingEvent}
    (step : revising.step a e b) : b.1.native.source ≤ a.1.native.source := by
  cases e with
  | inl event =>
    cases event with
    | inl c => have h := (native_step_amounts step.1.1).1; omega
    | inr _ =>
      obtain ⟨_, _, reached⟩ := (recover_complete_iff a.1 b.1).mp step.1
      rw [reached]
      exact Nat.le_refl _
  | inr found => have h := encounter_source_exact step; omega

/-- A stronger encounter deadline than the general native potential bound.
Every encounter includes two real probes, irrespective of its reading or act. -/
theorem encounter_source_deadline {a b : Revising} {es : List RevisingEvent}
    (history : Trace revising a es b) :
    20 * encounterCount es + b.1.native.source ≤ a.1.native.source := by
  induction history with
  | nil => change 0 + _ ≤ _; exact Nat.le_of_eq (Nat.zero_add _)
  | @cons a m b e es step _ ih =>
    cases e with
    | inl event =>
      exact Nat.le_trans ih (revising_source_nonincreasing step)
    | inr found =>
      have h := encounter_source_exact step
      change 20 * (encounterCount es + 1) + b.1.native.source ≤ a.1.native.source
      omega

/-- A genuinely productive finite continuation: with adequate transient reserve
and seven draws no larger than one actual arrival, every available pair of
source packets supports an encounter. Source is never reset between encounters. -/
theorem finite_replenishing_encounters (n : Nat) (a : Revising)
    (intact : a.1.native.broken = false) (opened : a.1.native.blocked = false)
    (accurate : Accurate a) (capacity : peak a.1.native ≤ a.1.native.capacity)
    (covered : 7 * draw a.1.native ≤ a.1.native.held)
    (adequate : 7 * draw a.1.native ≤ 655360)
    (source : 20 * n ≤ a.1.native.source) :
    ∃ b es, Trace revising a es b ∧ es.length = n ∧ encounterCount es = n ∧
      b.1.native.source + 20 * n = a.1.native.source ∧
      a.1.native.held ≤ b.1.native.held ∧
      b.1.native.held + n * (7 * draw a.1.native) = a.1.native.held + n * 655360 := by
  induction n generalizing a with
  | zero =>
    refine ⟨a, [], .nil _, rfl, rfl, rfl, Nat.le_refl _, ?_⟩
    rw [Nat.zero_mul, Nat.zero_mul]
  | succ n ih =>
    have enough : 20 ≤ a.1.native.source := by omega
    obtain ⟨b, step, sourceB, balance, intactB, openB, accurateB, peakB, capB, drawB⟩ :=
      funded_open_encounter a intact opened accurate capacity enough covered
    have grows : a.1.native.held ≤ b.1.native.held := by omega
    have coveredB : 7 * draw b.1.native ≤ b.1.native.held := by rw [drawB]; omega
    have capacityB : peak b.1.native ≤ b.1.native.capacity := by rw [peakB, capB]; exact capacity
    have adequateB : 7 * draw b.1.native ≤ 655360 := by rw [drawB]; exact adequate
    have enoughB : 20 * n ≤ b.1.native.source := by omega
    obtain ⟨c, es, history, length, count, remaining, holds, balanceC⟩ :=
      ih b intactB openB accurateB capacityB coveredB adequateB enoughB
    refine ⟨c, meet (contact a.1) :: es, .cons step history,
      congrArg Nat.succ length, congrArg Nat.succ count, ?_, Nat.le_trans grows holds, ?_⟩
    · omega
    · rw [drawB] at balanceC
      rw [Nat.succ_mul n (7 * draw a.1.native), Nat.succ_mul n 655360]
      omega

/-- The finite encounter horizon is sharp in this productive regime. This is
an existence/deadline equivalence, not a guarantee that every chosen command
schedule succeeds. Arbitrarily many prior failed probes can waste source. -/
theorem finite_encounter_horizon (n : Nat) (a : Revising)
    (intact : a.1.native.broken = false) (opened : a.1.native.blocked = false)
    (accurate : Accurate a) (capacity : peak a.1.native ≤ a.1.native.capacity)
    (covered : 7 * draw a.1.native ≤ a.1.native.held)
    (adequate : 7 * draw a.1.native ≤ 655360) :
    (∃ b es, Trace revising a es b ∧ encounterCount es = n) ↔
      20 * n ≤ a.1.native.source := by
  constructor
  · rintro ⟨b, es, history, count⟩
    have bound := encounter_source_deadline history
    rw [count] at bound
    omega
  · intro source
    obtain ⟨b, es, history, _, count, _⟩ :=
      finite_replenishing_encounters n a intact opened accurate capacity covered adequate source
    exact ⟨b, es, history, count⟩

/-- ChannelLaw permits an aging tick with no birth and no reserve decrease.
Thus its inequality is a permissive envelope, not the exact port executor. -/
theorem channel_permits_reserve_preserving_tick {Kind : Type u} (law : ChannelLaw Kind)
    (c : Config Kind) :
    (channelProcess law).step c [] ⟨c.reserve, aged c.tokens⟩ := by
  refine ⟨(append_nil_eq _).symm, ?_, ?_⟩
  · change c.reserve + 0 ≤ c.reserve + opened law.rate c.tokens
    exact Nat.le_add_right _ _
  · intro k impossible
    cases impossible

/-- With no source left, every completed revising event strictly lowers held
support. Opening and memory cannot replenish an exhausted represented source. -/
theorem exhausted_revising_step_lowers_held {a b : Revising} {e : RevisingEvent}
    (empty : a.1.native.source = 0) (step : revising.step a e b) :
    b.1.native.held < a.1.native.held := by
  have source := revising_source_nonincreasing step
  have emptyB : b.1.native.source = 0 := by omega
  have lower := revising_lowers_potential step
  change b.1.native.held + yieldPerUnit * b.1.native.source <
    a.1.native.held + yieldPerUnit * a.1.native.source at lower
  rw [emptyB, empty, Nat.mul_zero, Nat.add_zero, Nat.add_zero] at lower
  exact lower

/-- No reserve-faithful one-event inverse can realize even the permissive
reserve-preserving channel tick at an exhausted native state. A forward
abstraction may still omit these extra channel transitions. -/
theorem no_exact_channel_tick_lift_at_exhaustion {Kind : Type u}
    (law : ChannelLaw Kind) (view : Revising → Config Kind)
    (reserve : ∀ a, (view a).reserve = a.1.native.held) (a : Revising)
    (empty : a.1.native.source = 0) :
    (channelProcess law).step (view a) [] ⟨(view a).reserve, aged (view a).tokens⟩ ∧
    ¬ ∃ b e, revising.step a e b ∧
      view b = (⟨(view a).reserve, aged (view a).tokens⟩ : Config Kind) := by
  refine ⟨channel_permits_reserve_preserving_tick law _, ?_⟩
  rintro ⟨b, e, step, mapped⟩
  have same := congrArg Config.reserve mapped
  change (view b).reserve = (view a).reserve at same
  rw [reserve b, reserve a] at same
  have lower := exhausted_revising_step_lowers_held empty step
  rw [same] at lower
  exact Nat.lt_irrefl _ lower

/-- The exact remaining obligations for a reserve-faithful forward map, stated
as an equivalence. The middle clause preserves actual consumed/arrived ticks:
opening is an upper allowance, not automatically an actual source receipt.
The shape and surviving-support clauses cannot be inferred from this budget. -/
theorem channel_step_iff_actual_requirements {Kind : Type u} (law : ChannelLaw Kind)
    (view : Revising → Config Kind)
    (reserve : ∀ a, (view a).reserve = a.1.native.held)
    {a b : Revising} {e : RevisingEvent} (step : revising.step a e b)
    (births : List Kind) :
    (channelProcess law).step (view a) births (view b) ↔
      (view b).tokens = aged (view a).tokens ++ formed law births ∧
      formation law births + revisingArrived a e b ≤
        revisingEnacted a e b + opened law.rate (view a).tokens ∧
      (∀ k, k ∈ births → ∃ tok, tok ∈ aged (view a).tokens ∧ law.edge tok.kind k) := by
  have balance := continues_exact (revising_continues step)
  change b.1.native.held + revisingEnacted a e b =
    a.1.native.held + revisingArrived a e b at balance
  constructor
  · rintro ⟨shape, budget, support⟩
    rw [reserve a, reserve b] at budget
    exact ⟨shape, by omega, support⟩
  · rintro ⟨shape, budget, support⟩
    refine ⟨shape, ?_, support⟩
    rw [reserve a, reserve b]
    omega

/-- Actual arrival supplies a sufficient rate allowance, and actual consumption
supplies a sufficient demand allowance, only when both inequalities and the
aging/support correspondence have independently been established. -/
theorem channel_forward_of_actual_cover {Kind : Type u} (law : ChannelLaw Kind)
    (view : Revising → Config Kind)
    (reserve : ∀ a, (view a).reserve = a.1.native.held)
    {a b : Revising} {e : RevisingEvent} (step : revising.step a e b)
    (births : List Kind)
    (shape : (view b).tokens = aged (view a).tokens ++ formed law births)
    (demand : formation law births ≤ revisingEnacted a e b)
    (arrival : revisingArrived a e b ≤ opened law.rate (view a).tokens)
    (support : ∀ k, k ∈ births → ∃ tok,
      tok ∈ aged (view a).tokens ∧ law.edge tok.kind k) :
    (channelProcess law).step (view a) births (view b) :=
  (channel_step_iff_actual_requirements law view reserve step births).2
    ⟨shape, Nat.add_le_add demand arrival, support⟩

/-- No fixed initial port supports arbitrarily many completed encounters,
including ports in the regime where every encounter locally replenishes held
support. A family with increasing initial source is a different quantifier. -/
theorem no_unbounded_encounters_from_one_start (a : Revising) :
    ¬ ∀ n, ∃ b es, Trace revising a es b ∧ encounterCount es = n := by
  intro unbounded
  obtain ⟨b, es, history, count⟩ := unbounded (a.1.native.source + 1)
  have bound := encounter_source_deadline history
  rw [count] at bound
  omega

/-- Same acquired blocked start, with five encounters' finite source supplied
once at time zero; no spare pair or retained reading is supplied. -/
def replenishingExampleStart : Revising :=
  (⟨{ acquiredStart.native with source := 100 }, 0, 0⟩, none)

def replenishingExampleHistory : List RevisingEvent :=
  revisingHistory ++ [meet (true, false), meet (true, false), meet (true, false)]

/-- Initial failed inquiry, recovery, acquired formation, then three further
open encounters, all in one reached-state history. The finite source is now
exhausted despite growth of held support. -/
theorem actual_acquisition_and_replenishment :
    ∃ b, runRevising replenishingExampleStart replenishingExampleHistory = some b ∧
      Trace revising replenishingExampleStart replenishingExampleHistory b ∧
      encounterCount replenishingExampleHistory = 5 ∧
      b.1.native.source = 0 ∧ b.1.native.held = 2415158 ∧
      b.1.native.enacted = 606282 ∧ b.1.native.arrived = 2621440 ∧
      b.1.native.transferred = 40 ∧ b.1.native.dissipated = 60 ∧
      b.1.spare = 0 ∧ b.1.recovered = 1 ∧ Accurate b := by
  refine ⟨_, rfl, runAgent_sound rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩

end Generative.InquirySufficiency.PortRenewalLawClosure

#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.no_channel_birth_from_empty
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.live_tokens_do_not_stand_still
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.no_contact_only_formation_map
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.read_port_step
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.no_contact_invariant_live_map
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.sourceUsed
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.supportStages
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.native_step_amounts
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.inquiry_amounts
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.inquiry_arrival
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.inquiry_held_balance
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.native_source_bound
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.native_trace_source_bound
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.acted_source_retained
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.encounter_source_exact
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.encounter_enacted_exact
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.encounter_arrival_exact
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.encounter_held_balance
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.encounter_replenishes_iff
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.extended_source_bound
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.extended_trace_source_bound
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.revising_source_bound
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.revising_trace_source_bound
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.probe_ready_of_two_draws
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.probe_held_balance
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.fundedInquiry
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.funded_open_encounter
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.encounterCount
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.revising_source_nonincreasing
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.encounter_source_deadline
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.finite_replenishing_encounters
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.finite_encounter_horizon
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.channel_permits_reserve_preserving_tick
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.exhausted_revising_step_lowers_held
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.no_exact_channel_tick_lift_at_exhaustion
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.channel_step_iff_actual_requirements
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.channel_forward_of_actual_cover
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.no_unbounded_encounters_from_one_start
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.replenishingExampleStart
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.replenishingExampleHistory
#print axioms Generative.InquirySufficiency.PortRenewalLawClosure.actual_acquisition_and_replenishment
