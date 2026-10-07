import GenerativeCore

/-!
# A formed coupling changes jointly effective assembly routes

An optional source lot, loose parts, assembly work, an actual coupling bar,
partial assembly and completed assemblies are differentiated within one state.
Two supplied ports can be spanned by a newly assembled bar. The supplied contact
law then permits two joints in one work operation; manual formation makes one
joint per operation. This efficiency is a model premise, not a physical derivation.
The bar is reusable, persists after products, and is not a stored partial product.

Targets are explicit trees on a,b,c roles, distinguished at a common address.
No ethical predicate, innovation beyond these recipes, or universal future
reachability claim is defined. Dismantling comparisons retain the disconnected
bar's material and do not refund its historical construction work.
-/

namespace FormationRoutes

inductive Role where
  | a | b | c
  deriving DecidableEq, Repr

inductive Tree where
  | atom (role : Role)
  | join (left right : Tree)
  deriving DecidableEq, Repr

def parts : Tree → Nat
  | .atom _ => 1
  | .join l r => parts l + parts r

inductive Port where
  | left | right
  deriving DecidableEq, Repr

def inspect : Tree → List Port → Option Role
  | .atom r, [] => some r
  | .join l _, .left :: path => inspect l path
  | .join _ r, .right :: path => inspect r path
  | _, _ => none

def dyadAB : Tree := .join (.atom .a) (.atom .b)
def dyadBC : Tree := .join (.atom .b) (.atom .c)
def leftForm : Tree := .join dyadAB (.atom .c)
def rightForm : Tree := .join (.atom .a) dyadBC

theorem common_address_distinguishes :
    inspect leftForm [.left, .left] = some .a ∧
    inspect rightForm [.left, .left] = none := by
  exact ⟨rfl, rfl⟩

theorem forms_distinct : leftForm ≠ rightForm := by decide

inductive Bar where
  | absent
  | loose
  | span (first second : Port)
  deriving DecidableEq, Repr

def barParts : Bar → Nat
  | .absent => 0
  | _ => 1

def Spans : Bar → Prop
  | .span p q => p ≠ q
  | _ => False

instance spansDecidable (b : Bar) : Decidable (Spans b) := by
  cases b <;> unfold Spans <;> infer_instance

structure Lot where
  raw : Nat
  work : Nat
  deriving DecidableEq, Repr

structure State where
  source : Option Lot
  raw : Nat
  work : Nat
  spent : Nat
  bar : Bar
  pending : Option Tree
  products : List Tree
  deriving DecidableEq, Repr

def initial (raw work : Nat) : State := ⟨some ⟨raw,work⟩, 0, 0, 0, .absent, none, []⟩
def stocked (raw work : Nat) : State := ⟨none, raw, work, 0, .absent, none, []⟩

inductive Event where
  | receive | attach | repair
  | startAB | startBC | finishLeft | finishRight | syncLeft | syncRight
  deriving DecidableEq, Repr

def advance (s : State) : Event → State
  | .receive => match s.source with
    | none => s
    | some lot => {s with source := none, raw := s.raw + lot.raw, work := s.work + lot.work}
  | .attach => {s with raw := s.raw - 1, work := s.work - 1,
                       spent := s.spent + 1, bar := .span .left .right}
  | .repair => {s with work := s.work - 1, spent := s.spent + 1, bar := .span .left .right}
  | .startAB => {s with raw := s.raw - 2, work := s.work - 1,
                        spent := s.spent + 1, pending := some dyadAB}
  | .startBC => {s with raw := s.raw - 2, work := s.work - 1,
                        spent := s.spent + 1, pending := some dyadBC}
  | .finishLeft => {s with raw := s.raw - 1, work := s.work - 1,
                           spent := s.spent + 1, pending := none, products := leftForm :: s.products}
  | .finishRight => {s with raw := s.raw - 1, work := s.work - 1,
                            spent := s.spent + 1, pending := none, products := rightForm :: s.products}
  | .syncLeft => {s with raw := s.raw - 3, work := s.work - 1,
                         spent := s.spent + 1, products := leftForm :: s.products}
  | .syncRight => {s with raw := s.raw - 3, work := s.work - 1,
                          spent := s.spent + 1, products := rightForm :: s.products}

def Enabled (s : State) : Event → Prop
  | .receive => s.source.isSome = true
  | .attach => s.bar = .absent ∧ 1 ≤ s.raw ∧ 1 ≤ s.work
  | .repair => s.bar = .loose ∧ 1 ≤ s.work
  | .startAB | .startBC => s.pending = none ∧ 2 ≤ s.raw ∧ 1 ≤ s.work
  | .finishLeft => s.pending = some dyadAB ∧ 1 ≤ s.raw ∧ 1 ≤ s.work
  | .finishRight => s.pending = some dyadBC ∧ 1 ≤ s.raw ∧ 1 ≤ s.work
  | .syncLeft | .syncRight => Spans s.bar ∧ s.pending = none ∧ 3 ≤ s.raw ∧ 1 ≤ s.work

instance enabledDecidable (s : State) (e : Event) : Decidable (Enabled s e) := by
  cases e <;> unfold Enabled <;> infer_instance

def Step (s : State) (e : Event) (t : State) : Prop := Enabled s e ∧ t = advance s e
def process : Generative.Process State Event := ⟨Step⟩

def Synchronized (e : Event) : Prop := e = .syncLeft ∨ e = .syncRight
def bypassProcess : Generative.Process State Event := ⟨fun s e t => Step s e t ∧ ¬ Synchronized e⟩

def children (s : State) : List State :=
  ([Event.receive, .attach, .repair, .startAB, .startBC, .finishLeft,
    .finishRight, .syncLeft, .syncRight].filter (fun e => decide (Enabled s e))).map (advance s)

theorem finite_branching (s t : State) : (∃ e, Step s e t) ↔ t ∈ children s := by
  constructor
  · rintro ⟨e, enabled, rfl⟩
    apply List.mem_map.mpr
    refine ⟨e, List.mem_filter.mpr ⟨?_, by simpa using enabled⟩, rfl⟩
    cases e <;> simp
  · intro h
    obtain ⟨e, he, rfl⟩ := List.mem_map.mp h
    exact ⟨e, of_decide_eq_true (List.mem_filter.mp he).2, rfl⟩

def sourceRaw (s : State) : Nat := (s.source.getD ⟨0,0⟩).raw
def sourceWork (s : State) : Nat := (s.source.getD ⟨0,0⟩).work
def partialParts (s : State) : Nat := (s.pending.map parts).getD 0
def productParts : List Tree → Nat
  | [] => 0
  | t :: ts => parts t + productParts ts

/-- Two seed ports plus every supplied part, including source and stored bar. -/
def material (s : State) : Nat := 2 + sourceRaw s + s.raw + barParts s.bar + partialParts s + productParts s.products
def workAccount (s : State) : Nat := sourceWork s + s.work + s.spent
def manualProgress (s : State) : Nat := 2 * s.products.length + if s.pending.isSome then 1 else 0

theorem disconnected_step_is_bypass {s t : State} {e : Event}
    (h : Step s e t) (disconnected : ¬ Spans s.bar) : ¬ Synchronized e := by
  rintro (rfl | rfl) <;> exact disconnected h.1.1

theorem step_accounts {s t : State} {e : Event} (h : Step s e t) :
    material t = material s ∧ workAccount t = workAccount s := by
  obtain ⟨he, rfl⟩ := h
  cases e with
  | receive =>
    cases hs : s.source with
    | none => simp [Enabled, hs] at he
    | some lot =>
      simp only [advance, hs, material, workAccount, sourceRaw, sourceWork, partialParts,
        Option.getD_some, Option.getD_none]
      exact ⟨by omega, by omega⟩
  | attach | repair | startAB | startBC | finishLeft | finishRight | syncLeft | syncRight =>
    simp_all [Enabled, advance, material, workAccount, sourceRaw, sourceWork, partialParts,
      barParts, productParts, parts, dyadAB, dyadBC, leftForm, rightForm]
    all_goals (first | exact ⟨by omega, by omega⟩ | omega)

theorem trace_accounts {s t : State} {es : List Event}
    (h : Generative.Trace process s es t) :
    material t = material s ∧ workAccount t = workAccount s := by
  induction h with
  | nil => exact ⟨rfl,rfl⟩
  | cons hs _ ih =>
    have one := step_accounts hs
    exact ⟨ih.1.trans one.1, ih.2.trans one.2⟩

theorem bypass_step_progress {s t : State} {e : Event}
    (h : Step s e t) (bypass : ¬ Synchronized e)
    (bound : manualProgress s ≤ s.spent) : manualProgress t ≤ t.spent := by
  obtain ⟨he,rfl⟩ := h
  cases e with
  | receive =>
    cases hs : s.source with
    | none => simp [Enabled,hs] at he
    | some lot => simpa [advance, hs, manualProgress] using bound
  | attach | repair =>
    exact Nat.le_trans bound (Nat.le_succ s.spent)
  | startAB | startBC | finishLeft | finishRight =>
    simp_all [Enabled, advance, manualProgress]
    all_goals omega
  | syncLeft | syncRight => simp [Synchronized] at bypass

theorem bypass_trace_progress {s t : State} {es : List Event}
    (h : Generative.Trace bypassProcess s es t)
    (bound : manualProgress s ≤ s.spent) : manualProgress t ≤ t.spent := by
  induction h with
  | nil => exact bound
  | cons hs _ ih => exact ih (bypass_step_progress hs.1 hs.2 bound)

theorem forget_bypass {s t : State} {es : List Event}
    (h : Generative.Trace bypassProcess s es t) : Generative.Trace process s es t := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons hs.1 ih

theorem bypass_output_bound (raw work : Nat) {t : State} {es : List Event}
    (h : Generative.Trace bypassProcess (initial raw work) es t) :
    2 * t.products.length ≤ work := by
  have progress := bypass_trace_progress h (by simp [initial, manualProgress])
  have account := (trace_accounts (forget_bypass h)).2
  simp only [initial, workAccount, sourceWork, Option.getD_some, Nat.add_zero] at account
  unfold manualProgress at progress
  omega

theorem bypass_three_work_at_most_one {t : State} {es : List Event}
    (h : Generative.Trace bypassProcess (initial 7 3) es t) : t.products.length ≤ 1 := by
  have bound := bypass_output_bound 7 3 h
  omega

theorem unfed_step_spends {s t : State} {e : Event}
    (h : Step s e t) (unfed : s.source = none) :
    t.source = none ∧ t.work + 1 = s.work := by
  obtain ⟨he,rfl⟩ := h
  cases e <;> simp_all [Enabled, advance]
  all_goals omega

theorem zero_work_no_step {s : State} (unfed : s.source = none) (empty : s.work = 0) :
    ∀ e t, ¬ Step s e t := by
  intro e t h
  have spent := (unfed_step_spends h unfed).2
  omega

theorem zero_work_trace_constant {s t : State} {es : List Event}
    (h : Generative.Trace process s es t) (unfed : s.source = none) (empty : s.work = 0) : t = s := by
  cases h with
  | nil => rfl
  | cons hs _ => exact False.elim (zero_work_no_step unfed empty _ _ hs)

theorem disconnected_fresh_step_no_product {s t : State} {e : Event}
    (h : Step s e t) (unfed : s.source = none) (fresh : s.pending = none)
    (disconnected : ¬ Spans s.bar) : t.products = s.products := by
  obtain ⟨he,rfl⟩ := h
  cases e <;> simp_all [Enabled, advance]

theorem disconnected_one_work_no_product {s t : State} {es : List Event}
    (h : Generative.Trace process s es t) (unfed : s.source = none)
    (fresh : s.pending = none) (disconnected : ¬ Spans s.bar) (budget : s.work ≤ 1) :
    t.products = s.products := by
  cases h with
  | nil => rfl
  | cons hs tail =>
    have first := disconnected_fresh_step_no_product hs unfed fresh disconnected
    have next := unfed_step_spends hs unfed
    have empty := zero_work_trace_constant tail next.1 (by omega)
    rw [empty]
    exact first

/-- The intervention changes placement only; historical spent work is retained. -/
def disconnect (s : State) : State := {s with bar := .loose}

theorem disconnection_preserves_support (s : State) (connected : Spans s.bar) :
    material (disconnect s) = material s ∧ workAccount (disconnect s) = workAccount s ∧
    (disconnect s).raw = s.raw ∧ (disconnect s).work = s.work ∧
    (disconnect s).spent = s.spent ∧ (disconnect s).products = s.products := by
  cases hb : s.bar with
  | absent | loose => simp [hb,Spans] at connected
  | span p q => simp [disconnect, material, workAccount, sourceRaw, sourceWork, partialParts, hb, barParts]

inductive Form where
  | left | right
  deriving DecidableEq, Repr

def treeOf : Form → Tree
  | .left => leftForm
  | .right => rightForm

def syncEvent : Form → Event
  | .left => .syncLeft
  | .right => .syncRight

def startEvent : Form → Event
  | .left => .startAB
  | .right => .startBC

def finishEvent : Form → Event
  | .left => .finishLeft
  | .right => .finishRight

def dyadOf : Form → Tree
  | .left => dyadAB
  | .right => dyadBC

/-- A source-funded, already formed bar; the work spent forming it remains present. -/
def ready (remaining : Nat) (products : List Tree) : State :=
  ⟨none, 3*remaining, remaining, 1+products.length, .span .left .right, none, products⟩

def pushed : List Form → List Tree → List Tree
  | [], products => products
  | f :: fs, products => pushed fs (treeOf f :: products)

theorem pushed_length (forms : List Form) (products : List Tree) :
    (pushed forms products).length = forms.length + products.length := by
  induction forms generalizing products with
  | nil => simp [pushed]
  | cons f fs ih => simp only [pushed, ih, List.length_cons]; omega

theorem receive_step (raw work : Nat) : Step (initial raw work) .receive (stocked raw work) := by
  exact ⟨rfl, by simp [stocked, initial, advance]⟩

theorem attach_step (n : Nat) : Step (stocked (3*n+1) (n+1)) .attach (ready n []) := by
  constructor
  · exact ⟨rfl, by simp [stocked], by simp [stocked]⟩
  · simp [stocked, ready, advance]

theorem formed_prefix (n : Nat) :
    Generative.Trace process (initial (3*n+1) (n+1)) [.receive,.attach] (ready n []) := by
  exact .cons (receive_step _ _) (.cons (attach_step n) (.nil _))

theorem synchronized_step (f : Form) (n : Nat) (products : List Tree) :
    Step (ready (n+1) products) (syncEvent f) (ready n (treeOf f :: products)) := by
  cases f <;> constructor
  all_goals simp [Enabled, ready, syncEvent, treeOf, Spans, advance, Nat.mul_add]
  all_goals omega

theorem synchronized_list (forms : List Form) (products : List Tree) :
    Generative.Trace process (ready forms.length products) (forms.map syncEvent)
      (ready 0 (pushed forms products)) := by
  induction forms generalizing products with
  | nil => exact .nil _
  | cons f fs ih => exact .cons (synchronized_step f fs.length products) (ih (treeOf f :: products))

theorem formed_joint_history (forms : List Form) :
    Generative.Trace process (initial (3*forms.length+1) (forms.length+1))
      ([.receive,.attach] ++ forms.map syncEvent) (ready 0 (pushed forms [])) := by
  exact Generative.trace_append_iff.mpr ⟨ready forms.length [], formed_prefix _, synchronized_list forms []⟩

theorem formed_joint_costs (forms : List Form) :
    (ready 0 (pushed forms [])).products.length = forms.length ∧
    (ready 0 (pushed forms [])).spent = forms.length+1 ∧
    (ready 0 (pushed forms [])).raw = 0 ∧ (ready 0 (pushed forms [])).work = 0 ∧
    (ready 0 (pushed forms [])).bar = .span .left .right := by
  simp [ready, pushed_length, Nat.add_comm]

theorem multiple_completions_exceed_bypass (n : Nat) (multiple : 2 ≤ n)
    {es : List Event} {t : State}
    (h : Generative.Trace bypassProcess (initial (3*n+1) (n+1)) es t) : t.products.length < n := by
  have bound := bypass_output_bound (3*n+1) (n+1) h
  omega

theorem both_forms_in_one_history :
    Generative.Trace process (initial 7 3)
      [.receive,.attach,.syncLeft,.syncRight] (ready 0 [rightForm,leftForm]) := by
  exact formed_joint_history [.left,.right]

theorem both_forms_unreachable_by_bypass {t : State} {es : List Event}
    (h : Generative.Trace bypassProcess (initial 7 3) es t) :
    t.products ≠ [rightForm,leftForm] := by
  intro products
  have bound := bypass_three_work_at_most_one h
  simp [products] at bound

def manualPending (f : Form) (bar : Bar) (surplus work spent : Nat) (products : List Tree) : State :=
  ⟨none, surplus+1, work+1, spent+1, bar, some (dyadOf f), products⟩

def manualResult (f : Form) (bar : Bar) (surplus work spent : Nat) (products : List Tree) : State :=
  ⟨none, surplus, work, spent+2, bar, none, treeOf f :: products⟩

theorem manual_two_steps (f : Form) (bar : Bar) (surplus work spent : Nat) (products : List Tree) :
    Generative.Trace bypassProcess ⟨none, surplus+3, work+2, spent, bar, none, products⟩
      [startEvent f, finishEvent f] (manualResult f bar surplus work spent products) := by
  refine Generative.Trace.cons (m := manualPending f bar surplus work spent products) ?_ ?_
  · cases f <;> simp [bypassProcess, Step, Enabled, advance, startEvent, manualPending, dyadOf, Synchronized]
  · refine Generative.Trace.cons (m := manualResult f bar surplus work spent products) ?_ ?_
    · cases f <;> simp [bypassProcess, Step, Enabled, advance, finishEvent, manualPending, manualResult, dyadOf, treeOf, Synchronized]
    · exact .nil _

theorem either_form_without_coupling (f : Form) :
    Generative.Trace bypassProcess (initial 7 3)
      [.receive, startEvent f, finishEvent f] (manualResult f .absent 4 1 0 []) := by
  apply Generative.Trace.cons
  · exact ⟨receive_step 7 3, by simp [Synchronized]⟩
  · exact manual_two_steps f .absent 4 1 0 []

theorem matched_connected_can_finish (f : Form) :
    Generative.Trace process (ready 1 []) [syncEvent f] (ready 0 [treeOf f]) := by
  exact .cons (synchronized_step f 0 []) (.nil _)

theorem matched_disconnected_cannot_finish {t : State} {es : List Event}
    (h : Generative.Trace process (disconnect (ready 1 [])) es t) : t.products = [] := by
  exact disconnected_one_work_no_product h rfl rfl (by simp [disconnect,Spans]) (by decide)

theorem repair_uses_last_work :
    Step (disconnect (ready 1 [])) .repair
      ⟨none, 3, 0, 2, .span .left .right, none, []⟩ := by
  exact ⟨⟨rfl, by decide⟩, rfl⟩

theorem connected_underfunded_cannot_finish {t : State} {es : List Event}
    (h : Generative.Trace process {ready 1 [] with work := 0} es t) : t.products = [] := by
  rw [zero_work_trace_constant h rfl rfl]
  rfl

theorem redundant_for_single_target_with_two_work (f : Form) :
    Generative.Trace bypassProcess {disconnect (ready 1 []) with work := 2}
      [startEvent f, finishEvent f] (manualResult f .loose 0 0 1 []) := by
  exact manual_two_steps f .loose 0 0 1 []

end FormationRoutes
