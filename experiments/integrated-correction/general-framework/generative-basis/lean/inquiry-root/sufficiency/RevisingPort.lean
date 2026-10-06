import PortValuation
import ValuationInCore

/-!
# The revising port: valuation and port as one process

`PortValuation` read the port's formation disposition as an organization of the
valuation package, and `ValuationInCore` placed every such organization in the
generative core. The organization and the port were still two processes linked
by a theorem about what an inquiry records. Reading the record and applying the
decision rule were described, not built.

This module builds them. The revising port's state is the extended port together
with what it retains: the last recorded pair of arrivals. Its events are the
port's own activity (native calls and recovery), which leave the retained
reading alone, and encounters. An encounter takes the port's own contact
coordinate, acts on the retained reading (forming the contact when neither
output last arrived), then runs the native inquiry and retains what it records.

No split between an organization and a world is assumed. The valuation
package's "presented condition" is here the port's own contact coordinate, its
consequence law is native execution, and its retained condition is one more
coordinate of the same state. What sets the reading apart from the rest of the
state is only a relation inside the process: activity steps keep it and only
encounters change it (`reading_changes_only_at_encounters`), just as the contact
changes only through formation.

Proved here:

* the consequence law is derived, now including the act: an encounter records the
  profile of the contact its own act leaves (`encounter_effects`);
* the retained readings along every history are exactly the valuation
  organization's run over the contacts met (`memory_is_org_run`), so every
  history is at once a core trace of the organization (`memory_trace`);
* every history is at once an actual history of the extended port
  (`port_trace`), so all formation, recovery and ledger results apply to it;
* the contact class changes only through the organization's own selection
  (`class_change_requires_selection`);
* once the contact has been met, the disposition forms exactly when the contact
  is blocked, through any later activity (`met_selects_blocked`). Reading after
  acting removes the staleness `PortValuation` found when the reading preceded
  the act;
* one executed history from a blocked class-C port with no spares: the first
  encounter finds no arrival, recovery turns that waste into a pair, the second
  encounter forms on the port's own reading and records an arrival
  (`revising_loop`).

Each part of the encounter is necessary for the claim that the disposition
forms exactly when blocked, and is proved so here rather than assumed. The
decision rule is the only rule on recorded arrivals that does it
(`decision_rule_unique`). One output's arrival never suffices
(`one_output_cannot_decide`), so two probes at different outputs are needed;
after an intact reset the other output is first reached after two rotations
(`other_output_after_two_rotations`). The intact reset cannot be dropped: a
broken reset can probe the same output twice, and then no rule decides
(`broken_reset_cannot_decide`). Reading after acting is needed too:
`PortValuation.disposition_stale_then_recovers` shows the reading taken before
the act goes stale.

Two inputs of the extended port remain and are the next to remove: the recovery
rate of ten wasted units per pair (being grounded in a separate thread), and
the formation rule (formation meets the native interface demand and clears
`blocked`). "Valuation" keeps the package's thin functional sense: a selective
disposition.
-/

namespace Generative.InquirySufficiency.RevisingPort

open Generative NativePacketProcess PacketLawDerivation
open FormationClosure FormationLaw AcquiredContact ValuationDevelopment PortValuation

/-- The consequence of acting `a` toward contact `x`: what an inquiry then records.
Forming opens the contact; not forming leaves it. -/
def actingConsequence : World (Bool × Bool) Bool (Bool × Bool) :=
  fun x a => profile x.1 (x.2 && !a)

/-- The retained reading: none before any encounter. -/
abbrev Memory := Option (Bool × Bool)

abbrev Revising := Port × Memory

/-- The port's own activity, or an encounter with the contact it finds in its own state. -/
abbrev RevisingEvent := Sum (Sum NativePacketProcess.Command Unit) (Bool × Bool)

/-- What the act does: form the contact, or leave the port as it is. -/
def acted : Bool → Port → Port → Prop
  | true, x, z => formation.step x () z
  | false, x, z => z = x

/-- The revising port. Activity keeps the retained reading. An encounter meets the
present contact, acts on the retained reading, inquires, and retains the record. -/
def revising : Process Revising RevisingEvent where
  step a e b := match e with
    | .inl event => activity.step a.1 event b.1 ∧ b.2 = a.2
    | .inr found => contact a.1 = found ∧
        ∃ z, acted (portOrg.select a.2 found) a.1 z ∧
          ∃ q : Inquiry z.native, b.1 = ⟨q.s5, z.spare, z.recovered⟩ ∧
            b.2 = some (q.reading.arrived0, q.reading.arrived1)

/-! ## Retained parameters -/

theorem inquiry_retains_broken {s : NativePacketProcess.State} (q : Inquiry s) :
    q.s5.broken = s.broken := by
  rw [(completed_retains_parameters q.step5).2.2.1, (completed_retains_parameters q.step4).2.2.1,
    (completed_retains_parameters q.step3).2.2.1, (completed_retains_parameters q.step2).2.2.1,
    (completed_retains_parameters q.step1).2.2.1]

theorem activity_retains_broken {x y : Port} {e : Sum NativePacketProcess.Command Unit}
    (step : activity.step x e y) : y.native.broken = x.native.broken := by
  cases e with
  | inl command =>
    obtain ⟨⟨_, actual⟩, _, _⟩ := step
    exact (completed_retains_parameters actual).2.2.1
  | inr _ =>
    obtain ⟨_, _, rfl⟩ := (recover_complete_iff x y).mp step
    rfl

theorem acted_effects {b : Bool} {x z : Port} (act : acted b x z) :
    z.native.broken = x.native.broken ∧ contact z = (x.native.tau, x.native.blocked && !b) := by
  cases b with
  | true =>
    obtain ⟨_, _, rfl⟩ := (formPort_complete_iff x z).mp act
    show _ ∧ (x.native.tau, false) = (x.native.tau, x.native.blocked && false)
    cases x.native.blocked <;> exact ⟨rfl, rfl⟩
  | false =>
    rw [act]
    show x.native.broken = x.native.broken ∧
      (x.native.tau, x.native.blocked) = (x.native.tau, x.native.blocked && true)
    cases x.native.blocked <;> exact ⟨rfl, rfl⟩

/-- Every step of the revising port keeps the reset intact or broken as it was. -/
theorem step_retains_broken {a b : Revising} {e : RevisingEvent} (step : revising.step a e b) :
    b.1.native.broken = a.1.native.broken := by
  cases e with
  | inl event => exact activity_retains_broken step.1
  | inr found =>
    obtain ⟨_, z, act, q, reached, _⟩ := step
    rw [reached]
    exact (inquiry_retains_broken q).trans (acted_effects act).1

theorem trace_retains_broken {a b : Revising} {es : List RevisingEvent} (trace : Trace revising a es b) :
    b.1.native.broken = a.1.native.broken := by
  induction trace with
  | nil => rfl
  | cons step _ ih => exact ih.trans (step_retains_broken step)

/-! ## One encounter -/

/-- An encounter records the profile of the contact its own act leaves, and that
contact is what the port carries on with. The consequence law is derived. -/
theorem encounter_effects {a b : Revising} {found : Bool × Bool}
    (step : revising.step a (.inr found) b) (intact : a.1.native.broken = false) :
    b.2 = portOrg.next actingConsequence a.2 found ∧
      contact b.1 = (found.1, found.2 && !portOrg.select a.2 found) := by
  obtain ⟨met, z, act, q, reached, retained⟩ := step
  subst met
  obtain ⟨broken, shape⟩ := acted_effects act
  have intactZ : z.native.broken = false := broken.trans intact
  have reads := inquiry_reads_profile q intactZ
  obtain ⟨_, _, _, _, sameTau, sameBlocked, _⟩ := inquiry_reveals q intactZ
  have tauZ : z.native.tau = a.1.native.tau := congrArg Prod.fst shape
  have blockedZ : z.native.blocked = (a.1.native.blocked && !portOrg.select a.2 (contact a.1)) :=
    congrArg Prod.snd shape
  constructor
  · rw [retained, reads, tauZ, blockedZ]
    rfl
  · rw [reached]
    show (q.s5.tau, q.s5.blocked) = _
    rw [sameTau, sameBlocked, tauZ, blockedZ]
    rfl

/-! ## Whole histories -/

/-- The contacts met, in order. -/
def encounters : List RevisingEvent → List (Bool × Bool)
  | [] => []
  | .inl _ :: rest => encounters rest
  | .inr found :: rest => found :: encounters rest

/-- What the revising port retains is exactly the valuation organization's run
over the contacts it met. -/
theorem memory_is_org_run {a b : Revising} {es : List RevisingEvent} (trace : Trace revising a es b)
    (intact : a.1.native.broken = false) :
    b.2 = portOrg.run actingConsequence a.2 (encounters es) := by
  induction trace with
  | nil => rfl
  | @cons a m b e rest step _ ih =>
    have intactM : m.1.native.broken = false := (step_retains_broken step).trans intact
    cases e with
    | inl event =>
      rw [ih intactM, step.2]
      rfl
    | inr found =>
      rw [ih intactM, (encounter_effects step intact).1]
      rfl

/-- The same history is a core trace of the valuation organization. -/
theorem memory_trace {a b : Revising} {es : List RevisingEvent} (trace : Trace revising a es b)
    (intact : a.1.native.broken = false) :
    Trace (ValuationInCore.orgProcess portOrg actingConsequence) a.2 (encounters es) b.2 :=
  (ValuationInCore.trace_iff_run portOrg actingConsequence _ _ _).mpr
    (memory_is_org_run trace intact).symm

/-- The reading is set apart only by which steps change it: histories without
an encounter keep it. -/
theorem reading_changes_only_at_encounters {a b : Revising} {es : List RevisingEvent}
    (trace : Trace revising a es b) (none : encounters es = []) : b.2 = a.2 := by
  induction trace with
  | nil => rfl
  | @cons a m b e rest step _ ih =>
    cases e with
    | inl event => exact (ih none).trans step.2
    | inr found => cases (show found :: encounters rest = [] from none)

/-- The act an encounter performs, as extended-port events. -/
def actEvents : Bool → List Event
  | true => [formE]
  | false => []

/-- The extended-port events a history performs, threading the retained reading. -/
def expand : Memory → List RevisingEvent → List Event
  | _, [] => []
  | m, .inl event :: rest => .inl event :: expand m rest
  | m, .inr found :: rest =>
    actEvents (portOrg.select m found) ++ nativeRun inquiryCommands ++
      expand (portOrg.next actingConsequence m found) rest

theorem act_trace {b : Bool} {x z : Port} (act : acted b x z) :
    Trace FormationClosure.process x (actEvents b) z := by
  cases b with
  | true => exact .cons act (.nil z)
  | false =>
    cases act
    exact .nil _

/-- A completed inquiry is an actual history of the extended port. -/
theorem lift_native (z : Port) {s t : NativePacketProcess.State}
    {command : NativePacketProcess.Command} {o : Observation}
    (actual : execute s command = .complete t o) :
    FormationClosure.process.step ⟨s, z.spare, z.recovered⟩ (nativeE command)
      ⟨t, z.spare, z.recovered⟩ :=
  ⟨⟨o, actual⟩, rfl, rfl⟩

theorem inquiry_port_trace (z : Port) (q : Inquiry z.native) :
    Trace FormationClosure.process z (nativeRun inquiryCommands) ⟨q.s5, z.spare, z.recovered⟩ :=
  .cons (lift_native z q.step1) (.cons (lift_native z q.step2) (.cons (lift_native z q.step3)
    (.cons (lift_native z q.step4) (.cons (lift_native z q.step5) (.nil _)))))

/-- Every history of the revising port is an actual history of the extended port. -/
theorem port_trace {a b : Revising} {es : List RevisingEvent} (trace : Trace revising a es b)
    (intact : a.1.native.broken = false) :
    Trace FormationClosure.process a.1 (expand a.2 es) b.1 := by
  induction trace with
  | nil => exact .nil _
  | @cons a m b e rest step _ ih =>
    have intactM : m.1.native.broken = false := (step_retains_broken step).trans intact
    cases e with
    | inl event =>
      have kept : m.2 = a.2 := step.2
      have tail := ih intactM
      rw [kept] at tail
      exact .cons step.1 tail
    | inr found =>
      have memory := (encounter_effects step intact).1
      obtain ⟨_, z, act, q, reached, _⟩ := step
      have tail := ih intactM
      rw [memory] at tail
      rw [reached] at tail
      exact trace_append_iff.mpr ⟨_, trace_append_iff.mpr ⟨z, act_trace act,
        inquiry_port_trace z q⟩, tail⟩

/-- How many encounters selected formation. -/
def selections : Memory → List RevisingEvent → Nat
  | _, [] => 0
  | m, .inl _ :: rest => selections m rest
  | m, .inr found :: rest =>
    (match portOrg.select m found with | true => 1 | false => 0) +
      selections (portOrg.next actingConsequence m found) rest

theorem formations_append (xs ys : List Event) :
    formations (xs ++ ys) = formations xs + formations ys := by
  induction xs with
  | nil => exact (Nat.zero_add _).symm
  | cons e rest ih =>
    cases e with
    | inl _ => exact ih
    | inr _ =>
      show formations (rest ++ ys) + 1 = formations rest + 1 + formations ys
      rw [ih, Nat.add_right_comm]

theorem inquiry_forms_nothing : formations (nativeRun inquiryCommands) = 0 := rfl

/-- The port's formations are exactly the organization's selections to form. -/
theorem formations_are_selections (m : Memory) (es : List RevisingEvent) :
    formations (expand m es) = selections m es := by
  induction es generalizing m with
  | nil => rfl
  | cons e rest ih =>
    cases e with
    | inl event => exact ih m
    | inr found =>
      show formations (actEvents (portOrg.select m found) ++ nativeRun inquiryCommands ++
        expand (portOrg.next actingConsequence m found) rest) = _
      rw [formations_append, formations_append, inquiry_forms_nothing, Nat.add_zero,
        ih (portOrg.next actingConsequence m found)]
      show _ = (match portOrg.select m found with | true => 1 | false => 0) +
        selections (portOrg.next actingConsequence m found) rest
      cases portOrg.select m found <;> rfl

/-- The contact class changes only through the organization's own selection. -/
theorem class_change_requires_selection {a b : Revising} {es : List RevisingEvent}
    (trace : Trace revising a es b) (intact : a.1.native.broken = false)
    (changed : targetOf b.1.native.tau b.1.native.blocked =
      targetOf a.1.native.tau a.1.native.blocked → False) :
    1 ≤ selections a.2 es := by
  rw [← formations_are_selections]
  exact class_change_requires_formation (port_trace trace intact) changed

/-! ## The disposition after the contact has been met -/

/-- The retained reading is the profile of the present contact. -/
def Accurate (a : Revising) : Prop := a.2 = some (profile a.1.native.tau a.1.native.blocked)

theorem accurate_selects_blocked {a : Revising} (accurate : Accurate a) (x : Bool × Bool) :
    portOrg.select a.2 x = a.1.native.blocked := by
  unfold Accurate at accurate
  rw [accurate]
  cases a.1.native.tau <;> cases a.1.native.blocked <;> rfl

/-- After any encounter the retained reading is accurate. -/
theorem encounter_accurate {a b : Revising} {found : Bool × Bool}
    (step : revising.step a (.inr found) b) (intact : a.1.native.broken = false) :
    Accurate b := by
  obtain ⟨memory, shape⟩ := encounter_effects step intact
  unfold Accurate
  rw [memory]
  show some (profile found.1 (found.2 && !portOrg.select a.2 found)) = _
  rw [show b.1.native.tau = found.1 from congrArg Prod.fst shape,
    show b.1.native.blocked = _ from congrArg Prod.snd shape]

/-- Activity keeps the retained reading accurate: it changes neither the reading
nor the contact. -/
theorem activity_keeps_accurate {a b : Revising} {event : Sum NativePacketProcess.Command Unit}
    (step : revising.step a (.inl event) b) (accurate : Accurate a) : Accurate b := by
  have same := activity_retains_contact a.1 event b.1 step.1
  unfold Accurate
  rw [step.2, accurate]
  show some (profile (contact a.1).1 (contact a.1).2) = some (profile (contact b.1).1 (contact b.1).2)
  rw [same]

theorem step_keeps_accurate {a b : Revising} {e : RevisingEvent} (step : revising.step a e b)
    (intact : a.1.native.broken = false) (accurate : Accurate a) : Accurate b := by
  cases e with
  | inl event => exact activity_keeps_accurate step accurate
  | inr found => exact encounter_accurate step intact

theorem trace_keeps_accurate {a b : Revising} {es : List RevisingEvent} (trace : Trace revising a es b)
    (intact : a.1.native.broken = false) (accurate : Accurate a) : Accurate b := by
  induction trace with
  | nil => exact accurate
  | cons step _ ih =>
    exact ih ((step_retains_broken step).trans intact) (step_keeps_accurate step intact accurate)

/-- Once the contact has been met, through any later activity and encounters,
the disposition forms exactly when the present contact is blocked: never
redundantly and never too late. -/
theorem met_selects_blocked {a m b : Revising} {found : Bool × Bool} {es : List RevisingEvent}
    (first : revising.step a (.inr found) m) (later : Trace revising m es b)
    (intact : a.1.native.broken = false) (x : Bool × Bool) :
    portOrg.select b.2 x = b.1.native.blocked :=
  accurate_selects_blocked (trace_keeps_accurate later ((step_retains_broken first).trans intact)
    (encounter_accurate first intact)) x

/-! ## One executed history -/

/-- One completed control call, with its proof. -/
def controlOf (s : NativePacketProcess.State) (command : NativePacketProcess.Command) :
    (r : Result) → execute s command = r → Option (Σ' t o, execute s command = .complete t o)
  | .complete t o, h => some ⟨t, o, h⟩
  | .stopped _ _, _ => none

def controlStep (s : NativePacketProcess.State) (command : NativePacketProcess.Command) :
    Option (Σ' t o, execute s command = .complete t o) :=
  controlOf s command (execute s command) rfl

/-- One completed probe with its receipt, with its proof. -/
def probeOf (s : NativePacketProcess.State) :
    (r : Result) → execute s .probe = r → Option (Σ' t r, execute s .probe = .complete t (.receipt r))
  | .complete t (.receipt r), h => some ⟨t, r, h⟩
  | .complete _ .silent, _ => none
  | .complete _ (.reading _), _ => none
  | .stopped _ _, _ => none

def probeStep (s : NativePacketProcess.State) :
    Option (Σ' t r, execute s .probe = .complete t (.receipt r)) :=
  probeOf s (execute s .probe) rfl

/-- Execute the five inquiry commands, keeping each intermediate state. -/
def inquire (s : NativePacketProcess.State) : Option (Inquiry s) :=
  match controlStep s .reset with
  | none => none
  | some ⟨s1, o1, h1⟩ => match probeStep s1 with
    | none => none
    | some ⟨s2, r0, h2⟩ => match controlStep s2 .a with
      | none => none
      | some ⟨s3, o3, h3⟩ => match controlStep s3 .a with
        | none => none
        | some ⟨s4, o4, h4⟩ => match probeStep s4 with
          | none => none
          | some ⟨s5, r1, h5⟩ => some ⟨s1, s2, s3, s4, s5, r0, r1, o1, o3, o4, h1, h2, h3, h4, h5⟩

def actPort : Bool → Port → Option Port
  | true, x => completeOutcome (formPort x)
  | false, x => some x

theorem actPort_sound {b : Bool} {x z : Port} (ran : actPort b x = some z) : acted b x z := by
  cases b with
  | true => exact completeOutcome_some ran
  | false =>
    cases ran
    rfl

def encounterPort (z : Port) : Option Revising :=
  match inquire z.native with
  | some q => some (⟨q.s5, z.spare, z.recovered⟩, some (q.reading.arrived0, q.reading.arrived1))
  | none => none

/-- Keep the retained reading through a completed port event. -/
def keep (a : Revising) : Option Port → Option Revising
  | some y => some (y, a.2)
  | none => none

/-- Inquire after a completed act. -/
def afterAct : Option Port → Option Revising
  | some z => encounterPort z
  | none => none

def runRevisingEvent (a : Revising) : RevisingEvent → Option Revising
  | .inl event => keep a (runEvent a.1 (.inl event))
  | .inr found =>
    if contact a.1 = found then afterAct (actPort (portOrg.select a.2 found) a.1)
    else none

def runRevising (a : Revising) : List RevisingEvent → Option Revising
  | [] => some a
  | e :: rest => match runRevisingEvent a e with
    | some b => runRevising b rest
    | none => none

theorem encounterPort_sound {z : Port} {b : Revising} (ran : encounterPort z = some b) :
    ∃ q : Inquiry z.native, b.1 = ⟨q.s5, z.spare, z.recovered⟩ ∧
      b.2 = some (q.reading.arrived0, q.reading.arrived1) := by
  unfold encounterPort at ran
  split at ran
  next q _ =>
    cases ran
    exact ⟨q, rfl, rfl⟩
  next => cases ran

theorem keep_some {a b : Revising} {result : Option Port} (ran : keep a result = some b) :
    result = some b.1 ∧ b.2 = a.2 := by
  cases result with
  | some y =>
    cases ran
    exact ⟨rfl, rfl⟩
  | none => cases ran

theorem afterAct_some {result : Option Port} {b : Revising} (ran : afterAct result = some b) :
    ∃ z, result = some z ∧ encounterPort z = some b := by
  cases result with
  | some z => exact ⟨z, rfl, ran⟩
  | none => cases ran

theorem runAgentEvent_sound {a b : Revising} {e : RevisingEvent} (ran : runRevisingEvent a e = some b) :
    revising.step a e b := by
  cases e with
  | inl event =>
    obtain ⟨completed, kept⟩ := keep_some ran
    exact ⟨runEvent_sound completed, kept⟩
  | inr found =>
    change (if contact a.1 = found then afterAct (actPort (portOrg.select a.2 found) a.1)
      else none) = some b at ran
    by_cases met : contact a.1 = found
    · rw [if_pos met] at ran
      obtain ⟨z, acting, inquired⟩ := afterAct_some ran
      exact ⟨met, z, actPort_sound acting, encounterPort_sound inquired⟩
    · rw [if_neg met] at ran
      cases ran

theorem runAgent_sound {a b : Revising} {es : List RevisingEvent} (ran : runRevising a es = some b) :
    Trace revising a es b := by
  induction es generalizing a with
  | nil =>
    cases ran
    exact .nil _
  | cons e rest ih =>
    unfold runRevising at ran
    split at ran
    next m stepped => exact .cons (runAgentEvent_sound stepped) (ih ran)
    next => cases ran

def recoverR : RevisingEvent := .inl (.inr ())
def meet (found : Bool × Bool) : RevisingEvent := .inr found

/-- Meet the blocked contact, recover the waste of that encounter, meet it again. -/
def revisingHistory : List RevisingEvent := [meet (true, true), recoverR, meet (true, true)]

/-- From a blocked class-C port with no spares and nothing retained: the first
encounter does not form (nothing is retained yet) and records no arrival;
recovery turns that waste into a pair; the second encounter forms on the port's
own reading and records one arrival. The port ends in class B with ten units
transferred, its reading accurate, and its disposition no longer forming. -/
theorem revising_loop :
    ∃ b, runRevising (acquiredStart, none) revisingHistory = some b ∧
      Trace revising (acquiredStart, none) revisingHistory b ∧
      targetOf acquiredStart.native.tau acquiredStart.native.blocked = .C ∧
      targetOf b.1.native.tau b.1.native.blocked = .B ∧
      b.2 = some (true, false) ∧ portOrg.select b.2 (contact b.1) = false ∧
      b.1.native.transferred = 10 ∧ b.1.native.wasted = 30 ∧
      b.1.spare = 0 ∧ b.1.recovered = 1 ∧
      selections none revisingHistory = 1 ∧
      expand none revisingHistory = acquiredHistory := by
  exact ⟨_, rfl, runAgent_sound rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩

/-! ## Why the rule, the two probes and the intact reset

None of these is a free choice. Each is necessary for the claim that the
disposition forms exactly when the contact is blocked. -/

/-- No contact configuration makes both outputs arrive. -/
theorem profile_never_both (tau blocked : Bool) : profile tau blocked ≠ (true, true) := by
  cases tau <;> cases blocked <;> decide

/-- The decision rule is forced: a rule on recorded arrivals forms exactly when
the contact is blocked if and only if it is `!r.1 && !r.2` on every reading a
port can produce. The one reading no port produces is left free. -/
theorem decision_rule_unique (f : Bool × Bool → Bool) :
    (∀ tau blocked, f (profile tau blocked) = blocked) ↔
      ∀ r, r ≠ (true, true) → f r = (!r.1 && !r.2) := by
  constructor
  · intro decides r possible
    obtain ⟨r1, r2⟩ := r
    cases r1 <;> cases r2
    · exact decides false true
    · exact decides false false
    · exact decides true false
    · exact absurd rfl possible
  · intro agrees tau blocked
    rw [agrees _ (profile_never_both tau blocked)]
    cases tau <;> cases blocked <;> rfl

/-- The organization's rule is that rule. -/
theorem portOrg_rule (r : Bool × Bool) (x : Bool × Bool) :
    portOrg.select (some r) x = (!r.1 && !r.2) := rfl

/-- One output's arrival cannot decide the contact: whichever output is tested,
no rule on its arrival forms exactly when blocked. Both outputs must be recorded,
so the inquiry needs two probes at different outputs. -/
theorem one_output_cannot_decide (o : Bool) (f : Bool → Bool) :
    ¬ ∀ tau blocked, f (arrivalAt o tau blocked) = blocked := by
  intro decides
  cases o
  · exact Bool.noConfusion ((decides false true).symm.trans (decides false false))
  · exact Bool.noConfusion ((decides true true).symm.trans (decides true false))

/-- From the phase an intact reset fixes, the next phase probes the same output;
the other output is first reached after two rotations. -/
theorem other_output_after_two_rotations :
    output .p0 = false ∧ output (nextPhase .p0) = false ∧ output (nextPhase (nextPhase .p0)) = true :=
  ⟨rfl, rfl, rfl⟩

/-- A port whose reset is broken, resting in phase `p1`. -/
def brokenPort (blocked : Bool) : NativePacketProcess.State :=
  { phase := .p1, tau := false, sigma := false, broken := true, blocked := blocked,
    receiptFlip := false, source := 40, fuel := 400000, live := 0, workspace := 0,
    capacity := 10, spent := 0, income := 0, transferred := 0, wasted := 0 }

/-- Its completed inquiries, blocked and open. -/
def brokenInquiry (blocked : Bool) : Inquiry (brokenPort blocked) :=
  (inquire (brokenPort blocked)).get (by cases blocked <;> rfl)

/-- With a broken reset both probes can test the same output, so a blocked and an
open contact leave identical readings. -/
theorem broken_readings_agree : (brokenInquiry true).reading = (brokenInquiry false).reading := rfl

/-- The intact reset cannot be dropped: no rule on what an inquiry records forms
exactly when the contact is blocked for every port. -/
theorem broken_reset_cannot_decide (f : Reading → Bool) :
    ¬ ∀ s (q : Inquiry s), f q.reading = s.blocked := by
  intro decides
  have blocked := decides _ (brokenInquiry true)
  have opened := decides _ (brokenInquiry false)
  rw [broken_readings_agree] at blocked
  exact Bool.noConfusion (blocked.symm.trans opened)

end Generative.InquirySufficiency.RevisingPort

#print axioms Generative.InquirySufficiency.RevisingPort.actingConsequence
#print axioms Generative.InquirySufficiency.RevisingPort.acted
#print axioms Generative.InquirySufficiency.RevisingPort.revising
#print axioms Generative.InquirySufficiency.RevisingPort.inquiry_retains_broken
#print axioms Generative.InquirySufficiency.RevisingPort.activity_retains_broken
#print axioms Generative.InquirySufficiency.RevisingPort.acted_effects
#print axioms Generative.InquirySufficiency.RevisingPort.step_retains_broken
#print axioms Generative.InquirySufficiency.RevisingPort.trace_retains_broken
#print axioms Generative.InquirySufficiency.RevisingPort.encounter_effects
#print axioms Generative.InquirySufficiency.RevisingPort.encounters
#print axioms Generative.InquirySufficiency.RevisingPort.memory_is_org_run
#print axioms Generative.InquirySufficiency.RevisingPort.memory_trace
#print axioms Generative.InquirySufficiency.RevisingPort.actEvents
#print axioms Generative.InquirySufficiency.RevisingPort.expand
#print axioms Generative.InquirySufficiency.RevisingPort.act_trace
#print axioms Generative.InquirySufficiency.RevisingPort.lift_native
#print axioms Generative.InquirySufficiency.RevisingPort.inquiry_port_trace
#print axioms Generative.InquirySufficiency.RevisingPort.port_trace
#print axioms Generative.InquirySufficiency.RevisingPort.selections
#print axioms Generative.InquirySufficiency.RevisingPort.formations_append
#print axioms Generative.InquirySufficiency.RevisingPort.inquiry_forms_nothing
#print axioms Generative.InquirySufficiency.RevisingPort.formations_are_selections
#print axioms Generative.InquirySufficiency.RevisingPort.class_change_requires_selection
#print axioms Generative.InquirySufficiency.RevisingPort.Accurate
#print axioms Generative.InquirySufficiency.RevisingPort.accurate_selects_blocked
#print axioms Generative.InquirySufficiency.RevisingPort.encounter_accurate
#print axioms Generative.InquirySufficiency.RevisingPort.activity_keeps_accurate
#print axioms Generative.InquirySufficiency.RevisingPort.step_keeps_accurate
#print axioms Generative.InquirySufficiency.RevisingPort.trace_keeps_accurate
#print axioms Generative.InquirySufficiency.RevisingPort.met_selects_blocked
#print axioms Generative.InquirySufficiency.RevisingPort.controlOf
#print axioms Generative.InquirySufficiency.RevisingPort.controlStep
#print axioms Generative.InquirySufficiency.RevisingPort.probeOf
#print axioms Generative.InquirySufficiency.RevisingPort.probeStep
#print axioms Generative.InquirySufficiency.RevisingPort.inquire
#print axioms Generative.InquirySufficiency.RevisingPort.actPort
#print axioms Generative.InquirySufficiency.RevisingPort.actPort_sound
#print axioms Generative.InquirySufficiency.RevisingPort.encounterPort
#print axioms Generative.InquirySufficiency.RevisingPort.keep
#print axioms Generative.InquirySufficiency.RevisingPort.afterAct
#print axioms Generative.InquirySufficiency.RevisingPort.runRevisingEvent
#print axioms Generative.InquirySufficiency.RevisingPort.runRevising
#print axioms Generative.InquirySufficiency.RevisingPort.encounterPort_sound
#print axioms Generative.InquirySufficiency.RevisingPort.keep_some
#print axioms Generative.InquirySufficiency.RevisingPort.afterAct_some
#print axioms Generative.InquirySufficiency.RevisingPort.runAgentEvent_sound
#print axioms Generative.InquirySufficiency.RevisingPort.runAgent_sound
#print axioms Generative.InquirySufficiency.RevisingPort.revisingHistory
#print axioms Generative.InquirySufficiency.RevisingPort.revising_loop
#print axioms Generative.InquirySufficiency.RevisingPort.profile_never_both
#print axioms Generative.InquirySufficiency.RevisingPort.decision_rule_unique
#print axioms Generative.InquirySufficiency.RevisingPort.portOrg_rule
#print axioms Generative.InquirySufficiency.RevisingPort.one_output_cannot_decide
#print axioms Generative.InquirySufficiency.RevisingPort.other_output_after_two_rotations
#print axioms Generative.InquirySufficiency.RevisingPort.brokenPort
#print axioms Generative.InquirySufficiency.RevisingPort.brokenInquiry
#print axioms Generative.InquirySufficiency.RevisingPort.broken_readings_agree
#print axioms Generative.InquirySufficiency.RevisingPort.broken_reset_cannot_decide
#print axioms Generative.InquirySufficiency.RevisingPort.reading_changes_only_at_encounters
