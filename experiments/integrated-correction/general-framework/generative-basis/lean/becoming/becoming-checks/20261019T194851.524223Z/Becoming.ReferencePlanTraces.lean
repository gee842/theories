import Becoming.ReferencePlan

/-!
# Reference-plan traces: revision of a reference plan as a process of the spine

`Becoming.ReferencePlan` states a history in which acquired mismatch revises the next reference
plan: an act is performed at an address of a channel, a mismatch revises the retained method,
probes acquire both references of each planned contact, a checked installation binds them, and
every act uses fuel. Its step is already a process of the spine, `ReferencePlan.P`, whose step
from `s` by `a` to `t` is `execute s a = some t`; most of its laws were stated of `operate`,
`execute`, `run` and `repair` and so stood apart from the base. This module reads them as laws of
that process, its steps and its traces.

* **The readings, exact.** A step of the process is an operation with the fuel it uses
  (`step_iff`, `enabled_iff`); the source's executed act sequences are exactly the process's
  traces (`run_iff`), whose end is therefore determined (`trace_unique`). The repair policy is
  the process of the acts `choose` picks (`chosen`), and the source's repairs of `n` steps are
  exactly its traces of length `n` (`repair_iff`).
* **Laws of the steps.** Every revise step puts the failed address at the head of the method and
  of the next plan, leaving the installed device in place (`revise_binds_plan`, `revise_step`);
  so the revised method contacts the failed address (`revise_registers`), keeps every selection the
  old one made (`revise_keeps_selections`, `revise_keeps`), and gains the choice at a new
  contact (`revise_gains_contact`). A probe step acquires both references of the next planned
  contact (`probe_binds`), a checked install step binds the fresh pairs (`install_binds`), and a
  frozen step re-runs the retained method whatever failed (`frozen_plan`), so at every retained
  method some failure is left unanswered (`frozen_leaves_unregistered`). A perform step
  answers through the installed key (`perform_response`); a key read off the low reference
  drives the contact to every target exactly where the two references differ
  (`checked_drives`), and after a drift step it misses every target (`drift_misses`).
* **The native history as traces.** The first use fails (`first_mismatch_step`) and the policy
  repairs in three steps (`first_repair`); the repaired contact is then used and a new address
  fails (`second_mismatch_trace`), the policy repairs in four steps (`second_repair`), and both
  revised contacts are used (`finished_trace`). The history is its two rounds and the last uses
  (`firstRound`, `secondRound`, `actualWord_rounds`, `history_rounds`); the rounds change the
  method twice (`rounds_change_method`), install each new contact and gain its choice
  (`first_round_installs_contact`, `first_round_registers`, `second_round_registers`), and after
  each round every use of an installed contact meets its target (`first_round_meets`,
  `second_round_meets`, `first_use_meets`, `second_use_meets`). The history ends with half its
  fuel used and none restored (`history_uses_fuel`).
* **The controls as traces.** The frozen controls run and still fail
  (`frozen_control_fails`, `frozen_second_control_fails`); a drift after a checked repair runs
  into a mismatch (`drift_control_fails`); after an erased mismatch the policy has no step
  (`erased_no_repair`); with too little fuel or a constant channel the policy cannot complete a
  repair (`small_support_no_repair`, `constant_channel_no_repair`) while its contacts still use
  fuel (`small_support_uses_fuel`, `constant_channel_uses_fuel`); with no fuel no act is enabled
  (`exhausted_not_enabled`).

The local primitives of the source (two-reference binding, the Boolean channel family, the
revision policy) stay supplied, as the source says. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace ReferencePlanTraces

open ReferencePlan

/-! ## The readings -/

/-- **A step of the process is an operation with the fuel it uses**: enough fuel for the act, and
the operation's outcome with that fuel moved from what is held to what is used. -/
theorem step_iff {s t : State} {a : Act} :
    P.step s a t ↔ use a ≤ s.fuel ∧
      ∃ u, operate s a = some u ∧ t = { u with fuel := s.fuel - use a, used := s.used + use a } := by
  constructor
  · intro h
    change execute s a = some t at h
    unfold execute at h
    split at h
    next enough =>
      cases eq : operate s a with
      | none => rw [eq] at h; contradiction
      | some u =>
        rw [eq] at h
        exact ⟨enough, u, rfl, (Option.some.inj h).symm⟩
    next => contradiction
  · intro ⟨enough, u, op, eq⟩
    change execute s a = some t
    unfold execute
    rw [if_pos enough, op, eq]

/-- **An act is enabled exactly where its fuel is held and its operation has an outcome.** -/
theorem enabled_iff {s : State} {a : Act} :
    Enabled P s a ↔ use a ≤ s.fuel ∧ ∃ u, operate s a = some u :=
  ⟨fun ⟨_, st⟩ => match step_iff.mp st with
    | ⟨enough, u, op, _⟩ => ⟨enough, u, op⟩,
   fun ⟨enough, u, op⟩ => ⟨_, step_iff.mpr ⟨enough, u, op, rfl⟩⟩⟩

/-- **The source's executed act sequences are exactly the traces of the process.** -/
theorem run_iff {s t : State} {as : List Act} : ReferencePlan.run s as = some t ↔ Trace P s as t :=
  ⟨run_trace, fun h => by
    induction h with
    | nil => rfl
    | @cons s m t a as step _ ih =>
      change (execute s a).bind (fun x => ReferencePlan.run x as) = some t
      rw [step]
      exact ih⟩

/-- The end of a trace of the process is determined by where it starts and its acts. -/
theorem trace_unique {s t u : State} {as : List Act} (h : Trace P s as t) (h' : Trace P s as u) :
    t = u :=
  Option.some.inj ((run_iff.mpr h).symm.trans (run_iff.mpr h'))

/-- Where an act sequence executes to `t₀`, its trace ends exactly at `t₀`. -/
theorem trace_iff_of_run {s t₀ t : State} {as : List Act} (h : ReferencePlan.run s as = some t₀) :
    Trace P s as t ↔ t = t₀ :=
  ⟨fun tr => Option.some.inj ((run_iff.mpr tr).symm.trans h),
   fun e => run_iff.mp (Eq.subst (motive := fun x => ReferencePlan.run s as = some x) e.symm h)⟩

/-- Where an act executes to `t₀`, its step ends exactly at `t₀`. -/
theorem step_iff_of_execute {s t₀ t : State} {a : Act} (h : execute s a = some t₀) :
    P.step s a t ↔ t = t₀ :=
  ⟨fun st => Option.some.inj (st.symm.trans h),
   fun e => Eq.subst (motive := fun x => P.step s a x) e.symm h⟩

/-- An option mapped to `some v` holds a value mapped to `v`. -/
theorem map_some {α β : Type} {o : Option α} {f : α → β} {v : β} (h : o.map f = some v) :
    ∃ x, o = some x ∧ f x = v :=
  match o, h with
  | some x, h => ⟨x, rfl, Option.some.inj h⟩
  | none, h => nomatch h

/-- A reading of the outcome of an operation that ignores fuel holds of every step by the act. -/
theorem step_reads {β : Type} {s t : State} {a : Act} {f : State → β} {v : β}
    (blind : ∀ u : State, f { u with fuel := s.fuel - use a, used := s.used + use a } = f u)
    (h : (operate s a).map f = some v) (st : P.step s a t) : f t = v :=
  match step_iff.mp st with
  | ⟨_, u, op, et⟩ =>
    (congrArg f et).trans ((blind u).trans
      (Option.some.inj ((congrArg (Option.map f) op).symm.trans h)))

/-- The repair policy read as a process: a step is the act `choose` picks, executed. -/
def chosen : Process State Act := ⟨fun s a t => choose s = some a ∧ P.step s a t⟩

theorem repair_of_trace {s t : State} {as : List Act} (h : Trace chosen s as t) :
    repair as.length s = some t := by
  induction h with
  | nil => rfl
  | @cons s m t a as step _ ih =>
    change (match choose s with
      | none => none
      | some a => (execute s a).bind (repair as.length)) = some t
    rw [step.1]
    change (execute s a).bind (repair as.length) = some t
    rw [step.2]
    exact ih

theorem trace_of_repair : ∀ {n : Nat} {s t : State}, repair n s = some t →
    ∃ as, as.length = n ∧ Trace chosen s as t
  | 0, s, _, h => ⟨[], rfl, Eq.subst (motive := fun x => Trace chosen s [] x) (Option.some.inj h)
      (Trace.nil s)⟩
  | n + 1, s, t, h => by
    change (match choose s with
      | none => none
      | some a => (execute s a).bind (repair n)) = some t at h
    cases ch : choose s with
    | none => rw [ch] at h; contradiction
    | some a =>
      rw [ch] at h
      change (execute s a).bind (repair n) = some t at h
      cases ex : execute s a with
      | none => rw [ex] at h; contradiction
      | some m =>
        rw [ex] at h
        match trace_of_repair h with
        | ⟨as, len, path⟩ => exact ⟨a :: as, congrArg (· + 1) len, Trace.cons ⟨ch, ex⟩ path⟩

/-- **The source's repairs of `n` steps are exactly the traces of length `n` of the policy's
process.** -/
theorem repair_iff {n : Nat} {s t : State} :
    repair n s = some t ↔ ∃ as, as.length = n ∧ Trace chosen s as t :=
  ⟨trace_of_repair, fun ⟨_, len, path⟩ =>
    Eq.subst (motive := fun k => repair k s = some t) len (repair_of_trace path)⟩

/-- Where a repair of `n` steps reaches `t₀`, the policy's traces of length `n` end exactly
there. -/
theorem repairs_iff_of_repair {n : Nat} {s t₀ t : State} (h : repair n s = some t₀) :
    (∃ as, as.length = n ∧ Trace chosen s as t) ↔ t = t₀ :=
  ⟨fun path => Option.some.inj ((repair_iff.mpr path).symm.trans h),
   fun e => repair_iff.mp (Eq.subst (motive := fun x => repair n s = some x) e.symm h)⟩

/-- Where a repair of `n` steps has no outcome, the policy's process has no trace of length `n`. -/
theorem no_repair_of {n : Nat} {s : State} (h : repair n s = none) :
    ¬ ∃ as t, as.length = n ∧ Trace chosen s as t :=
  fun ⟨as, _, len, path⟩ => nomatch h.symm.trans (repair_iff.mpr ⟨as, len, path⟩)

/-! ## Laws of the steps -/

/-- **Every revise step from a configuration holding the failed address `i` puts `i` at the head
of the method and of the next plan, leaving the installed device in place.** -/
theorem revise_binds_plan {s t : State} {i : Nat} (h : s.mismatch = some i)
    (st : P.step s .revise t) :
    (t.method, t.pending, t.installed) = (i :: s.method, i :: s.method, s.installed) :=
  step_reads (fun _ => rfl) (revision_binds_plan s i h) st

/-- **A revise step answers the mismatch held**: there is one, and its address heads the new
method. -/
theorem revise_step {s t : State} (st : P.step s .revise t) :
    ∃ i, s.mismatch = some i ∧ t.method = i :: s.method := by
  cases hm : s.mismatch with
  | none =>
    match step_iff.mp st with
    | ⟨_, _, op, _⟩ =>
      unfold operate at op
      rw [hm] at op
      contradiction
  | some i => exact ⟨i, rfl, congrArg Prod.fst (revise_binds_plan hm st)⟩

/-- **A revise step's method contacts the failed address it answers.** -/
theorem revise_registers {s t : State} {i : Nat} (h : s.mismatch = some i)
    (st : P.step s .revise t) :
    Learning.Training.Through (ReferencePlan.AgreeOn t.method) (fun x => x i = true) :=
  Eq.subst (motive := fun m => Learning.Training.Through (ReferencePlan.AgreeOn m) (fun x => x i = true))
    ((congrArg Prod.fst (revise_binds_plan h st)).trans (propose_from_mismatch s.method i).symm).symm
    (revise_registers_failure s.method i)

/-- **A revise step keeps every selection the old method made.** -/
theorem revise_keeps_selections {s t : State} (st : P.step s .revise t) :
    ∀ select, Learning.Training.Through (ReferencePlan.AgreeOn s.method) select →
      Learning.Training.Through (ReferencePlan.AgreeOn t.method) select :=
  match revise_step st with
  | ⟨i, _, method⟩ =>
    Eq.subst (motive := fun m => ∀ select, Learning.Training.Through (ReferencePlan.AgreeOn s.method) select →
        Learning.Training.Through (ReferencePlan.AgreeOn m) select)
      method.symm (old_selections_remain s.method i)

/-- **A revise step keeps every distinction of the old method.** -/
theorem revise_keeps {s t : State} (st : P.step s .revise t) :
    Registration.Keeps ReferencePlan.AgreeOn s.method t.method :=
  match revise_step st with
  | ⟨i, _, method⟩ =>
    Eq.subst (motive := fun m => Registration.Keeps ReferencePlan.AgreeOn s.method m) method.symm
      (added_keeps s.method i)

/-- **A revise step answering a failure at an address the method lacked gains the choice at that
contact**, which the old method could not make. -/
theorem revise_gains_contact {s t : State} {i : Nat} (h : s.mismatch = some i) (absent : i ∉ s.method)
    (st : P.step s .revise t) :
    Learning.Training.Through (ReferencePlan.AgreeOn t.method) (fun x => x i = true) ∧
      ¬ Learning.Training.Through (ReferencePlan.AgreeOn s.method) (fun x => x i = true) :=
  Eq.subst (motive := fun m => Learning.Training.Through (ReferencePlan.AgreeOn m) (fun x => x i = true) ∧
      ¬ Learning.Training.Through (ReferencePlan.AgreeOn s.method) (fun x => x i = true))
    (congrArg Prod.fst (revise_binds_plan h st)).symm (new_contact_choice s.method i absent)

/-- **A probe step, while building, acquires both references of the next planned contact.** -/
theorem probe_binds {s t : State} {i : Nat} {tail : List Nat} (active : s.building = true)
    (head : s.pending = i :: tail) (st : P.step s .probe t) :
    (t.pending, t.fresh) = (tail, ⟨i, s.channel i false, s.channel i true⟩ :: s.fresh) :=
  step_reads (fun _ => rfl) (probe_binds_both_references s i tail active head) st

/-- **An install step, once every planned contact is probed and every pair is checked, binds the
fresh pairs and ends building.** -/
theorem install_binds {s t : State} (active : s.building = true) (done : s.pending = [])
    (checked : valid s.fresh = true) (st : P.step s .install t) :
    (t.installed, t.building) = (s.fresh, false) :=
  step_reads (fun _ => rfl) (install_binds_fresh s active done checked) st

/-- **A frozen step's plan is the retained method, whatever failed.** -/
theorem frozen_plan {s t : State} (st : P.step s .frozen t) :
    t.pending = frozenRule s.method s.mismatch :=
  step_reads (fun _ => rfl) (frozen_reads_method s) st

/-- **At every retained method some failure is left unanswered by every frozen step.** -/
theorem frozen_leaves_unregistered (s : State) :
    ∃ i, ∀ t, P.step { s with mismatch := some i } .frozen t →
      ¬ Learning.Training.Through (ReferencePlan.AgreeOn t.pending) (fun x => x i = true) :=
  match frozen_misses s.method with
  | ⟨i, miss⟩ => ⟨i, fun _ st =>
      Eq.subst (motive := fun m => ¬ Learning.Training.Through (ReferencePlan.AgreeOn m) (fun x => x i = true))
        (frozen_plan st).symm miss⟩

/-- **A perform step answers through the installed key.** -/
theorem perform_response {s t : State} {i : Nat} {target : Bool}
    (st : P.step s (.perform i target) t) :
    t.response = s.channel i (ReferencePlan.flip (keyAt s.installed i) target) := by
  match step_iff.mp st with
  | ⟨_, u, op, et⟩ =>
    subst et
    unfold operate at op
    cases hb : s.building with
    | true => rw [hb] at op; contradiction
    | false =>
      rw [hb] at op
      exact congrArg State.response (Option.some.inj op).symm

/-- A perform step is enabled where the configuration is not building and holds fuel. -/
theorem perform_enabled {s : State} {i : Nat} {target : Bool} (ready : s.building = false)
    (enough : 1 ≤ s.fuel) : Enabled P s (.perform i target) :=
  enabled_iff.mpr ⟨enough, _, by unfold operate; rw [ready]; rfl⟩

/-- **A key read off the low reference drives the contact to every target exactly where the two
references differ**, at a configuration ready to perform. -/
theorem checked_drives {s : State} {i : Nat} (key : keyAt s.installed i = s.channel i false)
    (ready : s.building = false) (enough : 1 ≤ s.fuel) :
    (∀ target t, P.step s (.perform i target) t → t.response = target) ↔
      s.channel i false ≠ s.channel i true :=
  have answers : ∀ {target t}, P.step s (.perform i target) t →
      t.response = s.channel i (ReferencePlan.flip (s.channel i false) target) :=
    fun st => Eq.subst (motive := fun k => _ = s.channel i (ReferencePlan.flip k _)) key
      (perform_response st)
  ⟨fun meets => (checked_pair_iff (s.channel i)).mp fun target =>
      match perform_enabled (target := target) ready enough with
      | ⟨t, st⟩ => (answers st).symm.trans (meets target t st),
   fun separate target _ st => (answers st).trans (checked_pair_correct (s.channel i) separate target)⟩

/-- A drift step inverts the channel and keeps the installed device. -/
theorem drift_step {s t : State} (st : P.step s .drift t) :
    t.channel = (fun i b => !(s.channel i b)) ∧ t.installed = s.installed :=
  match step_iff.mp st with
  | ⟨_, u, op, et⟩ =>
    have e : { s with channel := fun i b => !(s.channel i b) } = u := Option.some.inj op
    ⟨(congrArg State.channel et).trans (congrArg State.channel e).symm,
     (congrArg State.installed et).trans (congrArg State.installed e).symm⟩

/-- **After a drift step, a key checked against separated references misses every target.** -/
theorem drift_misses {s t u : State} {i : Nat} (key : keyAt s.installed i = s.channel i false)
    (separate : s.channel i false ≠ s.channel i true) (drift : P.step s .drift t) (target : Bool)
    (st : P.step t (.perform i target) u) : u.response ≠ target := by
  have r := perform_response st
  rw [(drift_step drift).2, key, (drift_step drift).1] at r
  exact fun same => drift_fails (s.channel i) separate target (r.symm.trans same)

/-! ## The native history as traces -/

/-- The first round of the native history: a failed use and the policy's repair. -/
def firstRound : List Act := [.perform 0 true, .revise, .probe, .install]

/-- The second round: the repaired contact used, a failure at a new address, and the repair. -/
def secondRound : List Act := [.perform 0 true, .perform 1 true, .revise, .probe, .probe, .install]

/-- The last uses of both revised contacts. -/
def lastUses : List Act := [.perform 1 true, .perform 0 true]

/-- The native history is its two rounds and the last uses. -/
theorem actualWord_rounds : actualWord = firstRound ++ secondRound ++ lastUses := rfl

/-- **The native history passes through its rounds**: a trace of it is exactly a first round, a
second round from where that ends, and the last uses from there. -/
theorem history_rounds {t : State} :
    Trace P initial actualWord t ↔
      ∃ m₁ m₂, Trace P initial firstRound m₁ ∧ Trace P m₁ secondRound m₂ ∧ Trace P m₂ lastUses t :=
  Eq.subst (motive := fun w => Trace P initial w t ↔
      ∃ m₁ m₂, Trace P initial firstRound m₁ ∧ Trace P m₁ secondRound m₂ ∧ Trace P m₂ lastUses t)
    actualWord_rounds.symm
    (trace_append_iff.trans
      ⟨fun ⟨m₂, front, last⟩ => match trace_append_iff.mp front with
        | ⟨m₁, first, second⟩ => ⟨m₁, m₂, first, second, last⟩,
       fun ⟨m₁, m₂, first, second, last⟩ => ⟨m₂, trace_append_iff.mpr ⟨m₁, first, second⟩, last⟩⟩)

/-- The first round ends exactly at the first repair. -/
theorem firstRound_trace {t : State} : Trace P initial firstRound t ↔ t = repairedFirst :=
  trace_iff_of_run rfl

/-- The second round ends exactly at the second repair. -/
theorem secondRound_trace {t : State} : Trace P repairedFirst secondRound t ↔ t = repairedSecond :=
  trace_iff_of_run rfl

/-- **The first use fails**: the step performing at the empty method ends exactly at the
configuration holding the mismatch at address 0. -/
theorem first_mismatch_step {t : State} :
    P.step initial (.perform 0 true) t ↔ t = failedFirst :=
  step_iff_of_execute first_mismatch_acquired

/-- **The policy repairs the first failure in three steps**, ending exactly at the first repair. -/
theorem first_repair {t : State} :
    (∃ as, as.length = 3 ∧ Trace chosen failedFirst as t) ↔ t = repairedFirst :=
  repairs_iff_of_repair first_policy_repair

/-- **The policy repairs the second failure in four steps**, ending exactly at the second repair. -/
theorem second_repair {t : State} :
    (∃ as, as.length = 4 ∧ Trace chosen failedSecond as t) ↔ t = repairedSecond :=
  repairs_iff_of_repair second_policy_repair

/-- **After the first repair, the repaired contact is used and a new address fails.** -/
theorem second_mismatch_trace {t : State} :
    Trace P repairedFirst [.perform 0 true, .perform 1 true] t ↔ t = failedSecond :=
  trace_iff_of_run first_repair_used_then_second_mismatch

/-- **After the second repair, both revised contacts are used**, ending exactly at the finished
configuration. -/
theorem finished_trace {t : State} :
    Trace P repairedSecond [.perform 1 true, .perform 0 true] t ↔ t = finished :=
  trace_iff_of_run both_revised_contacts_used

/-- **The repaired contact meets its target after the first repair.** -/
theorem first_use_meets : ∃ t, P.step repairedFirst (.perform 0 true) t ∧ t.response = true :=
  match map_some first_use_succeeds with
  | ⟨t, st, response⟩ => ⟨t, st, response⟩

/-- **The newly repaired contact meets its target after the second repair.** -/
theorem second_use_meets : ∃ t, P.step repairedSecond (.perform 1 true) t ∧ t.response = true :=
  match map_some second_use_succeeds with
  | ⟨t, st, response⟩ => ⟨t, st, response⟩

/-- **Along the native history the method changes at each round**: empty at the start, the first
failed address after the first round, both after the second. -/
theorem rounds_change_method {t₁ t₂ : State} (first : Trace P initial firstRound t₁)
    (second : Trace P t₁ secondRound t₂) :
    initial.method = [] ∧ t₁.method = [0] ∧ t₂.method = [1, 0] := by
  have e₁ := firstRound_trace.mp first
  subst e₁
  have e₂ := secondRound_trace.mp second
  subst e₂
  exact methods_change_twice

/-- **The first round installs the contact at address 0**, which neither the installed device nor
the method held at the start. -/
theorem first_round_installs_contact {t : State} (first : Trace P initial firstRound t) :
    keyAt initial.installed 0 = false ∧ keyAt t.installed 0 = true ∧
      0 ∉ initial.method ∧ 0 ∈ t.method := by
  have e := firstRound_trace.mp first
  subst e
  exact first_candidate_unavailable_before

/-- **The first round gains the choice at contact 0 through the installed contacts**, which the
start did not have. -/
theorem first_round_registers {t : State} (first : Trace P initial firstRound t) :
    Learning.Training.Through (alikeOnInstalled t) (fun x => x 0 = true) ∧
      ¬ Learning.Training.Through (alikeOnInstalled initial) (fun x => x 0 = true) := by
  have e := firstRound_trace.mp first
  subst e
  exact first_installed_choice

/-- **The second round gains the choice at contact 1 through the installed contacts**, which the
first repair did not have. -/
theorem second_round_registers {t : State} (second : Trace P repairedFirst secondRound t) :
    Learning.Training.Through (alikeOnInstalled t) (fun x => x 1 = true) ∧
      ¬ Learning.Training.Through (alikeOnInstalled repairedFirst) (fun x => x 1 = true) := by
  have e := secondRound_trace.mp second
  subst e
  exact second_installed_choice

/-- **After the first round, every use of contact 0 meets its target.** -/
theorem first_round_meets {t u : State} {target : Bool} (first : Trace P initial firstRound t)
    (st : P.step t (.perform 0 target) u) : u.response = target := by
  have e := firstRound_trace.mp first
  subst e
  exact (perform_response st).trans (installed_response_correct target).1

/-- **After the second round, every use of contacts 0 and 1 meets its target.** -/
theorem second_round_meets {t u : State} {target : Bool}
    (second : Trace P repairedFirst secondRound t) :
    (P.step t (.perform 0 target) u → u.response = target) ∧
      (P.step t (.perform 1 target) u → u.response = target) := by
  have e := secondRound_trace.mp second
  subst e
  exact ⟨fun st => (perform_response st).trans (installed_response_correct target).2.1,
    fun st => (perform_response st).trans (installed_response_correct target).2.2⟩

/-- **The native history ends with half its fuel used and none restored.** -/
theorem history_uses_fuel {t : State} (h : Trace P initial actualWord t) :
    t.fuel = 15 ∧ t.used = 15 :=
  Eq.subst (motive := fun x : State => x.fuel = 15 ∧ x.used = 15)
    (trace_unique complete_history h) fuel_used_without_reset

/-! ## The controls as traces -/

/-- **The frozen control runs and still fails**: re-running the retained method installs nothing
and misses the target. -/
theorem frozen_control_fails :
    ∃ t, Trace P failedFirst [.frozen, .install, .perform 0 true] t ∧
      t.response = false ∧ t.installed = [] :=
  match frozen_method_still_fails with
  | ⟨h, response, installed⟩ => ⟨frozenEnd, run_iff.mp h, response, installed⟩

/-- **The second frozen control runs, keeps the first repair and still misses the new address.** -/
theorem frozen_second_control_fails :
    ∃ t, Trace P failedSecond [.frozen, .probe, .install, .perform 1 true] t ∧
      t.response = false ∧ keyAt t.installed 0 = true ∧ keyAt t.installed 1 = false :=
  match frozen_second_method_still_fails with
  | ⟨h, response, kept, missing⟩ => ⟨frozenSecondEnd, run_iff.mp h, response, kept, missing⟩

/-- **A drift after a checked repair runs into a mismatch at the repaired contact.** -/
theorem drift_control_fails :
    ∃ t, Trace P repairedFirst [.drift, .perform 0 true] t ∧
      (t.response, t.mismatch, t.fuel, t.used) = (false, some 0, 23, 7) :=
  match map_some drift_after_check_can_fail with
  | ⟨t, h, read⟩ => ⟨t, run_iff.mp h, read⟩

/-- **After the mismatch is erased, the policy has no step.** -/
theorem erased_no_repair {t : State} (erase : P.step failedFirst .erase t) :
    ¬ ∃ a u, chosen.step t a u :=
  fun ⟨a, u, st⟩ =>
    have none : repair 1 t = none :=
      Eq.subst (motive := fun o => o.bind (repair 1) = none) erase erased_mismatch_cannot_activate
    nomatch none.symm.trans (repair_iff.mpr ⟨[a], rfl, Trace.cons st (Trace.nil u)⟩)

/-- **With too little fuel the policy cannot complete the first repair.** -/
theorem small_support_no_repair :
    ¬ ∃ as t, as.length = 3 ∧ Trace chosen { failedFirst with fuel := 3 } as t :=
  no_repair_of support_too_small_to_build

/-- **With too little fuel the policy's contacts still use all of it**, and nothing is installed. -/
theorem small_support_uses_fuel :
    ∃ t, (∃ as, as.length = 2 ∧ Trace chosen { failedFirst with fuel := 3 } as t) ∧
      (t.fuel, t.used, t.installed) = (0, 4, []) :=
  match map_some references_use_fuel_before_exhaustion with
  | ⟨t, h, read⟩ => ⟨t, repair_iff.mp h, read⟩

/-- **With a constant channel the policy cannot complete the repair**: the separation check
fails. -/
theorem constant_channel_no_repair :
    ¬ ∃ as t, as.length = 3 ∧ Trace chosen { failedFirst with channel := fun _ _ => false } as t :=
  no_repair_of constant_channel_rejected

/-- **With a constant channel the policy's contacts still use fuel**, the fresh pair fails the
check, and nothing is installed. -/
theorem constant_channel_uses_fuel :
    ∃ t, (∃ as, as.length = 2 ∧ Trace chosen { failedFirst with channel := fun _ _ => false } as t) ∧
      (t.fuel, t.used, valid t.fresh, t.installed) = (26, 4, false, []) :=
  match map_some constant_channel_contacts_use_fuel with
  | ⟨t, h, read⟩ => ⟨t, repair_iff.mp h, read⟩

/-- **With no fuel no use is enabled.** -/
theorem exhausted_not_enabled : ¬ Enabled P { repairedFirst with fuel := 0 } (.perform 0 true) :=
  fun ⟨_, st⟩ => nomatch no_action_after_exhaustion.symm.trans st

end ReferencePlanTraces

end Becoming
