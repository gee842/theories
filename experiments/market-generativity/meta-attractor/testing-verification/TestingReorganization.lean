import AdmissionRevision

/-! Dependency-aware revision of testing. Three readers depend on represented
causal roots. A completed physical inspection is assumed to disclose its actual
root. At most one root may deviate in a transaction. This is not a discovery
theorem for all common causes, or a consensus protocol. -/
namespace TestingReorganization
open ReproductionNetwork
set_option autoImplicit false

def triple (a b c : Nat) (i : Fin 3) : Nat := if i = 0 then a else if i = 1 then b else c

def put {α : Type} (f : Fin 3 → α) (i : Fin 3) (v : α) : Fin 3 → α :=
  fun j => if j = i then v else f j

def Diverse (r : Fin 3 → Nat) : Prop := r 0 ≠ r 1 ∧ r 0 ≠ r 2 ∧ r 1 ≠ r 2
instance decidableDiverse (r : Fin 3 → Nat) : Decidable (Diverse r) := inferInstanceAs (Decidable (_ ∧ _ ∧ _))

def Agrees (reports : Fin 3 → Option Bool) (v : Bool) : Prop :=
  (reports 0 = some v ∧ reports 1 = some v) ∨
  (reports 0 = some v ∧ reports 2 = some v) ∨
  (reports 1 = some v ∧ reports 2 = some v)
instance decidableAgreement (reports : Fin 3 → Option Bool) (v : Bool) : Decidable (Agrees reports v) :=
  inferInstanceAs (Decidable ((_ ∧ _) ∨ (_ ∧ _) ∨ (_ ∧ _)))

theorem agreement_sound (r : Fin 3 → Nat) (reports : Fin 3 → Option Bool)
    (actual v : Bool) (badRoot : Nat) (hd : Diverse r)
    (honest : ∀ i, r i ≠ badRoot → reports i = some v → v = actual)
    (accept : Agrees reports v) : v = actual := by
  rcases accept with h | h | h
  · by_cases h0 : r 0 = badRoot
    · exact honest 1 (by intro h1; exact hd.1 (h0.trans h1.symm)) h.2
    · exact honest 0 h0 h.1
  · by_cases h0 : r 0 = badRoot
    · exact honest 2 (by intro h2; exact hd.2.1 (h0.trans h2.symm)) h.2
    · exact honest 0 h0 h.1
  · by_cases h1 : r 1 = badRoot
    · exact honest 2 (by intro h2; exact hd.2.2 (h1.trans h2.symm)) h.2
    · exact honest 1 h1 h.1

theorem agreement_available (r : Fin 3 → Nat) (reports : Fin 3 → Option Bool)
    (actual : Bool) (badRoot : Nat) (hd : Diverse r)
    (respond : ∀ i, r i ≠ badRoot → reports i = some actual) : Agrees reports actual := by
  by_cases h0 : r 0 = badRoot
  · exact Or.inr (Or.inr ⟨respond 1 (by intro h1; exact hd.1 (h0.trans h1.symm)),
      respond 2 (by intro h2; exact hd.2.1 (h0.trans h2.symm))⟩)
  · by_cases h1 : r 1 = badRoot
    · exact Or.inr (Or.inl ⟨respond 0 h0,respond 2 (by intro h2; exact hd.2.2 (h1.trans h2.symm))⟩)
    · exact Or.inl ⟨respond 0 h0,respond 1 h1⟩

structure Stage where
  root : Nat
  reading : Option Nat

structure State where
  plant : Installation
  roots : Fin 3 → Nat
  seen : Fin 3 → Option Nat
  staged : Option Stage
  revision : Nat

def Complete (s : State) : Prop := ∀ i, (s.seen i).isSome = true
instance decidableComplete (s : State) : Decidable (Complete s) :=
  inferInstanceAs (Decidable (∀ i, (s.seen i).isSome = true))
def decoded (s : State) : Fin 3 → Nat := fun i => (s.seen i).getD 0
def Knowledge (s : State) : Prop :=
  (∀ i v, s.seen i = some v → s.roots i = v) ∧
  (∀ st, s.staged = some st → ∀ v, st.reading = some v → st.root = v)
def Supported (s : State) : Prop := Equipped s.plant ∧ Established s.plant
def Invariant (s : State) : Prop := Supported s ∧ Knowledge s ∧ Diverse s.roots

def charge (s : State) (n : Nat) : State :=
  {s with plant := {s.plant with body := {s.plant.body with material := s.plant.body.material-n}}}

def inspected (s : State) (i : Fin 3) : State :=
  {charge s 1 with seen := put s.seen i (some (s.roots i))}
def built (s : State) (root : Nat) : State :=
  {charge s 2 with staged := some ⟨root,none⟩}
def tested (s : State) (st : Stage) : State :=
  {charge s 1 with staged := some ⟨st.root,some st.root⟩}
def switched (s : State) (i : Fin 3) (st : Stage) : State :=
  {charge s 1 with
    roots := put s.roots i st.root
    seen := put s.seen i st.reading
    staged := none
    revision := s.revision+1}
def worked (s : State) : State := {s with plant := cycle s.plant .separate}

inductive Event where
  | inspect : Fin 3 → Event
  | build : Nat → Event
  | test
  | switch : Fin 3 → Event
  | work

def process : Generative.Process State Event where
  step s event t := Supported s ∧ match event with
    | .inspect i => 12 ≤ s.plant.body.material ∧ t = inspected s i
    | .build root => 13 ≤ s.plant.body.material ∧ t = built s root
    | .test => ∃ st, s.staged = some st ∧ 12 ≤ s.plant.body.material ∧ t = tested s st
    | .switch i => ∃ st v, s.staged = some st ∧ st.reading = some v ∧ Complete s ∧
        Diverse (put (decoded s) i v) ∧ 12 ≤ s.plant.body.material ∧ t = switched s i st
    | .work => t = worked s

theorem complete_decodes_actual (s : State) (hk : Knowledge s) (hc : Complete s) :
    decoded s = s.roots := by
  funext i
  have hh := hc i
  cases he : s.seen i with
  | none => simp [he] at hh
  | some v => simpa [decoded,he] using (hk.1 i v he).symm

theorem charge_supported (s : State) (n : Nat) (hs : Supported s)
    (hm : 11+n ≤ s.plant.body.material) : Supported (charge s n) := by
  refine ⟨⟨hs.1.1,?_⟩,hs.2⟩
  change 11 ≤ s.plant.body.material-n
  omega

theorem work_supported (s : State) (hs : Supported s) : Supported (worked s) :=
  ⟨cycle_equipped _ _ hs.1,cycle_established _ _ hs.2 (by decide)⟩

theorem inspection_preserves_knowledge (s : State) (i : Fin 3) (hk : Knowledge s) :
    Knowledge (inspected s i) := by
  refine ⟨?_,hk.2⟩
  intro j v h
  by_cases he : j = i
  · subst j
    simpa [inspected,put] using h
  · exact hk.1 j v (by simpa [inspected,put,he] using h)

theorem build_preserves_knowledge (s : State) (root : Nat) (hk : Knowledge s) :
    Knowledge (built s root) := by
  refine ⟨hk.1,?_⟩
  intro st h v hv
  have he : (⟨root,none⟩ : Stage) = st := Option.some.inj h
  subst st
  contradiction

theorem test_preserves_knowledge (s : State) (st : Stage) (hk : Knowledge s) :
    Knowledge (tested s st) := by
  refine ⟨hk.1,?_⟩
  intro u h v hv
  have he : (⟨st.root,some st.root⟩ : Stage) = u := Option.some.inj h
  subst u
  exact Option.some.inj hv

theorem switch_preserves_knowledge (s : State) (i : Fin 3) (st : Stage)
    (hk : Knowledge s) (hstage : s.staged = some st) : Knowledge (switched s i st) := by
  constructor
  · intro j v h
    by_cases he : j = i
    · subst j
      simpa [switched,put] using hk.2 st hstage v (by simpa [switched,put] using h)
    · simpa [switched,put,he] using hk.1 j v (by simpa [switched,put,he] using h)
  · intro u h
    contradiction

theorem switch_preserves_diversity (s : State) (i : Fin 3) (st : Stage) (v : Nat)
    (hk : Knowledge s) (hc : Complete s) (ht : s.staged = some st)
    (hv : st.reading = some v) (hd : Diverse (put (decoded s) i v)) :
    Diverse (switched s i st).roots := by
  have he := hk.2 st ht v hv
  simpa [switched,complete_decodes_actual s hk hc,he] using hd

theorem step_preserves (s t : State) (event : Event)
    (hs : Invariant s) (step : process.step s event t) : Invariant t := by
  rcases hs with ⟨support,known,diverse⟩
  cases event with
  | inspect i =>
    obtain ⟨_,hm,rfl⟩ := step
    exact ⟨charge_supported s 1 support hm,inspection_preserves_knowledge s i known,diverse⟩
  | build root =>
    obtain ⟨_,hm,rfl⟩ := step
    exact ⟨charge_supported s 2 support hm,build_preserves_knowledge s root known,diverse⟩
  | test =>
    obtain ⟨_,st,_,hm,rfl⟩ := step
    exact ⟨charge_supported s 1 support hm,test_preserves_knowledge s st known,diverse⟩
  | switch i =>
    obtain ⟨_,st,v,ht,hv,hc,hd,hm,rfl⟩ := step
    exact ⟨charge_supported s 1 support hm,switch_preserves_knowledge s i st known ht,
      switch_preserves_diversity s i st v known hc ht hv hd⟩
  | work =>
    obtain ⟨_,rfl⟩ := step
    exact ⟨work_supported s support,known,diverse⟩

theorem trace_preserves (s t : State) (events : List Event)
    (hs : Invariant s) (trace : Generative.Trace process s events t) : Invariant t := by
  induction trace with
  | nil => exact hs
  | cons step _ ih => exact ih (step_preserves _ _ _ hs step)

theorem switch_keeps_complete (s : State) (i : Fin 3) (st : Stage) (v : Nat)
    (hc : Complete s) (hr : st.reading = some v) : Complete (switched s i st) := by
  intro j
  by_cases he : j = i
  · simp [switched,put,he,hr]
  · simpa [switched,put,he] using hc j

theorem step_keeps_complete (s t : State) (event : Event)
    (hc : Complete s) (step : process.step s event t) : Complete t := by
  cases event with
  | inspect i =>
    obtain ⟨_,_,rfl⟩ := step
    intro j
    by_cases he : j = i
    · simp [inspected,put,he]
    · simpa [inspected,put,he] using hc j
  | build root => obtain ⟨_,_,rfl⟩ := step; exact hc
  | test => obtain ⟨_,st,_,_,rfl⟩ := step; exact hc
  | switch i =>
    obtain ⟨_,st,v,_,hv,_,_,_,rfl⟩ := step
    exact switch_keeps_complete s i st v hc hv
  | work => obtain ⟨_,rfl⟩ := step; exact hc

theorem complete_through_trace (s t : State) (events : List Event)
    (hc : Complete s) (trace : Generative.Trace process s events t) : Complete t := by
  induction trace with
  | nil => exact hc
  | cons step _ ih => exact ih (step_keeps_complete _ _ _ hc step)

def accepted (s : State) (reports : Fin 3 → Option Bool) (v : Bool) : Prop :=
  Complete s ∧ Diverse (decoded s) ∧ Agrees reports v

theorem accepted_after_revision_is_sound (s t : State) (events : List Event)
    (hs : Invariant s) (trace : Generative.Trace process s events t)
    (reports : Fin 3 → Option Bool) (actual v : Bool) (badRoot : Nat)
    (honest : ∀ i, t.roots i ≠ badRoot → reports i = some v → v = actual)
    (ha : accepted t reports v) : v = actual :=
  agreement_sound t.roots reports actual v badRoot (trace_preserves _ _ _ hs trace).2.2 honest ha.2.2

theorem checking_available_after_revision (s t : State) (events : List Event)
    (hs : Invariant s) (hc : Complete s) (trace : Generative.Trace process s events t)
    (reports : Fin 3 → Option Bool) (actual : Bool) (badRoot : Nat)
    (respond : ∀ i, t.roots i ≠ badRoot → reports i = some actual) : accepted t reports actual := by
  have inv := trace_preserves _ _ _ hs trace
  have comp := complete_through_trace _ _ _ hc trace
  exact ⟨comp,by rw [complete_decodes_actual t inv.2.1 comp]; exact inv.2.2,
    agreement_available t.roots reports actual badRoot inv.2.2 respond⟩

def migrated (s : State) (i : Fin 3) (root : Nat) : State :=
  switched (tested (built s root) ⟨root,none⟩) i ⟨root,some root⟩

theorem migration_completes (s : State) (i : Fin 3) (root : Nat)
    (hs : Invariant s) (hc : Complete s) (hm : 15 ≤ s.plant.body.material)
    (hd : Diverse (put s.roots i root)) :
    Generative.Trace process s [.build root,.test,.switch i] (migrated s i root) := by
  have sb : Supported (built s root) := charge_supported s 2 hs.1 (by omega)
  have st : Supported (tested (built s root) ⟨root,none⟩) :=
    charge_supported (built s root) 1 sb (by change 12 ≤ s.plant.body.material-2; omega)
  refine .cons ⟨hs.1,by omega,rfl⟩ (.cons ⟨sb,_,rfl,?_,rfl⟩
    (.cons ⟨st,_,root,rfl,rfl,hc,?_,?_,rfl⟩ (.nil _)))
  · change 12 ≤ s.plant.body.material-2
    omega
  · change Diverse (put (decoded s) i root)
    rw [complete_decodes_actual s hs.2.1 hc]
    exact hd
  · change 12 ≤ s.plant.body.material-2-1
    omega

theorem migration_accounting (s : State) (i : Fin 3) (root : Nat) :
    (migrated s i root).plant.body.material = s.plant.body.material-4 ∧
    (migrated s i root).roots = put s.roots i root ∧
    (migrated s i root).revision = s.revision+1 := by
  refine ⟨?_,rfl,rfl⟩
  change s.plant.body.material-2-1-1 = s.plant.body.material-4
  omega

theorem work_finances_testing (s : State) (hs : Supported s) :
    s.plant.body.material+2 ≤ (worked s).plant.body.material := by
  have hd := demand_bound (arrangement .separate) s.plant.body.stock
  have hmax : maximumDemand (arrangement .separate) = 8 := by decide
  rw [hmax] at hd
  have hm := hs.1.2
  change s.plant.body.material+2 ≤
    s.plant.body.material-1-demand (arrangement .separate) s.plant.body.stock+11
  omega

theorem two_work_cycles_finance_migration (s : State) (hs : Supported s) :
    15 ≤ (worked (worked s)).plant.body.material := by
  have h1 := work_finances_testing s hs
  have h2 := work_finances_testing (worked s) (work_supported s hs)
  have h0 := hs.1.2
  omega

theorem work_refines_physical (s : State) (hs : Supported s) :
    Generative.Trace changingProcess s.plant [.revise .separate,.operate allotment] (worked s).plant :=
  cycle_is_executable s.plant .separate hs.1

def initial : State := ⟨warmStart,triple 0 1 2,fun _ => none,none,0⟩
def endowed : State := worked (worked (worked (worked initial)))
def surveyed : State := inspected (inspected (inspected endowed 0) 1) 2

theorem initial_invariant : Invariant initial := by
  refine ⟨warm_start_supported,?_,by decide⟩
  constructor
  · intro i v h
    contradiction
  · intro st h
    contradiction

theorem funded_initial_survey :
    Generative.Trace process initial [.work,.work,.work,.work,.inspect 0,.inspect 1,.inspect 2] surveyed := by
  refine .cons (m := worked initial) ?_
    (.cons (m := worked (worked initial)) ?_
    (.cons (m := worked (worked (worked initial))) ?_
    (.cons (m := endowed) ?_
    (.cons (m := inspected endowed 0) ?_
    (.cons (m := inspected (inspected endowed 0) 1) ?_
    (.cons (m := surveyed) ?_ (.nil _)))))))
  all_goals
    constructor
    · unfold Supported Equipped Established
      decide
    · first | rfl | exact ⟨by decide,rfl⟩

theorem surveyed_ready : Invariant surveyed ∧ Complete surveyed ∧ surveyed.plant.body.material = 16 := by
  refine ⟨trace_preserves _ _ _ initial_invariant funded_initial_survey,?_,by decide⟩
  decide

theorem replacing_a_dependency_is_actual :
    Generative.Trace process surveyed [.build 3,.test,.switch 0] (migrated surveyed 0 3) ∧
    (migrated surveyed 0 3).roots = triple 3 1 2 ∧
    (migrated surveyed 0 3).plant.body.material = 12 := by
  refine ⟨migration_completes _ _ _ surveyed_ready.1 surveyed_ready.2.1 (by decide) (by decide),?_,by decide⟩
  apply funext
  decide

def mergerTest : State := tested (built surveyed 0) ⟨0,none⟩

theorem common_dependency_merge_refused : ¬Generative.Enabled process mergerTest (.switch 1) := by
  rintro ⟨t,_,st,v,ht,hv,_,hd,_,_⟩
  have he : st = ⟨0,some 0⟩ := (Option.some.inj ht).symm
  subst st
  have he : v = 0 := (Option.some.inj hv).symm
  subst v
  have h : Diverse (triple 0 0 2) := hd
  exact h.1 rfl

theorem untested_path_refused (s : State) (root : Nat) (i : Fin 3) :
    ¬Generative.Enabled process (built s root) (.switch i) := by
  rintro ⟨t,_,st,v,ht,hv,_⟩
  have he : st = ⟨root,none⟩ := (Option.some.inj ht).symm
  subst st
  contradiction

def corruptedReports (r : Fin 3 → Nat) (bad : Nat) (actual : Bool) : Fin 3 → Option Bool :=
  fun i => some (if r i = bad then !actual else actual)

theorem merger_can_corrupt_two_readers :
    Agrees (corruptedReports (triple 0 0 2) 0 true) false ∧
    (∀ i, triple 0 0 2 i ≠ 0 → corruptedReports (triple 0 0 2) 0 true i = some true) := by
  constructor
  · decide
  · intro i h
    simp [corruptedReports,h]

theorem present_agreement_can_hide_lost_resilience :
    corruptedReports (triple 0 1 2) 99 true = corruptedReports (triple 0 0 2) 99 true ∧
    Agrees (corruptedReports (triple 0 0 2) 99 true) true ∧
    Agrees (corruptedReports (triple 0 0 2) 0 true) false := by
  refine ⟨?_,by decide,by decide⟩
  apply funext
  decide

def effectiveRoots (alias : Nat → Nat) (r : Fin 3 → Nat) : Fin 3 → Nat := fun i => alias (r i)
def hiddenCommonRoot (r : Fin 3 → Nat) : Fin 3 → Nat := effectiveRoots (fun _ => 0) r

theorem separate_labels_do_not_establish_causal_separation :
    Diverse (triple 0 1 2) ∧ ¬Diverse (hiddenCommonRoot (triple 0 1 2)) ∧
    Agrees (corruptedReports (hiddenCommonRoot (triple 0 1 2)) 0 true) false := by
  decide

def safeWithdrawal (s : State) : Bool := decide (∀ i : Fin 4, 3 ≤ s.plant.body.stock i)
def responseLaw (s : State) (reports : Fin 3 → Option Bool) (bad : Nat) : Prop :=
  ∀ i v, s.roots i ≠ bad → reports i = some v → v = safeWithdrawal s
instance decidableAccepted (s : State) (reports : Fin 3 → Option Bool) (v : Bool) :
    Decidable (accepted s reports v) :=
  inferInstanceAs (Decidable ((∀ i, (s.seen i).isSome = true) ∧ Diverse (decoded s) ∧ _))

def responseChoice (s : State) (reports : Fin 3 → Option Bool) : Arrangement :=
  if accepted s reports true then .broken else .separate
def response (s : State) (reports : Fin 3 → Option Bool) : State :=
  {charge s 3 with plant := cycle (charge s 3).plant (responseChoice s reports)}

theorem certified_response_preserves (s : State) (reports : Fin 3 → Option Bool) (bad : Nat)
    (hs : Invariant s) (hl : responseLaw s reports bad) (hm : 14 ≤ s.plant.body.material) :
    Invariant (response s reports) := by
  have paid := charge_supported s 3 hs.1 hm
  refine ⟨⟨cycle_equipped _ _ paid.1,?_⟩,hs.2⟩
  change Established (cycle (charge s 3).plant (responseChoice s reports))
  unfold responseChoice
  split
  next ha =>
    have hg : safeWithdrawal s = true :=
      (agreement_sound s.roots reports (safeWithdrawal s) true bad hs.2.2 (fun i hi => hl i true hi) ha.2.2).symm
    have floor : ∀ i : Fin 4, 3 ≤ s.plant.body.stock i := by simpa [safeWithdrawal] using hg
    intro i
    rw [AdmissionRevision.broken_stock]
    change 2 ≤ min 3 (s.plant.body.stock i - 1) ∧ min 3 (s.plant.body.stock i - 1) ≤ 3
    have := floor i
    omega
  next => exact cycle_established _ _ paid.2 (by decide)

theorem certified_response_is_physical (s : State) (reports : Fin 3 → Option Bool)
    (hs : Supported s) (hm : 14 ≤ s.plant.body.material) :
    Generative.Trace changingProcess (charge s 3).plant
      [.revise (responseChoice s reports),.operate allotment] (response s reports).plant :=
  cycle_is_executable _ _ (charge_supported s 3 hs hm).1

theorem changed_testing_controls_actual_response :
    responseChoice (worked (migrated surveyed 0 3))
      (corruptedReports (triple 3 1 2) 1 true) = .broken ∧
    (response (worked (migrated surveyed 0 3))
      (corruptedReports (triple 3 1 2) 1 true)).plant.body.stock = four 2 2 2 2 := by
  constructor
  · decide
  · apply funext
    decide

inductive JointEvent where
  | reorganize : Event → JointEvent
  | respond : (Fin 3 → Option Bool) → Nat → JointEvent

def jointProcess : Generative.Process State JointEvent where
  step s event t := match event with
    | .reorganize event => process.step s event t
    | .respond reports bad => Supported s ∧ 14 ≤ s.plant.body.material ∧
        responseLaw s reports bad ∧ t = response s reports

theorem joint_step_preserves (s t : State) (event : JointEvent)
    (hs : Invariant s) (step : jointProcess.step s event t) : Invariant t := by
  cases event with
  | reorganize event => exact step_preserves s t event hs step
  | respond reports bad =>
    obtain ⟨_,hm,hl,rfl⟩ := step
    exact certified_response_preserves s reports bad hs hl hm

theorem joint_history_preserves (s t : State) (events : List JointEvent)
    (hs : Invariant s) (trace : Generative.Trace jointProcess s events t) : Invariant t := by
  induction trace with
  | nil => exact hs
  | cons step _ ih => exact ih (joint_step_preserves _ _ _ hs step)

theorem joint_history_keeps_complete (s t : State) (events : List JointEvent)
    (hc : Complete s) (trace : Generative.Trace jointProcess s events t) : Complete t := by
  induction trace with
  | nil => exact hc
  | @cons _ _ _ event _ step _ ih =>
    apply ih
    cases event with
    | reorganize event => exact step_keeps_complete _ _ event hc step
    | respond reports bad =>
      obtain ⟨_,_,_,rfl⟩ := step
      exact hc

def freshRoot (s : State) : Nat := decoded s 0 + decoded s 1 + decoded s 2 + 1
def renewed (s : State) : State := migrated (worked (worked s)) 0 (freshRoot s)

theorem fresh_root_preserves_diversity (s : State) (hk : Knowledge s)
    (hc : Complete s) (hd : Diverse s.roots) : Diverse (put s.roots 0 (freshRoot s)) := by
  unfold Diverse put freshRoot
  rw [complete_decodes_actual s hk hc]
  simp only [ite_true,show (1 : Fin 3) ≠ 0 by decide,show (2 : Fin 3) ≠ 0 by decide,ite_false]
  constructor
  · omega
  · constructor
    · omega
    · exact hd.2.2

theorem funded_renewal_actual (s : State) (hs : Invariant s) (hc : Complete s) :
    Generative.Trace process s [.work,.work,.build (freshRoot s),.test,.switch 0] (renewed s) := by
  have w1 : process.step s .work (worked s) := ⟨hs.1,rfl⟩
  have inv1 := step_preserves _ _ _ hs w1
  have w2 : process.step (worked s) .work (worked (worked s)) := ⟨inv1.1,rfl⟩
  have inv2 := step_preserves _ _ _ inv1 w2
  exact .cons w1 (.cons w2 (migration_completes _ _ _ inv2 hc
    (two_work_cycles_finance_migration s hs.1) (fresh_root_preserves_diversity s hs.2.1 hc hs.2.2)))

theorem funded_renewal_retains_reserve (s : State) (hs : Supported s) :
    s.plant.body.material ≤ (renewed s).plant.body.material := by
  have h1 := work_finances_testing s hs
  have h2 := work_finances_testing (worked s) (work_supported s hs)
  have ha := (migration_accounting (worked (worked s)) 0 (freshRoot s)).1
  change s.plant.body.material ≤ (migrated (worked (worked s)) 0 (freshRoot s)).plant.body.material
  omega

def renewalHistory (s : State) : Nat → State
  | 0 => s
  | t+1 => renewed (renewalHistory s t)
def renewalEvents (s : State) : Nat → List Event
  | 0 => []
  | t+1 => renewalEvents s t ++ [.work,.work,.build (freshRoot (renewalHistory s t)),.test,.switch 0]

theorem repeated_renewal_supported (s : State) (hs : Invariant s) (hc : Complete s) (n : Nat) :
    Invariant (renewalHistory s n) ∧ Complete (renewalHistory s n) ∧
    Generative.Trace process s (renewalEvents s n) (renewalHistory s n) := by
  induction n with
  | zero => exact ⟨hs,hc,.nil _⟩
  | succ n ih =>
    have tr := funded_renewal_actual (renewalHistory s n) ih.1 ih.2.1
    exact ⟨trace_preserves _ _ _ ih.1 tr,complete_through_trace _ _ _ ih.2.1 tr,
      Generative.trace_append_iff.mpr ⟨_,ih.2.2,tr⟩⟩

theorem initial_to_arbitrarily_many_revisions (n : Nat) :
    Generative.Trace process initial
      ([.work,.work,.work,.work,.inspect 0,.inspect 1,.inspect 2] ++ renewalEvents surveyed n)
      (renewalHistory surveyed n) :=
  Generative.trace_append_iff.mpr ⟨_,funded_initial_survey,
    (repeated_renewal_supported surveyed surveyed_ready.1 surveyed_ready.2.1 n).2.2⟩

def borderline : State := {surveyed with plant := cycle surveyed.plant .broken}
def aliasedReports : Fin 3 → Option Bool :=
  corruptedReports (hiddenCommonRoot borderline.roots) 0 (safeWithdrawal borderline)

theorem unrepresented_common_cause_defeats_response :
    Invariant borderline ∧ accepted borderline aliasedReports true ∧
    (∀ i v, hiddenCommonRoot borderline.roots i ≠ 0 →
      aliasedReports i = some v → v = safeWithdrawal borderline) ∧
    ¬Established (response borderline aliasedReports).plant := by
  refine ⟨?_,by decide,?_,?_⟩
  · refine ⟨?_,surveyed_ready.1.2⟩
    unfold Supported Equipped Established
    decide
  · intro i v h
    exact False.elim (h rfl)
  · intro h
    have hh := (h 0).1
    change 2 ≤ 1 at hh
    omega

end TestingReorganization
